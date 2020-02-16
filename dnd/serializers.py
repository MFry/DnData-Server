from rest_framework import serializers
from .models import Campaign, Character, Player


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ("id", "name", "active")


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "name", "active", "campaign")


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("id", "name", "character")

