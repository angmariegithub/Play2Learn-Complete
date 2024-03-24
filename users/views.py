from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (UpdateView, ListView)
from django.shortcuts import get_object_or_404


from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm
from leaderboard.models import Leaderboard

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my-account')

class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
    
class MyGamesPageView(LoginRequiredMixin, ListView):
    model = Leaderboard
    ordering = ['-final_score']
    template_name = 'users/mygamespage_list.html'
    context_object_name = 'mygamespage_list'

    def get_queryset(self):
        #queryset = super().get_queryset()
        return Leaderboard.objects.filter(username=self.request.user.username)
        #queryset = queryset.filter(username=self.request.user.username)
        #return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaderboard'] = Leaderboard.objects.all()
        return context
    
