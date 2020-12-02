from django.contrib import admin
from .models import Student

# Register your models here.

class apiAdminArea(admin.AdminSite):
    site_header = 'Api admin area'

api_admin = apiAdminArea(name='apiAdmin')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'address')


api_admin.register(Student, StudentAdmin)
