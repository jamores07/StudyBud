from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Frontend Development!'},
    {'id': 3, 'name': 'Backend Development!'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
