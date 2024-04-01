from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReviewForm
from .models import UserReviews

class ReviewDetailView(DetailView):
    model = UserReviews

class ReviewListView(ListView):
    model = UserReviews
    ordering = ['-created']
    template_name = 'pages/home.html'
    #template_name = 'reviews/userReviews_list.html'
    #template_name = 'pages/home.html'
    #context_object_name = 'reviews_list'

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['userReviews'] = UserReviews.objects.all()
    #    return context

class ReviewView(FormView, LoginRequiredMixin, CreateView):
    model = UserReviews
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'




    
