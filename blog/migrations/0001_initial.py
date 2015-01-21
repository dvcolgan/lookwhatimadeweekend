# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '__first__'),
        ('uploadedimages', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to=b'post_images', null=True, verbose_name=b'Image (Optional)', blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(related_name='posts', to='comments.Comment')),
                ('contest', models.ForeignKey(related_name='posts', to='contests.Contest')),
                ('images', models.ManyToManyField(related_name='posts', to='uploadedimages.UploadedImage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
