from django.contrib import admin
from account.models import (
    Account
)

# Register your models here.
from django.contrib.auth import get_user_model

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','is_active']