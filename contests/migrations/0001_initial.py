# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploadedimages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(unique=True)),
                ('theme', models.CharField(max_length=255, blank=True)),
                ('start', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('innovation', models.PositiveIntegerField(choices=[(0, b'Not Applicable'), (1, b'One Star'), (2, b'Two Stars'), (3, b'Three Stars'), (4, b'Four Stars'), (5, b'Five Stars')])),
                ('refinement', models.PositiveIntegerField(choices=[(0, b'Not Applicable'), (1, b'One Star'), (2, b'Two Stars'), (3, b'Three Stars'), (4, b'Four Stars'), (5, b'Five Stars')])),
                ('artistry', models.PositiveIntegerField(choices=[(0, b'Not Applicable'), (1, b'One Star'), (2, b'Two Stars'), (3, b'Three Stars'), (4, b'Four Stars'), (5, b'Five Stars')])),
                ('overall', models.PositiveIntegerField(choices=[(0, b'Not Applicable'), (1, b'One Star'), (2, b'Two Stars'), (3, b'Three Stars'), (4, b'Four Stars'), (5, b'Five Stars')])),
                ('comments', models.TextField()),
                ('rater', models.ForeignKey(related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('link_1', models.CharField(max_length=255, null=True, verbose_name=b'Link 1 (Optional)', blank=True)),
                ('link_2', models.CharField(max_length=255, null=True, verbose_name=b'Link 2 (Optional)', blank=True)),
                ('link_3', models.CharField(max_length=255, null=True, verbose_name=b'Link 3 (Optional)', blank=True)),
                ('image_1', models.ImageField(upload_to=b'submission_images', null=True, verbose_name=b'Image 1 (Optional)', blank=True)),
                ('image_2', models.ImageField(upload_to=b'submission_images', null=True, verbose_name=b'Image 2 (Optional)', blank=True)),
                ('image_3', models.ImageField(upload_to=b'submission_images', null=True, verbose_name=b'Image 3 (Optional)', blank=True)),
                ('receive_ratings', models.BooleanField(default=True, verbose_name=b'Allow others to rate my entry')),
                ('category', models.ForeignKey(related_name='submissions', to='contests.Category')),
                ('comments', models.ManyToManyField(related_name='submissions', to='comments.Comment')),
                ('contest', models.ForeignKey(related_name='submissions', to='contests.Contest')),
                ('images', models.ManyToManyField(related_name='submissions', to='uploadedimages.UploadedImage')),
                ('user', models.ForeignKey(related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='submission',
            field=models.ForeignKey(related_name='ratings', to='contests.Submission'),
            preserve_default=True,
        ),
    ]
