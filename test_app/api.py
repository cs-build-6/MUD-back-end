from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    # print(f'name: {user.username}\n')
    players = room.playerNames(player_id)
    # print(f'user{user}, player{player}, player{player_id}\nuuid{uuid}, room{room}, player{players}')
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None: #and nextRoomID > 0:
        nextRoom = Room_DB.objects.get(coords=nextRoomID)   #changed id to coords
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

@csrf_exempt
@api_view(["POST"])
def look(request):
    player = request.user.player
    room = player.room()
    # IMPLEMENT
    return JsonResponse({'name':player.user.username, 
                            'title':room.title, 
                            'description':room.description,
                             'players':players, 
                             'items available' : room.itemdesc,
                             'floor' : room.floor,
                             'region' : room.region,
                             'inventory' : player.inv,
                             'error_msg':"You cannot move that way."}, safe=True)

@csrf_exempt
@api_view(["POST"])
def pick(request):
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    room = player.room()
    player_inv = player.inv()
    room_inv = room.roomitemsids
    
    if player_inv is None:
        player_inv = []
    else:
        player_inv = [int(x) for x in player_inv.strip('][').split(', ')]

    if room_inv is None:
        room_inv = []
    else:
        room_inv = [int(x) for x in room_inv.strip('][').split(', ')]

    pick_item = data['pick up']
    for thing in room_inv:
        if Item_DB.objects.get(id=thing).noun==pick_item or \
                        f'{Item_DB.objects.get(noun=thing)} of {Item_DB.objects.get(id=thing)}'==pick_item:


                        player_inv = player_inv + [thing]
                        room_inv.remove(thing)
                        room.roomitemsids = room_inv
                        player.inv = player_inv
                        room.itemdesc = 'You see the following objects in the room : '
                        for r_item in room_inv:
                            room_obj = Item_DB.objects.get(id=r_item)
                            r_room.itemdesc = r_room.itemdesc + f'{room_obj.noun} of {room_obj.skill}, '
                        r_room.itemdesc = r_room.itemdesc[:-2]
                        selected_item = Item_DB.objects.get(id=thing)
                        selected_item.item_room = None
                        selected_item.item_owner = player_id
                        selected_item.save()


    room.save()
    player.save()
    # IMPLEMENT

    return JsonResponse({'pickup':f"you picked up a {selected_item.noun}"}, safe=True, status=500)
