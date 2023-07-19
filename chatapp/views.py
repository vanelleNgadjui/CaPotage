from django.shortcuts import render
from .models import Room,Message
from django.contrib.auth.decorators import login_required

@login_required
def rooms(request):
    rooms = Room.objects.filter(participants=request.user)
    return render(request, "chats/rooms.html", {"rooms": rooms})
    
@login_required
def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "chats/room.html",{"room_name":room_name,"slug":slug,'messages':messages})