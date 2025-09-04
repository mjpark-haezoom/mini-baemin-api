# accounts/admin.py

from django.contrib import admin

from .models import ConsumerUser, OperatorUser, OwnerUser, User

# Temporarily disable admin registration for new user models
# to avoid migration issues
admin.site.register(ConsumerUser)
admin.site.register(OwnerUser)
admin.site.register(OperatorUser)
admin.site.register(User)
