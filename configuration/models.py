from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.


class Configuration(models.Model):

    name = models.CharField(max_length=30)
    user_defined_name = models.CharField(max_length=50)
    FieldTypes = (('aD', 'Dimension'), ('aM', 'Measure'))
    type = models.CharField(max_length=11, choices=FieldTypes)
    is_key = models.BooleanField(default=False, editable=True)
    unit = models.CharField(max_length=30, null=True, blank=True, editable=True)

    def __str__(self):
        return self.name

    def get_type(self):

        field_object = self._meta.get_field('type')
        value = self._get_FIELD_display(self, field_object)

        return value

    # def _get_FIELD_display(self, field):
    #     if self.is_key == 'True':
    #         # self.is_key = True
    #         self.unit = models.CharField(max_length=30, editable=True)
    #     return self.unit

    # def save(self, *args, **kwargs):
    #     if self.type == 'Dimension':
    #         self.is_key = models.BooleanField(default=False, editable=True)
    #         self.unit = models.CharField(max_length=30, null=True, blank=True, editable=True)
    #     super(Configuration, self).save(*args, **kwargs)

# @receiver(pre_save, sender=Configuration)
# def configuration_save_handler(sender, instance, *args, **kwargs):
#     if instance.types == 'Dimension':
#         instance.is_key = models.BooleanField(default=False, editable=True)
#         instance.unit = models.CharField(max_length=30, null=True, blank=True, editable=False)
