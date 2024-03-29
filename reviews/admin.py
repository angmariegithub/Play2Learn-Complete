from django.contrib import admin

from .models import UserReviews

@admin.register(UserReviews)
class UserReviewsAdmin(admin.ModelAdmin):
    model = UserReviews
    list_display = ['user', 'user_review', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')

        return ()
