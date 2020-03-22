from django.conf import settings as django_settings
from django.contrib.auth import login
from django.http import Http404, HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render, reverse
from django.views.generic import DetailView, ListView

from .forms import (CustomUserCreationForm, HelperCreationForm,
                    HelpRequestCreationForm, HelpSeekerCreationForm,
                    InstitutionCreationForm, LocationCreationForm)
from .models import CustomUser, Helper, HelpRequest, Institution
from .utils import send_invite_mail
# Create your views here.


def index(request):
    return render(request, 'index.html', None)


def profilepage(request, profile_id):
    user = None
    try:
        user = CustomUser.objects.get(pk=profile_id)
        user_login = request.user
        if user.id == user_login.id:
            login = True
        else:
            login = False
    except CustomUser.DoesNotExist:
        raise Http404('Nutzer existiert nicht')
    else:
        context = {'object': user, 'login': login}
        if user.is_helper:
            return render(request, 'profile_helper.html', context)
        elif user.is_help_seeker:
            return render(request, 'profile_helpseeker.html', context)


def settings(request):
    return render(request, 'settings.html', None)


def register(request):
    return render(request, 'register-selection.html', None)


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
            helper_form.save_m2m()
            login(request, user)
            return redirect('/')
    else:
        user_creation_form = CustomUserCreationForm()
        helper_form = HelperCreationForm()
        location_form = LocationCreationForm()
    return render(
        request, 'register.html',
        {
            'forms': [
                user_creation_form,
                helper_form,
                location_form,
            ],
            'action': 'register_helper',
            'caption': 'Registrierung für Helfer',
            'stylesheets': [
                '/static/stylesheet-register.css'
            ]
        }
    )


def register_help_seeker(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        help_seeker_creation_form = HelpSeekerCreationForm(request.POST)
        if user_creation_form.is_valid() \
                and help_seeker_creation_form.is_valid():
            user = user_creation_form.save()
            help_seeker = help_seeker_creation_form.save(commit=False)
            help_seeker.user = user
            help_seeker.save()
            login(request, user)
            return redirect('/')
    else:
        user_creation_form = CustomUserCreationForm()
    return render(
        request, 'register.html',
        {
            'forms': [
                user_creation_form
            ],
            'action': 'register_help_seeker',
            'caption': 'Registrierung für Hilfesuchende',
            'stylesheets': [
                '/static/stylesheet-register.css'
            ]
        }
    )


def create_institution(request):
    if request.method == 'POST':
        location_form = LocationCreationForm(request.POST)
        institution_creation_form = InstitutionCreationForm(request.POST)
        if location_form.is_valid() and institution_creation_form.is_valid():
            institution = institution_creation_form.save(commit=False)
            location = location_form.save()
            institution.location = location
            institution.save()
            return redirect(
                reverse('institution_detail', args=(institution.id,))
            )
    else:
        location_form = LocationCreationForm()
        institution_creation_form = InstitutionCreationForm()
    return render(request, 'register.html', {
        'forms': [
            institution_creation_form,
            location_form,
        ],
        'action': 'create_institution',
        'caption': 'Erstellung einer Institution',
        'stylesheets': [
            '/static/stylesheet-register.css'
        ]
    })


def create_help_request(request):
    if request.user.is_authenticated:
        if not request.user.is_help_seeker:
            return HttpResponse('You can\'t do this as a helper')
    else:
        return redirect('%s?next=%s' % (reverse('login'), request.path))
    if request.method == 'POST':
        location_form = LocationCreationForm(request.POST)
        help_request_creation_form = HelpRequestCreationForm(request.POST)
        if location_form.is_valid() and help_request_creation_form.is_valid():
            help_request = help_request_creation_form.save(commit=False)
            location = location_form.save()
            help_request.location = location
            help_request.help_seeker = request.user.helpseeker
            help_request.save()
            return redirect(
                reverse('help_request_detail', args=(help_request.id,))
            )
    else:
        location_form = LocationCreationForm()
        help_request_creation_form = HelpRequestCreationForm()
    return render(request, 'register.html', {
        'forms': [
            help_request_creation_form,
            location_form,
        ],
        'action': 'create_help_request',
        'caption': 'Ein Hilfegesuch erstellen',
        'stylesheets': [
            '/static/stylesheet-register.css'
        ]
    })


def add_helper(request):
    try:
        help_request = HelpRequest.objects.get(
            pk=request.POST.get('help_request')
        )
    except HelpRequest.DoesNotExist:
        raise Http404('Couldn\'t find help request')
    else:
        # find selected helpers
        helpers = []
        for key in request.POST.keys():
            if not key.startswith('helper-'):
                continue
            helper_id = key.replace('helper-', '')
            try:
                helper = Helper.objects.get(pk=helper_id)
            except Helper.DoesNotExist:
                pass
            else:
                help_request.helpers.add(helper)
                helpers.append(helper)
        if django_settings.EMAIL:
            send_invite_mail(help_request, helpers)
        return redirect(
            reverse('help_request_detail', args=(help_request.id,))
        )


class InstitutionDetailView(DetailView):
    model = Institution


class HelpRequestDetailView(DetailView):
    model = HelpRequest


class HelperListView(ListView):
    model = Helper

    def get_help_request(self):
        try:
            help_request_id = self.request.GET.get('from_hr')
            help_request = HelpRequest.objects.get(pk=help_request_id)
        except HelpRequest.DoesNotExist:
            return None
        else:
            return help_request

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        help_request = self.get_help_request()
        if help_request:
            context['help_request'] = help_request
        return context

    def get_queryset(self):
        help_request = self.get_help_request()
        if help_request:
            return Helper.objects.filter(is_available=True)\
                .exclude(helprequest__in=[help_request])
        else:
            return Helper.objects.filter(is_available=True)


class HelpRequestListView(ListView):
    model = HelpRequest

    def get_queryset(self):
        if not self.request.user.is_help_seeker:
            return HelpRequest.objects.none()
        return HelpRequest.objects.filter(
            help_seeker=self.request.user.helpseeker
        )
