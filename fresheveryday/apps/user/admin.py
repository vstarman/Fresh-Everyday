from django.contrib import admin
from apps.user import models

admin.site.register(models.User)
admin.site.register(models.Address)
