# Generated by Django 2.0.4 on 2018-04-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0008_auto_20180425_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='configuration',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.Name'),
        ),
    ]