from django.urls import path
from . import views #from the current folder import the views module


urlpatterns = [
    path("", views.home_view),
    path("home/", views.home_view),
]
