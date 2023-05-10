from django.contrib import admin
from base.settings import LPS_CONFIG
from .models import *
# Register your models here.

if LPS_CONFIG['products_enabled']['GPU']:
    admin.site.register(GPU)

if LPS_CONFIG['products_enabled']['CPU']:
    admin.site.register(CPU)

if LPS_CONFIG['products_enabled']['PC']:
    admin.site.register(PC)