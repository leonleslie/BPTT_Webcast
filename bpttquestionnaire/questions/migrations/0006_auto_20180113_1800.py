# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-13 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20180113_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpquestions',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
