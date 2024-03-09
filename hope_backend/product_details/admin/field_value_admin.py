from django.contrib import admin
from ..models import  FieldValue


class FieldValueAdmin(admin.ModelAdmin):
    list_display = ('field', 'text', 'file',)
    list_filter = ('field',)


# Register the models with their respective admin classes

admin.site.register(FieldValue, FieldValueAdmin)

