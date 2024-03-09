from django.contrib import admin
from ..models import Template

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)



# Register the models with their respective admin classes
admin.site.register(Template, TemplateAdmin)
