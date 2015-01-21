# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=10000)),
                ('comment_level', models.PositiveIntegerField(default=12)),
                ('deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(related_name='parent', blank=True, to='comments.Comment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
