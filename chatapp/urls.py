from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:slug>/", views.room, name="room"),
]
