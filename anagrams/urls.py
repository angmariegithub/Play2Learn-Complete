from django.urls import path

from .views import (AnagramHuntView, AnagramLeaderView)

urlpatterns = [
    path('', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('leader/', AnagramLeaderView.as_view(), name='anagram-leader'),
]