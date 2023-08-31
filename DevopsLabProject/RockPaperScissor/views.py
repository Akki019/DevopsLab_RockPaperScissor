from django.shortcuts import render, HttpResponse, redirect
import gamescore
from form import CHOICES

def index(request):

    if request.method=="POST":
        name=request.POST.get('name')
        rounds=request.POST.get('rounds')
        
        gamescore.newgame(name,rounds)

        return redirect('/input')


    return render(request,'index.html')

def input(request):

    form = CHOICES(request.POST)
    if form.is_valid():
        selected = form.cleaned_data.get("NUMS")
        AI=gamescore.AI()
        winner=gamescore.winner(selected,AI)
        print(winner)
        gamescore.gamescoreupdate(selected,AI,winner)
        return redirect('/page3')

    return render(request, 'input.html', {'form':form})

def page3(request):
    dic=gamescore.getresult()
    return render(request,'page3.html',dic)

