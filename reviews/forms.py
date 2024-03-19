from django import forms

class ReviewForm(forms.Form):
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '50', 'rows': '9', 'placeholder': 'Type your review'})
    )
