from django.db import models


class Name(models.Model):
    Sys_name = models.CharField(max_length=1)

    def __str__(self):
        return self.Sys_name


class Configuration(models.Model):
    FieldTypes = (
        ('aD', 'Dimension'),
        ('aM', 'Measure')
    )
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    user_defined_name = models.CharField(max_length=50)
    type = models.CharField(max_length=11, choices=FieldTypes)
    is_active = models.BooleanField(default=True)
    is_kpi = models.BooleanField(default=False)
    unit = models.CharField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.name.Sys_name

    # on save  change if any value is given
    def save(self, *args, **kwargs):
        if self.type != 'aM':
            self.is_kpi = False
            self.unit = None
        super(Configuration, self).save(*args, **kwargs)


class formula(models.Model):
    name = models.CharField(max_length=30, null=True, unique=True)
    formula = models.TextField(null=True)

    def __str__(self):
        return self.name