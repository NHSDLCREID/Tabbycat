from django.conf import settings
from django.contrib import messages
from django.db.models import Prefetch, Q
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy, ngettext
from django.views.generic.base import TemplateView

from actionlog.mixins import LogActionMixin
from actionlog.models import ActionLogEntry
from notifications.models import BulkNotification
from notifications.views import RoleColumnMixin, RoundTemplateEmailCreateView
from participants.models import Speaker
from tournaments.mixins import (CurrentRoundMixin, OptionalAssistantTournamentPageMixin,
                                PublicTournamentPageMixin, RoundMixin, TournamentMixin)
from tournaments.models import Round
from utils.misc import redirect_round
from utils.mixins import AdministratorMixin
from utils.views import ModelFormSetView, PostOnlyRedirectView

from .models import Motion, RoundMotion
from .statistics import MotionBPStatsCalculator, MotionTwoTeamStatsCalculator, RoundMotionBPStatsCalculator, RoundMotionTwoTeamStatsCalculator


class PublicMotionsView(PublicTournamentPageMixin, TemplateView):
    public_page_preference = 'public_motions'

    def get_template_names(self):
        return ['public_motions.html']

    def get_context_data(self, **kwargs):
        order_by = 'seq' if self.tournament.pref('public_motions_order') == 'forward' else '-seq'

        # Include rounds whether *either* motions are released *or* it's this
        # round or a previous round. The template checks motion_released again
        # and displays a "not released" message if motions are not released.
        filter_q = Q(motions_released=True) | Q(seq__lte=self.tournament.current_round.seq)

        kwargs['rounds'] = self.tournament.round_set.filter(filter_q).order_by(
                order_by).prefetch_related(Prefetch('motion_set', queryset=Motion.objects.order_by('roundmotions__seq')))
        return super().get_context_data(**kwargs)


class EditMotionsView(AdministratorMixin, LogActionMixin, RoundMixin, ModelFormSetView):
    # Django doesn't have a class-based view for formsets, so this implements
    # the form processing analogously to FormView, with less decomposition.

    template_name = 'motions_edit.html'
    action_log_type = ActionLogEntry.ACTION_TYPE_MOTION_EDIT
    formset_model = Motion

    def get_formset_factory_kwargs(self):
        excludes = ['round', 'id']

        nexisting = self.get_formset_queryset().count()
        if self.tournament.pref('enable_motions'):
            delete = True
            extra = max(3 - nexisting, 0)
        else:
            excludes.append('seq')
            extra = max(1 - nexisting, 0)
            delete = nexisting > 1  # if there's more than one, allow deletion

        return {'can_delete': delete, 'exclude': excludes, 'extra': extra}

    def get_formset_kwargs(self):
        nexisting = self.get_formset_queryset().count()
        nmotions = 3 if self.tournament.pref('enable_motions') else 1
        initial = [{'seq': i} for i in range(nexisting+1, nmotions+1)]
        return {'initial': initial}

    def get_formset_queryset(self):
        return self.round.motion_set.order_by('roundmotions__seq')

    def formset_valid(self, formset):
        motions = formset.save(commit=True)
        for i, motion in enumerate(motions, start=1):
            RoundMotion(motion=motion, round=self.round, seq=1).save()

            self.log_action(content_object=motion)

        return self.show_message(len(motions), len(formset.deleted_objects))

    def show_message(self, count, deleted):
        if not self.tournament.pref('enable_motions') and count == 1:
            messages.success(self.request, _("The motion has been saved."))
        elif count > 0:
            messages.success(self.request, ngettext("%(count)d motion has been saved.",
                "%(count)d motions have been saved.", count) % {'count': count})

        if deleted > 0:
            messages.success(self.request, ngettext("%(count)d motion has been deleted.",
                "%(count)d motions have been deleted.", deleted) % {'count': deleted})

        return redirect_round('draw-display', self.round)


class CopyMotionsView(EditMotionsView):
    formset_model = RoundMotion

    def get_formset_factory_kwargs(self):
        excludes = ['round', 'id']

        nexisting = self.get_formset_queryset().count()
        if self.tournament.pref('enable_motions'):
            delete = True
            extra = max(3 - nexisting, 0)
        else:
            excludes.append('seq')
            extra = max(1 - nexisting, 0)
            delete = nexisting > 1  # if there's more than one, allow deletion

        return {'can_delete': delete, 'exclude': excludes, 'extra': extra}

    def get_formset_queryset(self):
        return self.round.roundmotions_set.all()

    def formset_valid(self, formset):
        motions = formset.save(commit=False)
        for i, motion in enumerate(motions, start=1):
            if not self.tournament.pref('enable_motions'):
                motion.seq = i
            motion.round = self.round
            motion.save()

            self.log_action(content_object=motion.motion)

        for rm in formset.deleted_objects:
            rm.delete()

        return self.show_message(len(motions), len(formset.deleted_objects))


class CopyPreviousMotionsView(AdministratorMixin, LogActionMixin, RoundMixin, PostOnlyRedirectView):
    round_redirect_pattern_name = 'draw-display'
    action_log_type = ActionLogEntry.ACTION_TYPE_MOTION_EDIT

    def post(self, request, *args, **kwargs):
        self.round.roundmotions_set.all().delete()
        motions = self.round.prev.roundmotions_set.select_related('motion')
        new_motions = []

        for motion in motions:
            new_motions.append(RoundMotion(motion=motion.motion, seq=motion.seq, round=self.round))
            self.log_action(content_object=motion.motion)

        RoundMotion.objects.bulk_create(new_motions)
        messages.success(request, ngettext(
            "The motion was copied from the previous round.",
            "The %(count)d motions were copied from the previous round.",
            len(new_motions)) % {'count': len(new_motions)})
        return super().post(request, *args, **kwargs)


class BaseReleaseMotionsView(AdministratorMixin, LogActionMixin, RoundMixin, PostOnlyRedirectView):

    round_redirect_pattern_name = 'draw-display'

    def post(self, request, *args, **kwargs):
        round = self.round
        round.motions_released = self.motions_released
        round.save()
        self.log_action()

        messages.success(request, self.message_text)
        return super().post(request, *args, **kwargs)


class ReleaseMotionsView(BaseReleaseMotionsView):

    action_log_type = ActionLogEntry.ACTION_TYPE_MOTIONS_RELEASE
    motions_released = True
    message_text = _("Released the motion(s).")


class UnreleaseMotionsView(BaseReleaseMotionsView):

    action_log_type = ActionLogEntry.ACTION_TYPE_MOTIONS_UNRELEASE
    motions_released = False
    message_text = _("Unreleased the motion(s).")


class BaseDisplayMotionsView(RoundMixin, TemplateView):

    template_name = 'show.html'

    def get_context_data(self, **kwargs):
        kwargs['motions'] = self.round.roundmotions_set.select_related('motion').order_by('seq')
        kwargs['motions_length'] = sum(len(i.motion.text) for i in kwargs['motions'])
        kwargs['infos'] = self.round.roundmotions_set.select_related('motion').exclude(motion__info_slide="").order_by('seq')
        kwargs['infos_length'] = sum(len(i.motion.info_slide) for i in kwargs['infos'])
        return super().get_context_data(**kwargs)


class AdminDisplayMotionsView(AdministratorMixin, BaseDisplayMotionsView):
    pass


class AssistantDisplayMotionsView(CurrentRoundMixin, OptionalAssistantTournamentPageMixin, BaseDisplayMotionsView):
    assistant_page_permissions = ['all_areas']


class EmailMotionReleaseView(RoleColumnMixin, RoundTemplateEmailCreateView):
    page_subtitle = _("Round Motions")

    event = BulkNotification.EVENT_TYPE_MOTIONS
    subject_template = 'motion_email_subject'
    message_template = 'motion_email_message'

    round_redirect_pattern_name = 'draw-display'

    def get_default_send_queryset(self):
        return Speaker.objects.filter(team__round_availabilities__round=self.round, email__isnull=False).exclude(email__exact="")


class BaseMotionStatisticsView(TournamentMixin, TemplateView):
    template_name = 'motion_statistics.html'
    page_title = gettext_lazy("Motion Statistics")
    page_emoji = '💭'

    for_public = False

    def get_context_data(self, **kwargs):
        kwargs['statistics'] = self.get_statistics()
        kwargs['type'] = self.stats_type
        kwargs['for_public'] = self.for_public
        kwargs['stage'] = {'PRELIM': Round.STAGE_PRELIMINARY, 'ELIM': Round.STAGE_ELIMINATION}
        return super().get_context_data(**kwargs)


class RoundMotionStatisticsView(BaseMotionStatisticsView):
    stats_type = "round"

    def get_statistics(self, *args, **kwargs):
        if self.tournament.pref('teams_in_debate') == 'two':
            return RoundMotionTwoTeamStatsCalculator(self.tournament, *args, **kwargs)
        else:
            return RoundMotionBPStatsCalculator(self.tournament, *args, **kwargs)


class GlobalMotionStatisticsView(BaseMotionStatisticsView):
    stats_type = "global"

    def get_statistics(self, *args, **kwargs):
        if self.tournament.pref('teams_in_debate') == 'two':
            return MotionTwoTeamStatsCalculator(self.tournament, *args, **kwargs)
        else:
            return MotionBPStatsCalculator(self.tournament, *args, **kwargs)


class BasePublicMotionStatisticsView(PublicTournamentPageMixin):
    """Base class for public motion tabs

    Motion context provided in subclasses."""
    public_page_preference = 'motion_tab_released'
    cache_timeout = settings.TAB_PAGES_CACHE_TIMEOUT
    for_public = True


class AdminRoundMotionStatisticsView(AdministratorMixin, RoundMotionStatisticsView):
    pass


class AdminGlobalMotionStatisticsView(AdministratorMixin, GlobalMotionStatisticsView):
    pass


class PublicRoundMotionStatisticsView(BasePublicMotionStatisticsView, RoundMotionStatisticsView):
    pass


class PublicGlobalMotionStatisticsView(BasePublicMotionStatisticsView, GlobalMotionStatisticsView):
    pass
