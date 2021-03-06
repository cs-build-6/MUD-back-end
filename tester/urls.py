"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from test_app.views import *
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from test_app.api import *

from graphene_django.views import GraphQLView

urlpatterns = [
    url('makeitems', makeitems),
    path('say/',say, name = 'say with pusher"'),
    path('grid',grid, name = 'grid'),
    url('init', initialize),
    url('move', move),
    url('look', look),
    url('pick', pick),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    #path('', startuptest, name = 'startupscreen'),
    path('makeworld/', makeworld, name = 'makenewworld'),
    # path('makeitems/', makeitems, name = 'makenewitems'),
    path('admin/', admin.site.urls),
    #path('graphql/', GraphQLView.as_view(graphiql=True))
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
