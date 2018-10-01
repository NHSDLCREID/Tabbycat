import logging

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import get_object_or_404
from django.utils.text import format_lazy
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from checkins.models import PersonIdentifier
from checkins.utils import get_unexpired_checkins
from notifications.models import SentMessageRecord
from participants.models import Adjudicator, Person, Speaker
from tournaments.mixins import PersonalizablePublicTournamentPageMixin, TournamentMixin
from utils.misc import reverse_tournament
from utils.mixins import AdministratorMixin
from utils.tables import TabbycatTableBuilder
from utils.views import PostOnlyRedirectView, VueTableTemplateView

from .utils import populate_url_keys

logger = logging.getLogger(__name__)


class RandomisedUrlsMixin(AdministratorMixin, TournamentMixin):

    def get_context_data(self, **kwargs):
        # These are used to choose the nav display
        tournament = self.tournament
        kwargs['exists'] = tournament.participants.filter(url_key__isnull=False).exists()
        kwargs['blank_exists'] = tournament.participants.filter(url_key__isnull=True).exists()
        kwargs['to_email_exists'] = self.get_participants_to_email().exists()
        return super().get_context_data(**kwargs)

    def get_participants_to_email(self, already_sent=False):
        subquery = SentMessageRecord.objects.filter(
            event=SentMessageRecord.EVENT_TYPE_URL,
            tournament=self.tournament, email=OuterRef('email')
        )
        people = self.tournament.participants.filter(
            url_key__isnull=False, email__isnull=False
        ).exclude(
            email__exact=""
        ).annotate(
            already_sent=Exists(subquery)
        ).filter(already_sent=already_sent)
        return people


class RandomisedUrlsView(RandomisedUrlsMixin, VueTableTemplateView):

    template_name = 'private_urls.html'
    tables_orientation = 'columns'

    def add_url_columns(self, table, people, request):
        def build_url(person):
            if person.url_key is None:
                return {'text': _("no URL"), 'class': 'text-warning'}
            path = reverse_tournament('privateurls-person-index', self.tournament,
                kwargs={'url_key': person.url_key})
            return {'text': request.build_absolute_uri(path), 'class': 'small'}

        def build_link(person):
            if person.url_key is None:
                return ''
            path = reverse_tournament('privateurls-person-index', self.tournament,
                kwargs={'url_key': person.url_key})
            return {'text': "🔗", 'link': request.build_absolute_uri(path)}

        table.add_column(
            {'title': _("URL"), 'key': "url"},
            [build_url(person) for person in people]
        )
        table.add_column(
            {'title': "", 'key': "key"},
            [build_link(person) for person in people]
        )
        return table

    def get_speakers_table(self):
        speakers = Speaker.objects.filter(team__tournament=self.tournament)
        table = TabbycatTableBuilder(view=self, title=_("Speakers"), sort_key="name")
        table.add_speaker_columns(speakers, categories=False)
        self.add_url_columns(table, speakers, self.request)

        return table

    def get_adjudicators_table(self):
        tournament = self.tournament

        adjudicators = Adjudicator.objects.all() if tournament.pref('share_adjs') else Adjudicator.objects.filter(tournament=tournament)
        table = TabbycatTableBuilder(view=self, title=_("Adjudicators"), sort_key="name")
        table.add_adjudicator_columns(adjudicators, show_institutions=False, show_metadata=False)
        self.add_url_columns(table, adjudicators, self.request)

        return table

    def get_tables(self):
        return [self.get_adjudicators_table(), self.get_speakers_table()]


class GenerateRandomisedUrlsView(AdministratorMixin, TournamentMixin, PostOnlyRedirectView):

    tournament_redirect_pattern_name = 'privateurls-list'

    def post(self, request, *args, **kwargs):
        tournament = self.tournament

        nexisting_people = tournament.participants.filter(url_key__isnull=False).count()
        blank_people = tournament.participants.filter(url_key__isnull=True)
        nblank_people = blank_people.count()

        if nblank_people == 0:
            messages.error(self.request, _("All participants already have private URLs. "
                "If you want to delete them, use the Edit Database area."))

        else:
            populate_url_keys(blank_people)

            generated_urls_message = ngettext(
                "A private URL was generated for %(nblank_people)d person.",
                "Private URLs were generated for all %(nblank_people)d people.",
                nblank_people
            ) % {'nblank_people': nblank_people}
            non_generated_urls_message = ngettext(
                "The already-existing private URL for %(nexisting_people)d person was left intact.",
                "The already-existing private URLs for %(nexisting_people)d people were left intact",
                nexisting_people
            ) % {'nexisting_people': nexisting_people}

            if nexisting_people == 0:
                messages.success(self.request, generated_urls_message)
            else:
                messages.success(self.request, format_lazy(generated_urls_message, " ", non_generated_urls_message))

        return super().post(request, *args, **kwargs)


class EmailRandomizedUrlsView(RandomisedUrlsMixin, PostOnlyRedirectView):

    tournament_redirect_pattern_name = 'privateurls-list'

    def post(self, request, *args, **kwargs):
        t = self.tournament

        path = reverse_tournament('privateurls-person-index', t, kwargs={'url_key': '0'})
        url = request.build_absolute_uri(path)[:-2]

        async_to_sync(get_channel_layer().send)("notifications", {
            "type": "email",
            "message": "url",
            "extra": {'url': url, 'tournament_id': t.id}
        })

        messages.success(self.request, _("Private URL emails have been successfully queued for sending."))

        people_no_email = t.participants.filter(
            Q(email__isnull=True) | Q(email__exact=""), url_key__isnull=False
        ).values_list('name', flat=True)

        if people_no_email:
            messages.warning(self.request, ngettext(
                "This participant does not have an email address: %(participants)s",
                "These %(count)d participants do not have an email address: %(participants)s",
                people_no_email.count()) % {'count': people_no_email.count(), 'participants': ", ".join(people_no_email)})

        return super().post(request, *args, **kwargs)


class PersonIndexView(PersonalizablePublicTournamentPageMixin, TemplateView):
    slug_field = 'url_key'
    slug_url_kwarg = 'url_key'

    template_name = 'public_url_landing.html'

    def is_page_enabled(self, tournament):
        return self.tournament.pref('participant_feedback') == 'private-urls' or self.tournament.pref('participant_ballots') == 'private-urls' or self.tournament.pref('public_checkins_submit')

    def get_context_data(self, **kwargs):
        t = self.tournament
        participant = get_object_or_404(Person, url_key=kwargs['url_key'])
        kwargs['person'] = participant
        try:
            checkin_id = PersonIdentifier.objects.get(person=participant)
            checkins = get_unexpired_checkins(t, 'checkin_window_people')
            kwargs['event'] = checkins.filter(identifier=checkin_id).first()
        except ObjectDoesNotExist:
            kwargs['event'] = False

        kwargs['feedback_pref'] = t.pref('participant_feedback') == 'private-urls'
        kwargs['ballots_pref'] = t.pref('participant_ballots') == 'private-urls'

        return super().get_context_data(**kwargs)
