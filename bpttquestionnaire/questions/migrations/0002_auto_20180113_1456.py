# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-13 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpquestions',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
