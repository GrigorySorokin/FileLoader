# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0002_downloadfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_file', models.FileField(upload_to='')),
                ('percent', models.IntegerField()),
                ('done', models.BooleanField()),
                ('length', models.IntegerField()),
            ],
        ),
    ]
