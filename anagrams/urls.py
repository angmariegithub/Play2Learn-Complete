from django.urls import path

from .views import (AnagramHuntView)

urlpatterns = [
    path('', AnagramHuntView.as_view(), name='anagram-hunt'),
]