# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-15 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='emp_name',
            new_name='name',
        ),
    ]