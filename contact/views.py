from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactUsForm

class ContactUsFormView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact:thanks')

class ContactUsThanksView(TemplateView):
    template_name = 'contact/thanks.html'
