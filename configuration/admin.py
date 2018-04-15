from django.contrib import admin
from configuration.models import Configuration, Author

# Register your models here.


# class ConfigurationAdmin(admin.TabularInline):
#     fields = ['name', 'user_defined_name', 'type']
#

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user_defined_name', 'type']

admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Author)
