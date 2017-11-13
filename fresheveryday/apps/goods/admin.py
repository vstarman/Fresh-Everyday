from django.contrib import admin
from apps.goods import models

admin.site.register(models.GoodsType)
admin.site.register(models.Goods)
admin.site.register(models.GoodsSKU)
admin.site.register(models.GoodsImage)
admin.site.register(models.IndexGoodsBanner)
admin.site.register(models.IndexTypeGoodsBanner)
admin.site.register(models.IndexPromotionBanner)
