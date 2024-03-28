from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from leaderboard.models import Leaderboard
from games.models import Category

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class AnagramLeaderView(LoginRequiredMixin, ListView):
    model = Leaderboard
    ordering = ['-final_score']
    template_name = 'anagrams/anagramleader_list.html'
    context_object_name = 'anagramleader_list'

    def get_queryset(self):
        category_names = ['Anagrams 5', 'Anagrams 6', 'Anagrams 7', 'Anagrams 9']
        category_ids = {}
        for cat_name in category_names:
            category_obj = Category.objects.filter(category=cat_name).first()
            if category_obj:
                category_ids[category_obj.id] = category_obj.id
        return Leaderboard.objects.filter(category_id__in=category_ids.values())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaderboard'] = Leaderboard.objects.all()
        return context
