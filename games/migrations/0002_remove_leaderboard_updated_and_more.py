# Generated by Django 4.0.5 on 2024-03-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='updated',
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='final_score',
            field=models.TextField(max_length=10),
        ),
    ]