# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-13 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20180113_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpquestions',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
