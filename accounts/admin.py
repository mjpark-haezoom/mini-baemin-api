# accounts/admin.py

from django.contrib import admin

from .models import User

# Temporarily disable admin registration for new user models
# to avoid migration issues
admin.site.register(User)