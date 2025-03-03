from rest_framework import viewsets
from .models import Superheroe, SuperPower, League
from .serializers import SuperheroeSerializer, SuperPowerSerializer, LeagueSerializer

class SuperheroeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing superheroes.
    """
    queryset = Superheroe.objects.all()
    serializer_class = SuperheroeSerializer

class SuperPowerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing superpowers.
    """
    queryset = SuperPower.objects.all()
    serializer_class = SuperPowerSerializer

class LeagueViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing leagues.
    """
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
