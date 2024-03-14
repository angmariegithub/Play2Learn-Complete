from django.urls import reverse_lazy

from django.views.generic import (CreateView, DetailView, DeleteView, 
                                  ListView, TemplateView, UpdateView)
from .models import Leaderboard

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"
    
class LeaderboardCreateView(CreateView):
    model = Leaderboard
    fields = ['username', 'final_score']

class LeaderboardDeleteView(DeleteView):
    model = Leaderboard 

class LeaderboardDetailView(DetailView):
    model = Leaderboard 
    success_url = reverse_lazy('games:list')

class LeaderboardListView(ListView):
    model = Leaderboard

class LeaderboardUpdateView(UpdateView):
    model = Leaderboard
    fields = ['username', 'final_score']

