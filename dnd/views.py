from .models import Player, Character, Campaign
from .serializers import PlayerSerializer, CharacterSerializer, CampaignSerializer
from rest_framework import generics


class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
