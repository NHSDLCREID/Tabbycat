from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from tournaments.mixins import TournamentMixin

from . import serializers


class TournamentAPIMixin(TournamentMixin):
    tournament_field = 'tournament'

    def perform_create(self, serializer):
        serializer.save(**{self.tournament_field: self.tournament})

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(**{self.tournament_field: self.tournament})

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['tournament'] = self.tournament
        return context


class AdministratorAPIMixin:
    permission_classes = [IsAdminUser]


class BreakCategoryViewSet(TournamentAPIMixin, AdministratorAPIMixin, ModelViewSet):
    serializer_class = serializers.BreakCategorySerializer
    lookup_field = 'slug'


class SpeakerCategoryViewSet(TournamentAPIMixin, AdministratorAPIMixin, ModelViewSet):
    serializer_class = serializers.SpeakerCategorySerializer
    lookup_field = 'slug'


class BreakEligibilityView(TournamentAPIMixin, AdministratorAPIMixin, RetrieveUpdateAPIView):
    serializer_class = serializers.BreakEligibilitySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('team_set')


class SpeakerEligibilityView(TournamentAPIMixin, AdministratorAPIMixin, RetrieveUpdateAPIView):
    serializer_class = serializers.SpeakerEligibilitySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('speaker_set')
