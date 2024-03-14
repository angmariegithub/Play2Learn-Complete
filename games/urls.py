from django.urls import path

from .views import MathFactsView, AnagramHuntView, LeaderboardListView, LeaderboardDetailView

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('', LeaderboardListView.as_view(), name='list'),
    path('leaderboard/<slug>/', LeaderboardDetailView.as_view(), name='detail'),
]