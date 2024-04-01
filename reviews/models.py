from django.conf import settings
from django.db import models
from django.urls import reverse
from leaderboard.models import Leaderboard

from common.utils.text import unique_slug
    
class UserReviews(models.Model):
    user_review = models.TextField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[str(self.pk)])
        
    def __str__(self):
        return f"{self.user} - {self.user_review}"
