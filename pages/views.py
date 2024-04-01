#from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from reviews.models import UserReviews

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class ReviewList(ListView):
    model = UserReviews
    template_name = 'pages/home.html'
    context_object_name = 'reviews'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = UserReviews.objects.all()
        return context

#def ReviewList(request):
    #reviews = UserReviews.objects.all()
    #context = {'reviews': reviews}
    #return render(request, 'reviews/user_review.html', {'reviews': reviews})

#class ReviewListView(ListView):
 #   model = UserReviews
  #  template_name = 'pages/home.html'
   # context_object_name = 'review_list'

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   context['review_list'] = UserReviews.objects.all()
     #   return context

