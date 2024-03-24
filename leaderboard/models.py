from django.conf import settings
from django.db import models
from django.urls import reverse
from games.models import Category

from common.utils.text import unique_slug
    
class Leaderboard(models.Model):
    username = models.TextField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    final_score = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, 
                            null=False, editable=False)

    def get_absolute_url(self):
        return reverse('games:detail', args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.username} - {self.final_score}"
