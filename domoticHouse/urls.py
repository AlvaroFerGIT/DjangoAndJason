from django.urls.conf import path
from domoticHouse import views


urlpatterns = [
    path("", views.returnAJSON, name="response"),
]
