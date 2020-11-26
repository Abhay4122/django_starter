from django.contrib import admin
from .models import *
import django.apps
from django import forms

# Register your models here.

# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].help_text = 'New help text for title'

#     class Meta:
#         model = Post
#         exclude = ('', )

# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm

# admin.site.register(PostFormAdmin)

class promoAdminArea(admin.AdminSite):
    site_header = 'promo Admin Area'

promo_site = promoAdminArea(name='promoAdmin')
# Register Post for promo
promo_site.register(Post)

# Register Post for admin

@admin.register(Post) # OR 1
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ('date',)
    fieldsets = (
        ('Section 1', {
            'fields': ('title', ),
            'description': 'Text about section 1',
        }),
    )
    # fields = ['title']

# admin.site.register(Post) # OR 1
# admin.site.register(PostAdmin) # OR 1


# models = django.apps.apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# # unregister the models
# admin.site.unregister(django.contrib.admin.models.LogEntry)
# admin.site.unregister(django.contrib.auth.models.Permission)
# admin.site.unregister(django.contrib.auth.models.Group)
# admin.site.unregister(django.contrib.auth.models.User)
# admin.site.unregister(django.contrib.contenttypes.models.ContentType)
# admin.site.unregister(django.contrib.sessions.models.Session)


# Customizing admin login

# class AdminArea(admin.AdminSite):
#     site_header = 'Admin Area'

# admin_site = AdminArea(name='AreaAdmin')
