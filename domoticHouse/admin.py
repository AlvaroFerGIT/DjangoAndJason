from django.contrib import admin
from domoticHouse.models import Room, TemperatureControl, AutomatedWindows

# Register your models here.

admin.site.register(Room)
admin.site.register(TemperatureControl)
admin.site.register(AutomatedWindows)