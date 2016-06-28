# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0006_auto_20160628_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcardinfo',
            name='nonghe_id',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='shebao_id',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
    ]
