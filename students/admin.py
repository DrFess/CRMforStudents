from django.contrib import admin
from .models import Profile, Group, Geolocation

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Geolocation)
