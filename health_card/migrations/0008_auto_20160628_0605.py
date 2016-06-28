# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0007_auto_20160628_0558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthcardinfo',
            old_name='bank_name',
            new_name='salary_bank',
        ),
    ]
