from django.contrib import admin
from .models import Student, User

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


class UserConfig(admin.ModelAdmin):
    ordering = ('-doj',)
    list_display = ('email', 'name', 'contact', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('name', 'contact')}),
    )


admin.site.register(User, UserConfig)
