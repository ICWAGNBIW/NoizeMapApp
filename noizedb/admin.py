from django.contrib import admin
from .models import Coordinates, Measurement, Estimation, CorFrom, CorChark
# Register your models here.

admin.site.register(Coordinates)
admin.site.register(Measurement)
admin.site.register(Estimation)
admin.site.register(CorFrom)
admin.site.register(CorChark)