# Generated by Django 2.0.4 on 2018-04-25 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0007_auto_20180417_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='is_key',
            new_name='is_kpi',
        ),
    ]
