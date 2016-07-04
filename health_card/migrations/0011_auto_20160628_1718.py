# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0010_auto_20160628_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcardinfo',
            name='id_num',
            field=models.CharField(unique=True, max_length=18),
            preserve_default=True,
        ),
    ]
