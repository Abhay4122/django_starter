from django.contrib import admin
from .models import *

# Register your models here.

class promoAdminArea(admin.AdminSite):
    site_header = 'promo Admin Area'

promo_site = promoAdminArea(name='promoAdmin')
# Register Post for promo
promo_site.register(Post)
# Register Post for admin
admin.site.register(Post)
