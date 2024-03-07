
from django.contrib import admin
from ..models import Otp


class OtpAdmin(admin.ModelAdmin):
    search_fields = ("phone", "otp")
    list_display = ("phone", "otp")
    readonly_fields = ("phone", "otp")


admin.site.register(Otp, OtpAdmin)
