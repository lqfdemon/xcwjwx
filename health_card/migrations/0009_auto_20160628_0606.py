# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0008_auto_20160628_0605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BankInfo',
            new_name='SalaryBankInfo',
        ),
    ]
