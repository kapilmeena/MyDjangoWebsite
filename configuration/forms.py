from django.forms import ModelForm
from .models import Name, formula
#
#
# class ConfigurationForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ConfigurationForm, self).__init__(*args, **kwargs)
#
#         #only provide users that are not already linked to an actor, plus the user that was already chosen for this Actor
#         self.fields['name'].queryset = Name.objects.filter(Name(name__isnull=True))


class FormulaForm(ModelForm):
    class Meta:
        model = formula
        fields = ['f_name', 'f_description']
