from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'index.html', None)
    
def loginpage(request):
    return render (request, 'loginmaske.html', None)

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username = email, password = password)
    if user is not None:
        return profilepage(request, profile_id = user.id)
    else:
        return index(request)

def profilepage(request, profile_id):
    users = models.Helper.objects.all().filter(id = profile_id)

    if len(users) == 1:
        context = { 'profile' : users[0], 'user' : None }

        return render(request, 'profile.html', context)
    else:
        return not_found(request)

def settings(request):
    return render(request, 'settings.html', None)

def not_found(request):
    return render(request, 'notfound.html', None)

def startpage(request):
    return render(request, 'startpage.html', None)