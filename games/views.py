#from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Leaderboard

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class LeaderboardListView(ListView):
    model = Leaderboard