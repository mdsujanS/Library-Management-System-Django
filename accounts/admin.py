from django.contrib import admin
from .models import UserAccount


# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("get_username", "account_create_date", "balance")
    def get_username(self, obj):
        return obj.user.username
admin.site.register(UserAccount, UserAccountAdmin)