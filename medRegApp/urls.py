from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/<int:profile_id>', views.profilepage, name='profile-page'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login')
]
