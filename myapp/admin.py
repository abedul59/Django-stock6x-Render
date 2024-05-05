from django.contrib import admin

# Register your models here.
from myapp import models

admin.site.register(models.Person)
admin.site.register(models.NewsUnit)
admin.site.register(models.Stock6Sign202404)
admin.site.register(models.StockPERseg202404)