from django.forms import ModelForm, Textarea
from .models import UserReviews

class ReviewForm(ModelForm):
    class Meta:
        model = UserReviews
        fields = ['user_review']
        widgets = {
            'user_review': Textarea(
                attrs={'cols': 50, 'rows': 9, 'autofocus': True}
            ),
        }
        help_texts = {
            'user_review': 'Type your comments'
        }

