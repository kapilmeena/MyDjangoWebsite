# Generated by Django 2.0.4 on 2018-04-25 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0009_auto_20180425_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='name',
            new_name='Sys_name',
        ),
    ]
