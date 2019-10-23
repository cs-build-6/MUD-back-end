from django.shortcuts import render
from django.http import HttpResponse
from test_app.room_populator import *
from test_app.models import *


# Create your views here.
def startuptest(request):
    output = 'this is a test'
    return HttpResponse(output)

def makeworld(request):
    pop_db()
    output = 'world created - please check graphql for details'
    return HttpResponse(output)

def makeitems(request):
    pop_items()
    output = 'items created - please check graphql for details'
    return HttpResponse(output)

