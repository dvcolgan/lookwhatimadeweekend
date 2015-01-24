# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='images',
            field=models.ManyToManyField(related_name='submissions', null=True, to='uploadedimages.UploadedImage', blank=True),
            preserve_default=True,
        ),
    ]
