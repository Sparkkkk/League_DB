from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from .models import LeagueDBModel

def index(request):
    return HttpResponse('Reached LeagueDB_app')

def hello(request):
    leagueList = LeagueDBModel.objects.raw('SELECT id, col from "leagueDB_app_leaguedbmodel"')
    template = loader.get_template('leagueDB_app/index.html')
    context = {
        'latest_question_list': leagueList,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'leagueDB_app/index.html')

def page2(request): 
    template = loader.get_template('leagueDB_app/index.html')
    return HttpResponse(template.render(request))
# Create your views here.
