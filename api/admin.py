from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Student, User
from .forms import UserAdminChangeForm, UserAdminCreationForm
import django.apps

# Register your models here.

class apiAdminArea(admin.AdminSite):
    site_header = 'Api admin area'

api_admin = apiAdminArea(name='apiAdmin')

class StudentConfig(admin.ModelAdmin):
    search_fields = ('name', 'email')
    ordering = ('-doj',)
    list_filter = ('doj',)
    list_display = ('name', 'email', 'contact', 'address')


api_admin.register(Student, StudentConfig)

admin.site.register(Student, StudentConfig)


class UserConfig(BaseUserAdmin):
    ordering = ('-doj',)
    list_display = ('email', 'name', 'contact', 'is_staff')
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal', {'fields': ('name', 'contact', 'bio')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

admin.site.register(User, UserConfig)

admin.site.register(django.contrib.admin.models.LogEntry)
# admin.site.unregister(django.contrib.auth.models.User)

# models = django.apps.apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
