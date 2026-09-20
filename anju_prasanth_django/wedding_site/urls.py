from django.urls import path
from wedding.views import home

urlpatterns = [
    path("", home, name="home"),
]
