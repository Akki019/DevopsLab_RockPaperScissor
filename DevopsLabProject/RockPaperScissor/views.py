from django.shortcuts import render, HttpResponse, redirect
import gamescore

def index(request):

    if request.method=="POST":
        name=request.POST.get('name')
        rounds=request.POST.get('rounds')
        
        gamescore.newgame(name,rounds)

        return redirect('/input')


    return render(request,'index.html')

def input(request):
    return render(request,'input.html')

def page3(request):
    return render(request,'page3.html')

