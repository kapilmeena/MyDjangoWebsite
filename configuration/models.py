from django.db import models
import datetime
# import django.utils.timezone
# Create your models here.


class Configuration(models.Model):
    name = models.CharField(max_length=30)
    user_defined_name = models.CharField(max_length=50)
    FieldTypes = (('aD', 'Dimension'), ('aM', 'Measure'))
    type = models.CharField(max_length=11, choices=FieldTypes)

    def __str__(self):
        return self.name


class Author(models.Model):
    author_name = models.CharField(max_length=24)
    # author_dob = models.DateField(default=django.utils.timezone.now(), null=True)
    author_dob = models.DateField(default=datetime.date.today(), null=True)

    def __str__(self):
        return self.author_name
