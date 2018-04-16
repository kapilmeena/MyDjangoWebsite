from django.contrib import admin
from configuration.models import Configuration


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['is_key', 'name', 'user_defined_name', 'type']
    search_fields = ['name', 'user_defined_name', 'type']
class Meta :
    ordering : ['-name']

    # def show_hide(self):
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
