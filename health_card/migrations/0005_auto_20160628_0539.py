# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0004_auto_20160628_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_name', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='id_num',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='unit_name',
            field=models.ForeignKey(to='health_card.UnitInfo', null=True),
            preserve_default=True,
        ),
    ]
