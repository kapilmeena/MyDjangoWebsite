from django.db import models


# Create your models here.
class Name(models.Model):
    Sys_name = models.CharField(max_length=1)

    # class Meta:
    #     app_label = 'server_data' # this will be used for selecting database

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

    # class Meta:
    #     app_label = 'client_data' # this will be used for selecting database

    def __str__(self):
        return self.name.Sys_name

    # on save  change if any value is given
    def save(self, *args, **kwargs):
        if self.type != 'aM':
            self.is_kpi = False
            self.unit = None
        super(Configuration, self).save(*args, **kwargs)


    # clean get called on validation
    # def clean(self):
    #     if self.type == 'aM':
    #         if self.unit

    # def save(self, *args, **kwargs):
    #     if self.type == 'Dimension':
    #         self.is_kpi = models.BooleanField(default=False, editable=True)
    #         self.unit = models.CharField(max_length=30, null=True, blank=True, editable=True)
    #     super(Configuration, self).save(*args, **kwargs)


class formula(models.Model):
    f_name = models.CharField(max_length=30, null=True)
    f_description = models.TextField(null=True)

    def __str__(self):
        return self.f_name