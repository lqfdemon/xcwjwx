# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160709_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=1000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='sub_title',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=True,
        ),
    ]
