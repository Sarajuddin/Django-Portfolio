from django.urls import path
from kirtiapp import views

urlpatterns = [
    path('', views.index),
]
