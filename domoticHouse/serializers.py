'''
Created on 21 nov. 2018

@author: A735843
'''

from rest_framework import serializers
from domoticHouse.models import Room, TemperatureControl

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ("room_name","temperature")
        
class TemperatureControlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= TemperatureControl
        fields = ("temperature","humidity")