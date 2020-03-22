from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/<int:profile_id>', views.profilepage, name='view_profile'),
    path('settings', views.settings, name='settings'),
    path('register/helper', views.register_helper, name='register_helper'),
    path('register/helpseeker', views.register_help_seeker,
         name='register_help_seeker'),
    path('institutions/create', views.create_institution,
         name='create_institution'),
    path('institutions/<int:pk>/', views.InstitutionDetailView.as_view(),
         name='institution_detail'),
    path('helprequests/<int:pk>', views.HelpRequestDetailView.as_view(),
         name='help_request_detail'),
    path('users/', include('django.contrib.auth.urls')),
    path('helprequests/create', views.create_help_request,
         name='create_help_request'),
    path('helprequests/', views.HelpRequestListView.as_view(),
         name='help_request_list'),
    path('helpers/', views.HelperListView.as_view(),
         name='helper_list'),
    path('register', views.register, name="register-selection")
]
