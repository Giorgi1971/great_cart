from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Work with admin panel, customised that. For Password Read-only
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('first_name', 'last_name')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
