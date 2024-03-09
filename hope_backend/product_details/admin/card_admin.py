from django.contrib import admin
from ..models import  Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('template', 'id',)
    filter_horizontal = ('values',)

# Register the models with their respective admin classes
admin.site.register(Card, CardAdmin)
