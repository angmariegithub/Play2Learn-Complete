#from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView
from .models import Leaderboard

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"
    
class LeaderboardDetailView(DetailView):
    model = Leaderboard 

class LeaderboardListView(ListView):
    model = Leaderboard

