from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/<int:profile_id>', views.profilepage, name='profile-page')
]
