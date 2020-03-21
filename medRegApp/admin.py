from django.contrib import admin

from .models import Helper, HelpRequest, HelpSeeker, Institution, Qualification, Location, CustomUser

# Register your models here.
admin.site.register(Qualification)
admin.site.register(Helper)
admin.site.register(Institution)
admin.site.register(HelpSeeker)
admin.site.register(HelpRequest)
admin.site.register(Location)
admin.site.register(CustomUser)
