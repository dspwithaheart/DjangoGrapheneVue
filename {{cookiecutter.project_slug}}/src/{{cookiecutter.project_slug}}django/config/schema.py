import graphene
import graphql_jwt

from django.db.models.base import ModelBase
from config.schemaFromModels import query_and_mutation_class
import {{cookiecutter.project_slug}}django.models  as all_models




def get_models_as_list(all_models):
    models = []
    for name in dir(all_models):
        model = getattr(all_models, name)
        if type(model) == ModelBase:
            models.append(model)
    return models

query_class, mutation_class = query_and_mutation_class(get_models_as_list(all_models))

class JwtMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(query_class, graphene.ObjectType):
    pass


class Mutation(JwtMutation, mutation_class, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
