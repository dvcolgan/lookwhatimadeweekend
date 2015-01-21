from django.db import models


class UploadedImage(models.Model):
    caption = models.CharField(max_length=255, blank=True)
