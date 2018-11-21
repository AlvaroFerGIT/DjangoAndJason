from django.shortcuts import render
from domoticHouse.models import Room, TemperatureControl
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import viewsets
from domoticHouse.serializers import RoomSerializer,\
    TemperatureControlSerializer


# Create your views here. 

"""By JsonResponse, got a problem using this, the thing it returns the id on the objects 
(because is using a Relational Model!) so it return the json only with the ID as value, when it needs all the damm Object
    
def return_jason(request):
    domotic_house_data = Room.objects.all().values()
    
    return JsonResponse(list(domotic_house_data), safe=False)
    
"""

"""By HttpResponse using serializiers, same problem
   
def return_jason(request):  
    data = serializers.serialize("json", Room.objects.all())
    return HttpResponse(data, content_type="application/json")
   
"""

def return_jason(request):
    domotic_house_data = Room.objects.all().values()
    
    return JsonResponse(list(domotic_house_data), safe=False)


class RoomViewSet (viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class TemperatureControlViewSet(viewsets.ModelViewSet):
    queryset = TemperatureControl.objects.all()
    serializer_class = TemperatureControlSerializer