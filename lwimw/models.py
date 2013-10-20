from django.db import models
from django.db.models import Sum, Avg
from django.contrib.auth.models import *
from util.functions import *
import re
import ipdb

class Contest(models.Model):
    number = models.PositiveIntegerField(unique=True)
    theme = models.CharField(max_length=255)
    start_date = models.DateField()

    class Meta:
        get_latest_by = 'start_date'

    def __unicode__(self):
        return 'Look What I Made Weekend %d - %s (%s)' % (self.number, self.theme, self.start_date)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Submission(models.Model):
    user = models.ForeignKey(User, related_name='submissions')
    contest = models.ForeignKey(Contest, related_name='submissions')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='submissions')
    comments = models.TextField(blank=True)
    link_1 = models.CharField(max_length=255)
    link_2 = models.CharField("Link 2 (Optional)", max_length=255, blank=True)
    link_3 = models.CharField("Link 3 (Optional)", max_length=255, blank=True)
    link_4 = models.CharField("Link 4 (Optional)", max_length=255, blank=True)
    link_5 = models.CharField("Link 5 (Optional)", max_length=255, blank=True)
    receive_ratings = models.BooleanField('Allow others to rate my entry', default=True)

    def calculate_average_ratings(self):
        return {
            'innovation': self.ratings.aggregate(Avg('innovation'))['innovation__avg'] or 0,
            'theme': self.ratings.aggregate(Avg('theme'))['theme__avg'] or 0,
            'refinement': self.ratings.aggregate(Avg('refinement'))['refinement__avg'] or 0,
            'artistry': self.ratings.aggregate(Avg('artistry'))['artistry__avg'] or 0,
            'overall': self.ratings.aggregate(Avg('overall'))['overall__avg'] or 0,
        }


class Rating(models.Model):
    RATINGS = (
        (0, 'N/A'),
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    )
    rater = models.ForeignKey(User, related_name='ratings')
    submission = models.ForeignKey(Submission, related_name='ratings')

    innovation = models.PositiveIntegerField(choices=RATINGS)
    theme = models.PositiveIntegerField(choices=RATINGS)
    refinement = models.PositiveIntegerField(choices=RATINGS)
    artistry = models.PositiveIntegerField(choices=RATINGS)
    overall = models.PositiveIntegerField(choices=RATINGS)
    comments = models.TextField(blank=True)
