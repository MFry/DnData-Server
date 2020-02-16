from django.urls import path
from . import views

urlpatterns = [path("api/players/", views.PlayerListCreate.as_view())]

