from django.contrib import admin
from apps.order import models

admin.site.register(models.OrderGoods)
admin.site.register(models.OrderInfo)
