# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0009_auto_20160628_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandingBankInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_name', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='handing_bank',
            field=models.ForeignKey(to='health_card.HandingBankInfo', null=True),
            preserve_default=True,
        ),
    ]
