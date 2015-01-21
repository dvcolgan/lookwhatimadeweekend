from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    contest = models.ForeignKey('contests.Contest', related_name='posts')
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=10000)
    image = models.ImageField('Image (Optional)', upload_to='post_images', blank=True, null=True)
    images = models.ManyToManyField('uploadedimages.UploadedImage', related_name='posts')
    comments = models.ManyToManyField('comments.Comment', related_name='posts')
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s by %s" % (self.title, self.author.username)
