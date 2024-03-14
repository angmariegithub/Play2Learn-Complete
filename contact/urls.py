from django.urls import path

from .views import ContactUsFormView, ContactUsThanksView

app_name = 'contact'
urlpatterns = [
    path('contact/', ContactUsFormView.as_view(), name='contact'),
    path('contact/thanks/', ContactUsThanksView.as_view(), name='thanks'),
]

