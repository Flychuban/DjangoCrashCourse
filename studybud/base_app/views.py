from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn JavaScript'},
]


def home(request):
    rooms = Room.objects.all()
    
    context = {
        'rooms': rooms
    }
    return render(request, 'base_app/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    
    context = {"room": room}
    return render(request, 'base_app/room.html', context)

def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'base_app/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {"form": form}
    return render(request, 'base_app/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    context = {"obj": room}
    return render(request, 'base_app/deleteRoom.html', context)