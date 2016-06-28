# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0005_auto_20160628_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcardinfo',
            name='address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='book_address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='tel',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
    ]
