from django.contrib import admin
from ..models import TemplateSection
from dynamic_raw_id.admin import DynamicRawIDMixin

class TemplateSectionAdmin(DynamicRawIDMixin,admin.ModelAdmin):
    list_display = ('template', 'plan_type',)
    list_filter = ('template', 'plan_type',)
    dynamic_raw_id_fields=('fields','template')




# Register the models with their respective admin classes

admin.site.register(TemplateSection, TemplateSectionAdmin)

