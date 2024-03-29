from django.urls import path

from .views import ReviewView, ReviewThanksView, ReviewDetailView

app_name = 'reviews'
urlpatterns = [
    path('reviews/create', ReviewView.as_view(), name='create'),
    path('reviews/thanks/', ReviewThanksView.as_view(), name='thanks'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='detail'),
]