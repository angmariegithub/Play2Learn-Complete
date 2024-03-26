from django.urls import path

from .views import (MathFactsView)

urlpatterns = [
    path('', MathFactsView.as_view(), name='math-facts'),
]



