# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160709_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscategory',
            name='category_id',
            field=models.IntegerField(unique=True, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xaeID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
    ]
