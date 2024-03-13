from django.db import models

class Leaderboard(models.Model):
    username = models.TextField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    game_type = models.TextField(max_length=20)
    game_settings = models.TextField(max_length=20)
    final_score = models.TextField(max_length=10)

    def __str__(self):
        return f"{self.username} - {self.final_score}"
