from django.shortcuts import render
from django.http import HttpResponse
from test_app.room_populator import *
from test_app.models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# Create your views here.
def startuptest(request):
    output = 'this is a test'
    return HttpResponse(output)
    
@csrf_exempt
@api_view(["GET"])
def makeworld(request):
    Room_DB.objects.all().delete()
    Item_DB.objects.all().delete()
    pop_db()
    output = 'world created - please check graphql for details'
    return HttpResponse(output)

@csrf_exempt
@api_view(["GET"])
def makeitems(request):
    current_floor = request.user.player.currentRoom.strip('][').split(', ')[2]
    assign_items(current_floor=current_floor)
    output = 'items created - please check graphql for details'
    return HttpResponse(output)

