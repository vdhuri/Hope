from django.contrib import admin
from ..models import  Field



class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_type', 'is_required', 'is_disabled')
    list_filter = ('field_type', 'is_required', 'is_disabled')


# Register the models with their respective admin classes
admin.site.register(Field, FieldAdmin)

