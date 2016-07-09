# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160709_0659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '\u65b0\u95fb', 'verbose_name_plural': '\u65b0\u95fb'},
        ),
        migrations.AlterModelOptions(
            name='newscategory',
            options={'verbose_name': '\u65b0\u95fb\u680f\u76ee', 'verbose_name_plural': '\u65b0\u95fb\u680f\u76ee'},
        ),
        migrations.AddField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 9, 12, 17, 47, 843928, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 9, 12, 17, 58, 559608, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
