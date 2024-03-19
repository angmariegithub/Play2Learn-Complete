from django.urls import path

from .views import ReviewView, ReviewThanksView

app_name = 'reviews'
urlpatterns = [
    path('reviews/', ReviewView.as_view(), name='app'),
    path('reviews/thanks/', ReviewThanksView.as_view(), name='thanks'),
]