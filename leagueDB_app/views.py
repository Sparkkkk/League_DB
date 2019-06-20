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


# Those None need to be replaced by SQL
def page2(request):
    # for page 2 username is the parameter passed from URL
    username = request.content_params.get('username')
    top5_champions = LeagueDBModel.objects.raw('SELECT cid AS id, name FROM "leagueDB_app_champion"')

    matches = LeagueDBModel.objects.raw('SELECT name from "leagueDB_app_champion"')

    context = {
        'top5': top5_champions,
        'matches': matches
    }
    template = loader.get_template('leagueDB_app/page2.html')
    return HttpResponse(template.render(context, request))


def page3(request):

    champions_name = LeagueDBModel.objects.raw('SELECT cid AS id, name FROM "leagueDB_app_champion"')
    winrate_with_champion_name = None
    context = {
        'champ_name': champions_name,
        'winrate': winrate_with_champion_name
    }
    template = loader.get_template('leagueDB_app/page3.html')
    return HttpResponse(template.render(context, request))


def page4(request):
    # for page 4, champion name is the parameter passed from URL
    champion_name = request.content_params.get('champion_name')
    top5_player = None
    recommond_items = None
    context = {
        'top5': top5_player,
        'recom': recommond_items
    }

    template = loader.get_template('leagueDB_app/page4.html')
    return HttpResponse(template.render(context, request))

# Create your views here.
