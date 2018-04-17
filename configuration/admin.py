from django.contrib import admin
from configuration.models import Configuration
from django.contrib import messages


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_defined_name', 'type', 'is_key']
    search_fields = ['name', 'user_defined_name', 'type']
    list_filter = ('type',)
    fieldsets = (
            (None, {
                'fields': ('name', 'user_defined_name', 'type')
            }),
            ('Advanced', {
                'fields': ('is_key', 'unit')
            })
        )

    class Media:
       js = ("jquery.js", "my_code.js",)

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

    # if Configuration.type=='aD':
    #     fieldsets=(
    #             (None, {
    #                 'fields': ('name', 'user_defined_name', 'type')
    #             }),
    #             ('Advanced', {
    #                 'fields': ('unit','is_key')
    #             })
    #         )


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
