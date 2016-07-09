# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20160709_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscategory',
            name='category_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
