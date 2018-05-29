import random
from .VerticaPythonConnectionPackage import connection
from sqlparse import format
import re
from decimal import  Decimal
import datetime
import json
from django.shortcuts import render
from .models import Configuration, Name, formula
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse,request
from .forms import FormulaForm
from configuration.admin import ConfigurationResource


def export_models (request):

    configuration_resource = ConfigurationResource()

    queryset1= Configuration.objects.filter(type="aM")
    queryset2= Configuration.objects.filter(type="aD")

    dataset0 = configuration_resource.export()
    dataset1 = configuration_resource.export(queryset1)
    dataset2 = configuration_resource.export(queryset2)
    mydataset = dataset0.json + dataset1.json  +  dataset2.json

    final_data = mydataset.replace('][', ',')


    response = HttpResponse(final_data,content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="config.json"'
    return response

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
    formulaList = formula.objects.all()
    context = {
        'list': formulaList,
        'form': FormulaForm
    }
    if request.method == "POST":
        form = FormulaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            # model_instance.timestamp = timezone.now()
            model_instance.save()
        return render(request, 'editor.html', context)
    else:
        form = FormulaForm

        return render(request, 'editor.html', context)
def editor_formula(request):

    return render(request, 'queryInspector.html')


def show_results(request):
    a = request.GET.get('a', ' ')
    text = a.replace('\'', '\"')
    parsed = format(text, reindent=True, keyword_case='upper') # from sqlparse
    parsed = parsed.split('\n')
    try:
        config = {
            "host": '10.90.21.44',
            "port": 5433,
            "user": 'dev_theresults_appuser',
            "database": 'cc_dev_qa_vertica01',
            "password": 'the_results_app1234'
        }
        vp = connection.Vertica(config=config)
        data = json.dumps(vp.read_data(a), default=myconverter)
        columnlist = [d.name for d in vp.cursor.description]
        return JsonResponse(data=json.loads(json.dumps({"error": False, "result":json.loads(data), "columnlist":columnlist, "formatList": parsed})), safe=False)
    except Exception as ex:
        msg = str(ex).lower().replace('vertica', 'DB')
        return JsonResponse(data=json.loads(json.dumps({"error":True,"errorMessage": msg})), safe=False)
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    if isinstance(o, Decimal):
        return str(o)