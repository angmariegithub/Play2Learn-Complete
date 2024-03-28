from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from leaderboard.models import Leaderboard
from games.models import Category

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class MathLeaderView(LoginRequiredMixin, ListView):
    model = Leaderboard
    ordering = ['-final_score']
    template_name = 'mathfacts/mathleader_list.html'
    context_object_name = 'mathleader_list'

    def get_queryset(self):
        category_names = ['Math +', 'Math -', 'Math /', 'Math x']
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