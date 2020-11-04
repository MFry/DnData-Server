import graphene
from graphene_django import DjangoObjectType
from graphene import relay

from ..models import Character as CharacterModel
from ..models import Campaign as CampaignModel
from ..models import CharacterClass as CharacterClassModel
from ..models import CharacterSubclass as CharacterSubclassModel
from ..models import Race as RaceModel


class CharacterType(DjangoObjectType):
    pk = graphene.ID(source="pk")

    class Meta:
        model = CharacterModel
        interface = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CampaignModel.objects.get(id=id)
        return node


class CampaignType(DjangoObjectType):
    pk = graphene.ID(source="pk")

    class Meta:
        model = CampaignModel
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = CampaignModel.objects.get(id=id)
        return node


class CharacterClassType(DjangoObjectType):
    pk = graphene.ID(source="pk")

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
        model = RaceModel
        interface = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        node = RaceModel.objects.get(id=id)
        return node
