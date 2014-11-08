from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from util import datetime_


class ContestManager(models.Manager):
    def get_current(self):
        contests = self.model.objects.order_by('-number')
        if contests.exists():
            return contests[0]
        else:
            return None


class Contest(models.Model):
    number = models.PositiveIntegerField(unique=True)
    theme = models.CharField(max_length=255, blank=True)
    start = models.DateTimeField()

    objects = ContestManager()

    def __unicode__(self):
        return 'Look What I Made Weekend %d - %s' % (self.number, self.theme)

    @property
    def state(self):
        now = datetime_.now_()
        if now < self.start:
            return 'before'
        elif now < self.start + relativedelta(hours=48):
            return 'during'
        elif now < self.start + relativedelta(hours=49):
            return 'submitting'
        elif now < self.start + relativedelta(hours=48, weeks=2):
            return 'judging'
        else:
            return 'after'

    @property
    def theme_voting_state(self):
        now = datetime_.now_()
        if now < self.start and now > self.start - relativedelta(hours=24):
            return 'voting'
        else:
            return 'suggesting'

    @property
    def end_time(self):
        return self.start + timedelta(hours=48)

    @property
    def submission_time(self):
        return self.start + timedelta(hours=49)

    @property
    def judging_time(self):
        return self.start + timedelta(hours=48 + 14 * 24)

    @property
    def can_submit(self):
        return self.state == 'during' or self.state == 'submitting'

    def get_results(self):
        return (
            self.submissions.all().
            annotate(avg_innovation=Avg('ratings__innovation')).
            annotate(avg_refinement=Avg('ratings__refinement')).
            annotate(avg_artistry=Avg('ratings__artistry')).
            annotate(avg_overall=Avg('ratings__overall')).
            order_by('-avg_overall')
        )


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

    def __unicode__(self):
        return self.title


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
    refinement = models.PositiveIntegerField(choices=RATINGS)
    artistry = models.PositiveIntegerField(choices=RATINGS)
    overall = models.PositiveIntegerField(choices=RATINGS)
    comments = models.TextField()

    def __unicode__(self):
        return self.submission
