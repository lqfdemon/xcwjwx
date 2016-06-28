# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0002_bankinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcardinfo',
            name='bank_name',
            field=models.ForeignKey(to='health_card.BankInfo', null=True),
            preserve_default=True,
        ),
    ]
