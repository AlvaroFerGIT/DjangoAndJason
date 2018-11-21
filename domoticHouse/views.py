from django.shortcuts import render
from domoticHouse.models import Room
from django.http.response import JsonResponse


# Create your views here. Dunno why this fails!

def returnAJSON(request):
    domotic_house_data = Room.objects.all().values("room_name")
    rooms_list =list(domotic_house_data)
    return JsonResponse(rooms_list, safe=False)