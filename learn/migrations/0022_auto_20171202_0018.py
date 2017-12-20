# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-01 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0021_topic_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
