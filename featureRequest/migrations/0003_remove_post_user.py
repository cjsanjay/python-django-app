# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 01:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('featureRequest', '0002_auto_20160316_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
