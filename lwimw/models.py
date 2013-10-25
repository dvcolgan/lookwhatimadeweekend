from django.db import models
from django.db.models import Sum, Avg
from django.contrib.auth.models import *
from django.utils import timezone
from util.functions import *
import re
import ipdb
from datetime import date, timedelta



class ContestManager(models.Manager):
    def get_current_contest_state(self):
        contest = self.latest()
        now = timezone.now()
        print now, contest.start_time
        if now < contest.start_time:
            return 'before'
        elif contest.start_time <= now <= contest.get_end_time():
            return 'during'
        elif contest.get_end_time() < now <= contest.get_submission_time():
            return 'submission'
        elif contest.get_submission_time() < now <= contest.get_judging_time():
            return 'judging'
        else:
            return 'after'


class Contest(models.Model):
    number = models.PositiveIntegerField(unique=True)
    theme = models.CharField(max_length=255)
    start_time = models.DateTimeField()

    objects = ContestManager()

    class Meta:
        get_latest_by = 'start_time'

    def __unicode__(self):
        return 'Look What I Made Weekend %d - %s (%s)' % (self.number, self.theme, self.start_time)

    def get_end_time(self):
        return self.start_time + timedelta(hours=48)

    def get_submission_time(self):
        return self.start_time + timedelta(hours=49)

    def get_judging_time(self):
        return self.start_time + timedelta(hours=48+14*24)
        

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
    link_1 = models.CharField("Link 1 (Optional)", max_length=255, blank=True, null=True)
    link_2 = models.CharField("Link 2 (Optional)", max_length=255, blank=True, null=True)
    link_3 = models.CharField("Link 3 (Optional)", max_length=255, blank=True, null=True)
    image_1 = models.ImageField("Image 1 (Optional)", upload_to='submission_images', blank=True, null=True)
    image_2 = models.ImageField("Image 2 (Optional)", upload_to='submission_images', blank=True, null=True)
    image_3 = models.ImageField("Image 3 (Optional)", upload_to='submission_images', blank=True, null=True)
    receive_ratings = models.BooleanField('Allow others to rate my entry', default=True)
    used_theme = models.BooleanField('I used the theme', default=True)

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
        (0, 'Not Applicable'),
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


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    contest = models.ForeignKey(Contest, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField('Image (Optional)', upload_to='post_images', blank=True, null=True)

