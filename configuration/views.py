import random
# from django.shortcuts import render
from .models import Configuration, Name


# Name.__getattribute__(Name ,name='name')

# Create your views here.
def load_default(self):
    self.user_defined_name = self.name.Sys_name
    self.type = random.choice([True, False])
    self.is_active = True
    if self.type != 'mD':
        self.is_kpi = False
        self.unit = ''

    else:
        self.is_kpi = True
        self.unit = '$'

def load_all_from_default():
    configure = Configuration()
