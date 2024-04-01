from django.urls import path

from .views import AboutUsView, HomePageView, ReviewList
#from . import view

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('reviews/', ReviewList.as_view(), name='reviews'),
]