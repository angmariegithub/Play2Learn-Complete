from django.contrib import admin

from .models import Leaderboard

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    model = Leaderboard
    list_display = ['username', 'final_score', 'category', 'time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'time')

        return ()