from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, HelperCreationForm, LocationCreationForm

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
        return render(request, 'loginmaske.html',
                      {
                          'badLogin': True
                      })

def profilepage(request, profile_id):
    users = models.CustomUser.objects.all().filter(id = profile_id)

    # users = models.Helper.objects.all().filter(id = profile_id)
    if len(users) == 1:
        user = users[0]
        context = { 'user' : user }

        if user.helper.exists():
            return render(request, 'profile.html', context)
        elif user.helpSeeker is not None:
            return render(request, 'search.html', context)
    return not_found(request)

def settings(request):
    return render(request, 'settings.html', None)

def not_found(request):
    return render(request, 'notfound.html', None)

def startpage(request):
    return render(request, 'startpage.html', None)

def register_helper(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        helper_form = HelperCreationForm(request.POST)
        location_form = LocationCreationForm(request.POST)
        if user_creation_form.is_valid() and helper_form.is_valid()\
                and location_form.is_valid():
            user = user_creation_form.save()
            location = location_form.save()
            helper = helper_form.save(commit=False)
            helper.user = user
            helper.location = location
            helper.save()
            return redirect('/')
    else:
        user_creation_form = CustomUserCreationForm()
        helper_form = HelperCreationForm()
        location_form = LocationCreationForm()
    return render(
        request, 'register.html',
        {
            'user_form': user_creation_form,
            'helper_form': helper_form,
            'location_form': location_form
        }
    )
