from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReviewForm
from .models import UserReviews

class ReviewDetailView(DetailView):
    model = UserReviews

class ReviewView(FormView, LoginRequiredMixin, CreateView):
    model = UserReviews
    form_class = ReviewForm
    #template_name = 'reviews/user_review.html'
    #form_class = ReviewForm
    #success_url = reverse_lazy('reviews:thanks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'

