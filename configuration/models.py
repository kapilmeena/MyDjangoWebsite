from django.db import models
<<<<<<< HEAD


# Create your models here.
class Name(models.Model):
    Sys_name = models.CharField(max_length=1)

    # class Meta:
    #     app_label = 'server_data' # this will be used for selecting database
=======
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.


class Name(models.Model):
    Sys_name = models.CharField(max_length=1)
    #
    # class Meta:
    #     app_label = 'server_data'
>>>>>>> refs/remotes/origin/master

    def __str__(self):
        return self.Sys_name


class Configuration(models.Model):

    FieldTypes = (
        ('aD', 'Dimension'),
        ('aM', 'Measure')
    )

    name = models.OneToOneField(Name, on_delete=models.CASCADE)
<<<<<<< HEAD
=======
    # name = models.ForeignKey(Name, on_delete=models.CASCADE, unique=True)
>>>>>>> refs/remotes/origin/master

    user_defined_name = models.CharField(max_length=50)

    type = models.CharField(max_length=11, choices=FieldTypes)

    is_active = models.BooleanField(default=True)

    is_kpi = models.BooleanField(default=False)

    unit = models.CharField(max_length=30, null=True, blank=True)

<<<<<<< HEAD
    # class Meta:
    #     app_label = 'client_data' # this will be used for selecting database
=======

    #
    # class Meta:
    #     app_label = 'client_data'
>>>>>>> refs/remotes/origin/master

    def __str__(self):
        return self.name.Sys_name

<<<<<<< HEAD
    # on save  change if any value is given
=======
>>>>>>> refs/remotes/origin/master
    def save(self, *args, **kwargs):
        if self.type != 'aM':
            self.is_kpi = False
            self.unit = None
        super(Configuration, self).save(*args, **kwargs)

<<<<<<< HEAD
    # clean get called on validation
    # def clean(self):
    #     if self.type == 'aM':
    #         if self.unit
=======
    # def clean(self):
    #     if self.type == 'aM':
    #         if self.unit
    #

    # def get_type(self):
    #
    #     field_object = self._meta.get_field('type')
    #     value = self._get_FIELD_display(self, field_object)
    #
    #     return value

    # def _get_FIELD_display(self, field):
    #     if self.is_kpi == 'True':
    #         # self.is_kpi = True
    #         self.unit = models.CharField(max_length=30, editable=True)
    #     return self.unit
>>>>>>> refs/remotes/origin/master

    # def save(self, *args, **kwargs):
    #     if self.type == 'Dimension':
    #         self.is_kpi = models.BooleanField(default=False, editable=True)
    #         self.unit = models.CharField(max_length=30, null=True, blank=True, editable=True)
    #     super(Configuration, self).save(*args, **kwargs)
<<<<<<< HEAD
=======

# @receiver(pre_save, sender=Configuration)
# def configuration_save_handler(sender, instance, *args, **kwargs):
#     if instance.types == 'Dimension':
#         instance.is_key = models.BooleanField(default=False, editable=True)
#         instance.unit = models.CharField(max_length=30, null=True, blank=True, editable=False)
>>>>>>> refs/remotes/origin/master
