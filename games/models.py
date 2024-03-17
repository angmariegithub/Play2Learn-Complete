from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('games:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Categories'
        
    
class Leaderboard(models.Model):
    username = models.TextField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    #game_type = models.TextField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #game_settings = models.TextField(max_length=20)
    final_score = models.TextField(max_length=10)
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


