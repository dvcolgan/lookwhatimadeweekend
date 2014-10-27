from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from lwimw.models import Contest


class ThemeManager(models.Manager):
    def get_top_theme(self, contest):
        """
        Returns the currently winning theme for a particular contest.
        """
        return self.filter(contest=contest).annotate(rating=Avg('votes__rating')).order_by('-rating')[0]

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
        return "%s (%s)" % (self.theme, self.direction)


class VoteManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except:
            return None

    def get_votes(self, contest, user):
        """
        Generates a vote for this user, for each remaining theme in this
        contest. It then returns a query for all the touched votes.
        """
        # Loop over all themes that have not been eliminated, generating a null
        # vote for each.
        themes = Theme.objects.get_remaining_themes(contest)
        for theme in themes:
            vote = Vote(user=user, theme=theme, rating=0)
            vote.save(overwrite=False)

        # Return all votes by this user for this contest. There should be one
        # for each remaining theme.
        return self.filter(theme__contest=contest, user=user)


class Vote(models.Model):
    user = models.ForeignKey(User, related_name='theme_votes')
    theme = models.ForeignKey(Theme, related_name='votes')
    rating = models.IntegerField()

    objects = VoteManager()

    class Meta:
        ordering = ['-rating', ]

    def save(self, overwrite=True):
        # TODO:
        # Find a better solution. This one's pretty damn slow.

        # Check to see if this user has already voted on this theme.
        # If they have, then just update the old vote with the new rating.
        # Otherwise, save this new vote object. This ensures that the same
        # person can't vote for the same theme more than once, and that
        # their most recent vote will count.
        vote = Vote.objects.get_or_none(user=self.user, theme=self.theme)
        if vote is None:
            super(Vote, self).save()
        elif overwrite:
            vote.rating = self.rating
            vote.save()

    def __unicode__(self):
        return "%s (%s)" % (self.theme, self.rating)
