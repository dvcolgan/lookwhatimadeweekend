from django.db import models
from django.contrib.auth.models import User
from lwimw.models import *

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    contest = models.ForeignKey(Contest, related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    comments = models.ManyToManyField('PostComment', blank=True, null=True, related_name='comments')
    image = models.ImageField('Image (Optional)', upload_to='post_images', blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.username + "'s post with the title of " + self.title


class PostComment(models.Model):
    author = models.ForeignKey(User, related_name='commenter')
    post = models.ForeignKey(Post, related_name='posts_commented')
    comment_replied = models.ForeignKey("self", related_name='comment_replied_to', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    comment_level = models.PositiveIntegerField(default=12)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.username + "'s comment on the post by " + self.post.author.username + " with the title " + self.post.title