import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id

from graphene import relay, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation


from graphene_django.converter import convert_django_field
from rest_framework.serializers import ModelSerializer


def add_model_query(model):
    model_metaclass = type(
        f"Meta",
        (),
        {
            "model": model,
            "filter_fields": [
                field.name
                for field in model._meta.get_fields()
                # if not isinstance(field, OracleXMLTypeField)
            ],
            "interfaces": (relay.Node,),
        },
    )
    model_node = type(
        f"{model.__name__}Node", (DjangoObjectType,), {"Meta": model_metaclass}
    )

    return model_node


def add_model_mutation(serializer):
    mutation_metaclass = type(
        f"Meta",
        (),
        {"serializer_class": serializer, "model_operations": ["create", "update"]},
    )
    model_mutation = type(
        f"{serializer.__name__}Mutation",
        (SerializerMutation,),
        {"Meta": mutation_metaclass},
    )

    return model_mutation


def serializer_factory(model):
    cls_name = f"{model.__name__}Serializer"
    return type(
        cls_name,
        (ModelSerializer,),
        {"Meta": type("Meta", (), {"model": model, "fields": "__all__"})},
    )


def query_and_mutation_class(models):
    """
    # Generates GraphQL Relay query and mutations for standard models
    :param models:
    :return:
    """
    query_class = type("QueryClass", (graphene.ObjectType,), {})

    mutation_class = type("MutationClass", (graphene.ObjectType,), {})

    for model in models:
        model_node = add_model_query(model)
        setattr(query_class, f"{model.__name__.lower()}", relay.Node.Field(model_node))
        setattr(
            query_class,
            f"all_{model.__name__.lower()}",
            DjangoFilterConnectionField(model_node),
        )

        # generate serializer on the fly
        serializer = serializer_factory(model)
        model_mutation = add_model_mutation(serializer)
        setattr(
            mutation_class,
            f"mutate{model.__name__}",
            model_mutation.Field(),
        )

    return query_class, mutation_class


def query_and_mutation_class_with_serializer(models, serializers):
    """
    # Generates GraphQL Relay query and mutations for standard models with custom serializer

    :param models:
    :param serializers:
    :return:  a list of Relay query and mutation classes
    """
    query_class = type("QueryClass", (graphene.ObjectType,), {})

    mutation_class = type("MutationClass", (graphene.ObjectType,), {})

    for model in models:
        model_node = add_model_query(model)
        setattr(query_class, f"{model.__name__.lower()}", relay.Node.Field(model_node))
        setattr(
            query_class,
            f"all_{model.__name__.lower()}",
            DjangoFilterConnectionField(model_node),
        )

    for serializer in serializers:
        model_mutation = add_model_mutation(serializer)
        setattr(
            mutation_class,
            f"{serializer.__name__.lower()}Mutate",
            model_mutation.Field(),
        )

    return query_class, mutation_class
