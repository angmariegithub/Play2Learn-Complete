from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '100', 'rows': '5'})
    )