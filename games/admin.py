from django.contrib import admin


from .models import Leaderboard, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    model = Leaderboard
    list_display = ['username', 'final_score', 'category', 'time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'time')

        return ()
