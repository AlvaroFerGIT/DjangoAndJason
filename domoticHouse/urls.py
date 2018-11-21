from django.urls.conf import path
from domoticHouse import views


urlpatterns = [
    path("",views.JsonResponse,name="response"),
]
