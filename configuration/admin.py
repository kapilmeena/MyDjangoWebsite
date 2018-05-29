from django.contrib import admin
from django.contrib.admin import AdminSite
from configuration.models import Configuration, Name, formula
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

class ConfigurationResource(resources.ModelResource):
    name = resources.Field()
    # measure = resources.Field(column_name='measure') # column name represent the name of column in exported data
    # dimension = resources.Field(column_name='dimension')
    # full_title = resources.Field()

    class Meta:
        model = Configuration
        fields = ('name',)

    def dehydrate_name(self,Configuration):
        return '%s' %(Configuration.user_defined_name)

class ConfigurationAdmin(ImportExportActionModelAdmin):
    pass

# action function
def disable_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active=False)


# action function
def activate_multiple_column(modeladmin, request, queryset):
    queryset.update(is_active=True)


# description for display in action dropdown
disable_multiple_column.short_description = "mark these column deactivate"
activate_multiple_column.short_description = "mark these column activate"


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']
    # list_display = ['user_defined_name', 'type', 'is_active', 'is_kpi', 'unit']
    search_fields = ['name', 'user_defined_name']
    list_filter = ('type', 'is_active')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'user_defined_name', 'type', 'is_active')
        }),
        ('Advanced', {
            'classes': ('toggle',),
            'fields': ('is_kpi', 'unit'),
        })
    )
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


class formulaAdmin(admin.ModelAdmin):
    class Media:
        js = ("ace-builds/src-noconflict/ace.js","my_formula_script.js",)
        css = ("my_formula_css.js",)


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'


admin_site = MyAdminSite(name='myadmin')

# register our model with admin
admin.site.register(Configuration, ConfigurationAdmin)

admin.site.register(formula)