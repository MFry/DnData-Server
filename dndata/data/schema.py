import graphene
from graphene_django import DjangoObjectType
from graphene import Schema, relay, resolve_only_args, ObjectType

from .models import Character as CharacterModel
from .models import Campaign as CampaignModel
from .models import CharacterClass as CharacterClassModel
from .models import CharacterSubclass as CharacterSubclassModel
from .models import CharacterRace as CharacterRaceModel


class CharacterType(DjangoObjectType):
    class Meta:
        model = CharacterModel
        interface = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CampaignModel.objects.get(id=id)
        return node


class CampaignType(DjangoObjectType):
    class Meta:
        model = CampaignModel
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CampaignModel.objects.get(id=id)
        return node


class CharacterClassType(DjangoObjectType):
    class Meta:
        model = CharacterClassModel
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CharacterClassModel.objects.get(id=id)
        return node


class CharacterSubclassType(DjangoObjectType):
    class Meta:
        model = CharacterSubclassModel
        interface = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CharacterSubclassModel.objects.get(id=id)
        return node


class CharacterRaceType(DjangoObjectType):
    class Meta:
        model = CharacterRaceModel
        interface = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CharacterRaceModel.objects.get(id=id)
        return node


class Query(ObjectType):
    all_campaigns = graphene.List(CampaignType)
    all_characters = graphene.List(CharacterType)
    all_campaign_characters = graphene.List(
        CharacterType, campaign_name=graphene.String(required=True)
    )

    def resolve_all_campaigns(root, info):
        return CampaignModel.objects.all()

    def resolve_all_characters(root, info):
        return CharacterModel.objects.all()

    def resolve_all_campaign_characters(root, info, campaign_name):
        try:
            campaign = CampaignModel.objects.get(name=campaign_name)
            return CharacterModel.objects.filter(campaign=campaign)
        except (CharacterType.DoesNotExist, CampaignType.DoesNotExist):
            return None


schema = graphene.Schema(query=Query)
