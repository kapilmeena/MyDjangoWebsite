# Generated by Django 2.0.4 on 2018-04-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=24)),
                ('author_dob', models.DateField(default=2018, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user_defined_name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('aD', 'Dimension'), ('aM', 'Measure')], max_length=11)),
            ],
        ),
    ]
