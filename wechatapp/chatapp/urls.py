from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.my_view),
    path("<str:slug>/",views.room)

]
