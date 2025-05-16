from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.sites.AdminSite.site_header = "پنل مدیریت جنگو"
admin.sites.AdminSite.site_title = "پنل"
admin.sites.AdminSite.index_title = "پنل مدیریت"


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'bio', 'photo', 'job', 'phone')}),
    )
