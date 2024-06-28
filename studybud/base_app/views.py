from django.shortcuts import render
from django.http import HttpResponse
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