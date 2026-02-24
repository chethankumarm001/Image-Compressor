from django.urls import path
from .views import compress_view

urlpatterns = [
    path('', compress_view, name="home"),
]