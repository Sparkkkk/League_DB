from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

def index(request):
    return HttpResponse('Reached LeagueDB_app')

def hello(request):
    return render(request, 'leagueDB_app/index.html')
# Create your views here.
