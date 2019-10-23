from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def startuptest(request):
    output = 'this is a test'
    return HttpResponse(output)

