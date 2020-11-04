import graphene

from .character import query as character_query
from .character import mutations as character_mutations


class Query(character_query.Query, graphene.ObjectType):
    # This class inherit from multiple Queries to create the final schema
    pass


class Mutation(character_mutations.Mutation, graphene.ObjectType):
    # This class inherit from multiple Mutations to create the final schema
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
