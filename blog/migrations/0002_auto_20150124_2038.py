# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(related_name='posts', null=True, to='uploadedimages.UploadedImage', blank=True),
            preserve_default=True,
        ),
    ]
