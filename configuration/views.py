import random
<<<<<<< HEAD
import re
import json
from django.shortcuts import render
from .models import Configuration, Name
from django.http import HttpResponse, HttpResponseRedirect
from configuration.admin import ConfigurationResource


def export_models (request):
    # dataset = ConfigurationResource().export()
    # data = json.load(dataset.json)
    configuration_resource = ConfigurationResource()
    queryset1 = Configuration.objects.filter(type='aM')
    queryset2 = Configuration.objects.filter(type='aD')
    dataset0 = configuration_resource.export()
    dataset1 = configuration_resource.export(queryset1)
    dataset2 = configuration_resource.export(queryset2)

    # data=json.loads(dataset0.json)
    # name=json.dumps(data)
    name = dataset0.export('json')

    response = HttpResponse(name)
    response['Content-Disposition'] = 'attachment; filename = "config.txt"'
    return response


    # dataset_final = json.dump('['.join({"name":dataset0)},{"aM":{dataset1.tsv}},{"aD":{dataset2.tsv}})+']')


    # Configuration.objects.all()

    # dataset_final = dataset1+dataset2
    #
    # datasets = dataset1+dataset2
    # dataset_final = json.load(datasets)
    #
    # return HttpResponse(json.dumps(dataset_final))
    # return HttpResponse(dataset_final)

    # return HttpResponse(dataset.json)
    # return HttpResponse(dataset.csv)
    # return HttpResponse(dataset.xls)
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="config.json"'
    # return response
    # response = HttpResponse(dataset.csv, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="config.csv"'
    # return response
    # response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="config.xls"'
    # return response
    # response = HttpResponse(dataset0.tsv, content_type='application/tsv')
    # response['Content-Disposition'] = 'attachment; filename="config.txt"'
    # return response
#
# import sys, os
#
# sys.path.append("")
# os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'
#
# from django.core.serializers import serialize
# from . import models
# def export_models(request):
#     model_names = ['Name', 'Configuration'] # a list of the names of the models you want to export
#
#     for model_name in model_names:
#         cls = getattr(models, model_name)
#         filename = model_name.lower() + ".json"
#         file = open(filename, "w")
#         file.write(serialize("json", cls.objects.all()))
#     return HttpResponse(status=200)
=======
# from django.shortcuts import render
from .models import Configuration, Name
>>>>>>> refs/remotes/origin/master


# Name.__getattribute__(Name ,name='name')

<<<<<<< HEAD

# Create your views here.
def load_default(self,Name):
    self.name = Name
    # self.user_defined_name = Name.Sys_name
    self.user_defined_name = re.sub('[^a-zA-Z0-9\n\.]', ' ', Name.Sys_name)
    self.type = random.choice(['aD', 'aM'])
    self.is_kpi = True
    self.is_active = True
    if self.type != 'aM':
        self.is_kpi = False
        self.unit = ''
=======
# Create your views here.
def load_default(self):
    self.user_defined_name = self.name.Sys_name
    self.type = random.choice([True, False])
    self.is_active = True
    if self.type != 'mD':
        self.is_kpi = False
        self.unit = ''

>>>>>>> refs/remotes/origin/master
    else:
        self.is_kpi = True
        self.unit = '$'

<<<<<<< HEAD

def populate(nameObject):
    try:
        configuration = Configuration()
        load_default(configuration, nameObject)
        configuration.save()
    except:
        pass


def load_all_from_default(request):
    names = Name.objects.all()  # get all the objects of Name model
    for name in names:
        populate(name)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

=======
def load_all_from_default():
    configure = Configuration()
>>>>>>> refs/remotes/origin/master
