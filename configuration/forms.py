# from django.forms import forms
# from .models import Name
#
#
# class ConfigurationForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ConfigurationForm, self).__init__(*args, **kwargs)
#
#         #only provide users that are not already linked to an actor, plus the user that was already chosen for this Actor
#         self.fields['name'].queryset = Name.objects.filter(Name(name__isnull=True))