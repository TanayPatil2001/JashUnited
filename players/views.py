from django.shortcuts import render
from .models import hockey
from .forms import hockeyForm
# Create your views here.

def hockey_show(r):
    form = hockeyForm()
    if r.method == 'POST':
        form = hockeyForm(r.POST)
        if form.is_valid():
            form.save()
            #return()

    return render(r,'hockey.html',{'form':form})
