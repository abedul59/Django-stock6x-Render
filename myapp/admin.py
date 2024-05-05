from django.contrib import admin

# Register your models here.
from myapp.models import NewsUnit
from myapp.models import Person
from myapp import models

admin.site.register(NewsUnit)
admin.site.register(Person)
admin.site.register(models.MacroWaveA)
admin.site.register(models.MacroWaveB)
admin.site.register(models.MacroWaveC)
admin.site.register(models.USBondYieldDB)


admin.site.register(models.Stock6Sign202404)
admin.site.register(models.StockPERseg202404)