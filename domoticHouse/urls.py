from django.urls.conf import path, include
from domoticHouse import views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewSet)
router.register(r'temperatures', views.TemperatureControlViewSet)

urlpatterns = [
    path("", views.return_jason, name="response"),
    url("rest", include(router.urls)),
    url(r'rest/^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
