from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn JavaScript'},
]


def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base_app/home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            break
    
    context = {"room": room}
    return render(request, 'base_app/room.html', context)