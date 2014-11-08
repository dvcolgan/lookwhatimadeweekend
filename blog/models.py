from django.db import models
from django.contrib.auth.models import User
from contests.models import Contest


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    contest = models.ForeignKey(Contest, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=10000)
    image = models.ImageField('Image (Optional)', upload_to='post_images', blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s's post with the title of %s" % (self.author.username, self.title)


class PostComment(models.Model):
    author = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    reply = models.ForeignKey('self', related_name='parent', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=10000)
    comment_level = models.PositiveIntegerField(default=12)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s's comment on the post by %s with the title %s" % (self.author.username, self.post.author.username, self.post.title)
