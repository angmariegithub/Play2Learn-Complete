from django.urls import path

from .views import (MathFactsView, MathLeaderView)

urlpatterns = [
    path('', MathFactsView.as_view(), name='math-facts'),
    path('leader/', MathLeaderView.as_view(), name='math-leader'),
]



