from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ReviewForm

class ReviewView(FormView):
    template_name = 'reviews/user_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:thanks')

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'
