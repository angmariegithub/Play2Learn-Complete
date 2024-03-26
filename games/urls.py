from django.urls import path

from .views import (SaveData)

app_name = 'games'
urlpatterns = [
    path('save_data/', SaveData, name='save_data'),
]
