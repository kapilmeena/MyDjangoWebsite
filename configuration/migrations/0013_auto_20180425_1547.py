# Generated by Django 2.0.4 on 2018-04-25 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0012_auto_20180425_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configuration.Name'),
        ),
    ]
