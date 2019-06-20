from django.urls import path

from . import views

app_name = 'leaguedb_app'

urlpatterns = [
    # /leaguedb_app
    path('', views.index, name='index'),
    # leaguedb_app/hello
    path('page1', views.hello, name='page1'),
    # leaguedb_app/hello/
# <<<<<<< HEAD
#     path(r'page1/(a-z)*', views.page2, name='page2'),
#
#     path('randomQuery', views.randomQuery, name='randomQuery'),
# =======
    # path(r'page1/(a-z)*', views.page2, name='page2'),

    # testing page for page2
    path('page2', views.page2, name='page2'),

    # testing page for page2
    path('page3', views.page3, name='page3'),

    # testing page for page2
    path('page4', views.page4, name='page4'),

]
