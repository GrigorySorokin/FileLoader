# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0003_resulttask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulttask',
            name='id_file',
            field=models.IntegerField(),
        ),
    ]
