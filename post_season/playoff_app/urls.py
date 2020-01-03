from django.urls import path
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('leaderboard/', views.Leaderboard, name='leaderboard'),
    path('ladder/', views.Ladder, name='ladder'),
    path('playoff_teams/', views.Playoff_TeamListView.as_view(), name='playoff_teams'),
    path('wildcard/', views.WildCard, name='wildcard'),
    path('division/', views.Division, name='division'),
    path('conference/', views.Conference, name='conference'),
    path('superbowl/', views.Superbowl, name='superbowl'),
]
