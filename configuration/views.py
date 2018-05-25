import random
import re
import json
from django.shortcuts import render
from .models import Configuration, Name, formula
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormulaForm
from configuration.admin import ConfigurationResource


def export_models (request):
    # dataset = ConfigurationResource().export()

    configuration_resource = ConfigurationResource()

    queryset1= Configuration.objects.filter(type="aM")
    queryset2= Configuration.objects.filter(type="aD")

    dataset0 = configuration_resource.export()
    dataset1 = configuration_resource.export(queryset1)
    dataset2 = configuration_resource.export(queryset2)

    # final_dataset = json.dump(dataset0.json)
    # final_dataset = json.load(dataset0.json)
    # final_dataset = json.load(dataset1.json)
    # final_dataset = json.load(dataset2.json)
    # arr = list()
    # arr.extend( [dataset0.json,dataset1.json,dataset2.json])

    mydataset = dataset0.json + dataset1.json  +  dataset2.json

    final_data = mydataset.replace('][', ',')


    response = HttpResponse(final_data,content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="config.json"'
    return response

    # response = HttpResponse(arr, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="config.json"'
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


# Name.__getattribute__(Name ,name='name')


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
    else:
        self.is_kpi = True
        self.unit = '$'


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

def show_me(request):
    return render(HttpResponse, 'admin/configure_changelist.html')

def show_formula(request):
    context = {
        'form': FormulaForm
    }
    list = Name.objects.all()
    if request.method == "POST":
        form = FormulaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            # model_instance.timestamp = timezone.now()
            model_instance.save()
            context = {
                'list': list,
                'form': FormulaForm
            }
        return render(request, 'editor.html', context)
    else:
        form = FormulaForm

        return render(request, 'editor.html', {'list':list})