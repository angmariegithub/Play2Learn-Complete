# Generated by Django 5.0.3 on 2024-03-26 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='user',
        ),
    ]
