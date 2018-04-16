# Generated by Django 2.0.4 on 2018-04-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0004_configuration_is_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='is_key',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='unit',
            field=models.CharField(blank=True, editable=False, max_length=30, null=True),
        ),
    ]
