from django.contrib import admin
from django.urls import path
from RockPaperScissor import views

urlpatterns = [
    path('',views.index,name='Index'),
]