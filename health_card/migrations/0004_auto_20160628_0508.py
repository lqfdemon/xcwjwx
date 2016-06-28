# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_card', '0003_healthcardinfo_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('education_back', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NationInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nation', models.CharField(unique=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='education_back',
            field=models.ForeignKey(to='health_card.EducationInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='healthcardinfo',
            name='nation',
            field=models.ForeignKey(to='health_card.NationInfo', null=True),
            preserve_default=True,
        ),
    ]
