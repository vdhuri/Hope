from django.contrib import admin
from ..models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')

admin.site.register(UserDetails, UserDetailsAdmin)
