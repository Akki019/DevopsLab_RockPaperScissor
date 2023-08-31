from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')

def input(request):
    return render(request,'input.html')

def page3(request):
    return render(request,'page3.html')

