from django.shortcuts import render
from django.http import HttpResponse
from .models import Rooms

# Create your views here.

def home(request):
    rooms = Rooms.objects.all()#gets all rooms from the database
    return render(request, 'baseapp/index.html')
def login(request, user):
    return render(request, 'baseapp/index.html')

def register(request):
    return render(request, 'baseapp/signup.html')
