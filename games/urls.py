from django.urls import path

from .views import (MathFactsView, AnagramHuntView, LeaderboardCreateView, LeaderboardDeleteView,  
                    LeaderboardListView, LeaderboardDetailView, LeaderboardUpdateView)

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('', LeaderboardListView.as_view(), name='list'),
    path('leaderboard/<slug>/delete/', LeaderboardDeleteView.as_view(), name='delete'),
    path('leaderboard/<slug>/', LeaderboardDetailView.as_view(), name='detail'),
    path('leaderboard/<slug>/update/', LeaderboardDetailView.as_view(), name='update'),
    path('leaderboard/create/', LeaderboardDetailView.as_view(), name='create'),
]