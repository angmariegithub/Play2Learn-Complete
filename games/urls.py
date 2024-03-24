from django.urls import path

from .views import (MathFactsView, AnagramHuntView, LeaderboardDeleteView,  
                    LeaderboardListView, LeaderboardDetailView)

app_name = 'games'
urlpatterns = [
    path('', LeaderboardListView.as_view(), name='list'),
    path('leaderboard/<slug>/delete/', LeaderboardDeleteView.as_view(), name='delete'),
    path('leaderboard/<slug>/', LeaderboardDetailView.as_view(), name='detail'),
    path('leaderboard/<slug>/update/', LeaderboardDetailView.as_view(), name='update'),
    path('leaderboard/create/', LeaderboardDetailView.as_view(), name='create'),
    path('user/<username>/', LeaderboardListView.as_view(), name='user'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
]