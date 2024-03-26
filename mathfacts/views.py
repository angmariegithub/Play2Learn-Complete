from django.views.generic import TemplateView
#from leaderboard.models import Leaderboard
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required  # Import login_required decorator

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

    