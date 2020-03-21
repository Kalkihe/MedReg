from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def index(request):
    return render(request, 'index.html', None)
    
def loginpage(request):
    return render (request, 'loginmaske.html', None)

def profilepage(request, profile_id):
    user = models.CustomUser.objects.all().filter(id = profile_id)

    context = { 'user' : user }

    return render(request, 'profile.html', context)

def settings(request):
    return render(request, 'settings.html', None)
