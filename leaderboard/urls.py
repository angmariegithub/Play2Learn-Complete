from django.urls import path

from .views import (LeaderboardDeleteView,  
                    LeaderboardListView, LeaderboardDetailView)

app_name = 'leaderboard'
urlpatterns = [
    path('', LeaderboardListView.as_view(), name='list'),
    path('leaderboard/<slug>/delete/', LeaderboardDeleteView.as_view(), name='delete'),
    path('leaderboard/<slug>/', LeaderboardDetailView.as_view(), name='detail'),
    path('leaderboard/<slug>/update/', LeaderboardDetailView.as_view(), name='update'),
    path('leaderboard/create/', LeaderboardDetailView.as_view(), name='create'),
    path('user/<username>/', LeaderboardListView.as_view(), name='user'),
]