from django.contrib import admin

# Register your models here.
from myapp.models import Stock6Sign202404
from myapp.models import NewsUnit
from myapp.models import Person

admin.site.register(NewsUnit)
admin.site.register(Person)
admin.site.register(Stock6Sign202404)