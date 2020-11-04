import graphene
from graphene import Schema, relay, resolve_only_args, ObjectType

from .types import *


class Query(ObjectType):
    all_campaigns = graphene.List(CampaignType)
    all_characters = graphene.List(CharacterType)
    all_character_classes = graphene.List(CharacterClassType)
    all_races = graphene.List(CharacterRaceType)
    all_campaign_characters = graphene.List(
        CharacterType, campaign_name=graphene.String(required=True)
    )

    def resolve_all_campaigns(root, info):
        return CampaignModel.objects.all()

    def resolve_all_characters(root, info):
        return CharacterModel.objects.all()

    def resolve_all_character_classes(root, info):
        return CharacterClassModel.objects.all()

    def resolve_all_races(root, info):
        return RaceModel.objects.all()

    def resolve_all_campaign_characters(root, info, campaign_name):
        try:
            campaign = CampaignModel.objects.get(name=campaign_name)
            return CharacterModel.objects.filter(campaign=campaign)
        except (CharacterType.DoesNotExist, CampaignType.DoesNotExist):
            return None
