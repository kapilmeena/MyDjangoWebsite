from django.contrib import admin
from configuration.models import Configuration, Name
from django.http import request


# from django.contrib import messages

def  disable_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active = False)
disable_multiple_column.short_description = "mark these column deactivate"

def  activate_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active = True)
activate_multiple_column.short_description = "mark these column activate"


class ConfigurationAdmin(admin.ModelAdmin):

    list_display = ['name', 'user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']

    search_fields = ['name', 'user_defined_name', 'type']

    list_filter = ('type', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('name', 'user_defined_name', 'type', 'is_active')
        }),
        ('Advanced', {
            'classes': ('toggle',),
            'fields': ('is_kpi', 'unit'),
        })
    )
    actions = [disable_multiple_column, activate_multiple_column]

    class Media:
        js = ("jquery.js", "my_code.js",)


# class NameAdmin(admin.ModelAdmin):
#     admin.site.register(Name)

# class ConfigurationAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         #  At this point; the object already has the new values set; we will have to reset as needed
#         conditional_editable_fields = ['is_key', 'unit']
#         config_type = form.cleaned_data.get('type')
#         if config_type != 'aD':
#             for field in conditional_editable_fields:
#                 if field in form.changed_data:  # The value has been changed by the user
#                     setattr(obj, field, form.initial.get(field))  # Set the initial value
#                     self.message_user(request, "Cannot edit field: {}; value has been reset".format(field),
#                                       messages.WARNING)  # Inform the user that we reset the value
#         return super(ConfigurationAdmin, self).save_mode(request, obj, form, change)
#
#
#      if Configuration.type=='aD':
#     fieldsets=(
#             (None, {
#                 'fields': ('name', 'user_defined_name', 'type')
#             }),
#             ('Advanced', {
#                 'fields': ('unit','is_key')
#             })
#         )
#
#
#  def show_hide(self):
#     self.fields = Configuration.get_field_display()
# if Configuration.get_type(self=Configuration) == 'Dimension':
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'user_defined_name', 'type')
#         }),
#         ('Availability', {
#             'fields': ('is_key', 'unit')
#         })
#     )
# else:
#     fieldsets = (
#         (None, {
#             'fields': ('name', 'user_defined_name', 'type')
#         }),
#         ('Availability', {
#             'fields': ()
#         })
#     )


# class ConfigureEdits(admin.ChoicesFieldListFilter):
#     _field_list_filters =


admin.site.register(Configuration, ConfigurationAdmin)
