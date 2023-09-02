from django.contrib import admin
from django.urls import path
from RockPaperScissor import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('input',views.input,name='Input'),
    path('page3',views.page3,name='page3'),
    path('result',views.result,name='result'),
    path('nextround',views.nextround,name='nextround'),
]