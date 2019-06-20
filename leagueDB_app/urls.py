from django.urls import path

from . import views

app_name = 'leaguedb_app'

urlpatterns = [
    # /leaguedb_app
    path('', views.index, name='index'),
    # leaguedb_app/hello
    path('page1', views.hello, name='page1'),
    # leaguedb_app/hello/
    path(r'page1/(a-z)*', views.page2, name='page2'),

    path('randomQuery', views.randomQuery, name='randomQuery'),
]
