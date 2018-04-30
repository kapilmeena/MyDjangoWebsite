from django.contrib import admin
<<<<<<< HEAD
from django.contrib.admin import AdminSite
from configuration.models import Configuration, Name
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

class ConfigurationResource(resources.ModelResource):
    # name = Field(column_name='user_defined_name')
    # name = Field()

    class Meta:
        model = Configuration
        fields = ('user_defined_name',)
        # fields = ('name',)
        # exclude = ('type',)

        # def dehydrate_name(self, configuration):
        #     return '%s' % (configuration.user_defined_name)

# class ConfigurationAdmin(ImportExportModelAdmin):
#     resource_class = ConfigurationResource

# class ConfigurationAdmin(ImportExportActionModelAdmin):
#     pass

# action function
def disable_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active=False)


# action function
def activate_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active=True)


# description for display in action dropdown
disable_multiple_column.short_description = "mark these column deactivate"
=======
from configuration.models import Configuration, Name
from django.http import request


# from django.contrib import messages

def  disable_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active = False)
disable_multiple_column.short_description = "mark these column deactivate"

def  activate_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active = True)
>>>>>>> refs/remotes/origin/master
activate_multiple_column.short_description = "mark these column activate"


class ConfigurationAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['name', 'user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']
    # list_display = ['user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']
    search_fields = ['name', 'user_defined_name']
    list_filter = ('type', 'is_active')
    ordering = ('name',)
=======

    list_display = ['name', 'user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']

    search_fields = ['name', 'user_defined_name', 'type']

    list_filter = ('type', 'is_active')

>>>>>>> refs/remotes/origin/master
    fieldsets = (
        (None, {
            'fields': ('name', 'user_defined_name', 'type', 'is_active')
        }),
        ('Advanced', {
            'classes': ('toggle',),
            'fields': ('is_kpi', 'unit'),
        })
    )
<<<<<<< HEAD
    actions = [disable_multiple_column, activate_multiple_column]  # list of action function here

    def has_add_permission(self, request):  # add delete option for this model
        return False

    def has_delete_permission(self, request, obj=None):  # disable delete option for this model
        return False

    def get_actions(self, request):  # remove default 'delete selected' action
        actions = super().get_actions(request)
        if 'delete_selected' in actions and not ConfigurationAdmin.has_delete_permission(self, request):
            del actions['delete_selected']
        return actions

    # index_template = "admin/configure_changelist.html"
    change_list_template = "admin/configure_changelist.html"

    class Media:
        js = ("admin/js/jquery.js", "admin/js/my_code.js",)  # JS for conditionally hide advance field


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'


admin_site = MyAdminSite(name='myadmin')
=======
    actions = [disable_multiple_column, activate_multiple_column]

    class Media:
        js = ("jquery.js", "my_code.js",)


>>>>>>> refs/remotes/origin/master
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

<<<<<<< HEAD
# register our model with admin
=======

>>>>>>> refs/remotes/origin/master
admin.site.register(Configuration, ConfigurationAdmin)
