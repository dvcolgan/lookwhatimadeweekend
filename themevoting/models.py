from django.db import models
from django.contrib.auth.models import User
from lwimw.models import Contest


class Theme(models.Model):
    contest = models.ForeignKey(Contest, related_name='potential_themes')
    submitted_by = models.ForeignKey(User, related_name='themes_submitted')
    name = models.CharField(max_length=255)


class ThemeBump(models.Model):
    DIRECTION_CHOICES = (
        ('up', 'Up'),
        ('down', 'Down'),
    )
    theme = models.ForeignKey(Theme, related_name='bumps')
    user = models.ForeignKey(User, related_name='bumps')
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='theme_votes')
    theme = models.ForeignKey(Theme, related_name='votes')
    rating = models.IntegerField()
