# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favoutire',
            field=models.BooleanField(default=False),
        ),
    ]
