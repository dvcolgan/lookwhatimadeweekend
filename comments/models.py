from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments')
    reply = models.ForeignKey('self', related_name='parent', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=10000)
    comment_level = models.PositiveIntegerField(default=12)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s: "%s"' % (self.author.username, self.body)
