from django.db import models
from uuid import uuid4
import uuid

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    playerNames = models.CharField(max_length = 100,null=True)

class Item_DB(models.Model):
    id = models.AutoField(primary_key=True)
    noun = models.CharField(max_length = 50)
    skill = models.CharField(max_length = 50)
    item_room = models.CharField(max_length = 50,null=True)
    item_owner = models.CharField(max_length = 50,null=True)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room_DB.objects.first().id
            self.save()
    def room(self):
        try:
            return Room_DB.objects.get(id=self.currentRoom)
        except Room_DB.DoesNotExist:
            self.initialize()
            return self.room()

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()



    



