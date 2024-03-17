from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (CreateView, DetailView, DeleteView, 
                                  ListView, TemplateView, UpdateView)
from .models import Leaderboard

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"
    
class LeaderboardCreateView(LoginRequiredMixin, CreateView):
    model = Leaderboard
    fields = ['username', 'final_score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

