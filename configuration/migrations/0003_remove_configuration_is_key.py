# Generated by Django 2.0.4 on 2018-04-16 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_auto_20180416_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='is_key',
        ),
    ]
