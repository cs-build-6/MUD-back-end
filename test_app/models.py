from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

class Room_DB(models.Model):
    """db of one instance of generator"""
    id = models.CharField(primary_key=True, max_length = 20)
    coords = models.CharField(max_length = 20)
    description = models.CharField(max_length=500)
    x = models.IntegerField()
    y = models.IntegerField()
    floor = models.IntegerField()
    n_to = models.CharField(max_length = 20,null=True)
    s_to = models.CharField(max_length = 20,null=True)
    e_to = models.CharField(max_length = 20,null=True)
    w_to = models.CharField(max_length = 20,null=True)
    u_to = models.CharField(max_length = 20,null=True)
    d_to = models.CharField(max_length = 20,null=True)
    region = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    roomitemsids = models.CharField(max_length = 100,null=True)

class Item_DB(models.Model):
    id = models.AutoField(primary_key=True)
    noun = models.CharField(max_length = 50)
    skill = models.CharField(max_length = 50)
    item_room = models.CharField(max_length = 50,null=True)
    item_owner = models.CharField(max_length = 50,null=True)



    



