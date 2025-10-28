"""URL confiuration for health app"""

from django.urls import path

from . import views

app_name = "health"
urlpatterns = [
    path("ping/", views.ping, name="ping"),
]
