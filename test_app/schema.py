from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Room_DB

class Room_DBType(DjangoObjectType):

    class Meta:
        model = Room_DB

        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    rooms = graphene.List(Room_DBType)


    def resolve_rooms(self, info):
        return Room_DB.objects.all()

schema = graphene.Schema(query=Query)