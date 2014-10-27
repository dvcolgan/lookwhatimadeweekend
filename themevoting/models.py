from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from lwimw.models import Contest


class ThemeManager(models.Manager):
    def get_remaining_themes(self, contest):
        """
        Return a list of themes for a contest, excluding items which were
        bumped down more than up.
        """

        # TODO: try to find a nicer way to tally bumps

        themes = self.filter(contest=contest)
        for theme in self.filter(contest=contest).select_related('bumps__direction'):
            bump_ups = ThemeBump.objects.filter(theme=theme, direction="up").count()
            bump_downs = ThemeBump.objects.filter(theme=theme, direction="down").count()
            if bump_downs > bump_ups:
                themes.exclude(pk=theme.pk)
        return themes


class Theme(models.Model):
    contest = models.ForeignKey(Contest, related_name='potential_themes')
    submitted_by = models.ForeignKey(User, related_name='themes_submitted')
    name = models.CharField(max_length=255)

    objects = ThemeManager()

    def __unicode__(self):
        return self.name


class ThemeBump(models.Model):
    DIRECTION_CHOICES = (
        ('up', 'Up'),
        ('down', 'Down'),
    )
    theme = models.ForeignKey(Theme, related_name='bumps')
    user = models.ForeignKey(User, related_name='bumps')
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)

    def __unicode__(self):
        return "%s (%s)" % (theme, direction)


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='theme_votes')
    theme = models.ForeignKey(Theme, related_name='votes')
    rating = models.IntegerField()

    def __unicode__(self):
        return "%s (%s)" % (theme, rating)
