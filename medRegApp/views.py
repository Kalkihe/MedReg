from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html', None)
    
def loginpage(request):
    return render (request, 'loginmaske.html', None)

def profilepage(request, profile_id):
    context = { 'profile_id' : profile_id }
    return render(request, 'profile.html', context)

