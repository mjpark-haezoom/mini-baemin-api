# stores/admin.py

from django.contrib import admin

from .models import Menu, Store

admin.site.register(Store)
admin.site.register(Menu)
