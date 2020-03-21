from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/<int:profile_id>', views.profilepage, name='profile-page'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('settings', views.settings, name='settings'),
    path('login', views.login, name='login'),
    path('startpage',views.startpage,name='startpage'),
    path('register/helper', views.register_helper, name='register_helper'),
    path('register/helpseeker', views.register_help_seeker, name='register_help_seeker'),
    path('institutions/create', views.create_institution, name='create_institution'),
    path('institutions/<int:pk>/', views.InstitutionDetailView.as_view(), name='institution_detail'), 
    path('helprequest/<int:pk>', views.HelpRequestDetailView.as_view(), name='help_request_detail'),
    path('results', views.results, name='results')
]
