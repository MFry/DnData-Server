import graphene
from graphene import Mutation, ObjectType
from graphql import GraphQLError
from ..models.players import *


# class CreatePlayer(Mutation):
#     id = graphene.ID()
#     name = graphene.String()
#     character_class = graphene.ID()


class CreateCharacterSubclass(Mutation):
    id = graphene.ID()
    character_class = graphene.ID()
    name = graphene.String()
    url = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        character_class_id = graphene.ID()
        character_class = graphene.String()
        url = graphene.String()

    def mutate(self, info, name, url, **kwargs):
        char_class = None
        character_class_id = kwargs.get("character_class_id", None)
        character_class = kwargs.get("character_class", None)

        if not character_class_id and not character_class:
            raise GraphQLError(
                'Either "character_class_id" or "character_class" must be supplied.'
            )
        if character_class_id:
            char_class = CharacterClass.objects.get(pk=character_class_id)
        else:
            char_class = CharacterClass.objects.get(name=character_class)

        characterSubClass = CharacterSubclass.objects.create_class(
            name=name, url=url, character_class=char_class
        )
        return CreateCharacterSubclass(
            id=characterSubClass.pk,
            name=characterSubClass.name,
            url=characterSubClass.url,
            character_class=characterSubClass.character_class,
        )


class CreateCharacterClass(Mutation):
    id = graphene.ID()
    name = graphene.String()
    url = graphene.String()

    class Arguments:
        name = graphene.String(required=True)
        url = graphene.String()

    def mutate(self, info, name, url):
        characterClass = CharacterClass.objects.create_class(name=name, url=url)
        return CreateCharacterClass(
            id=characterClass.pk, name=characterClass.name, url=characterClass.url
        )


class Mutation(ObjectType):
    create_character_class = CreateCharacterClass.Field()
    create_character_subclass = CreateCharacterSubclass.Field()
