from django.contrib import admin

# Register your models here.
from .models import Device,HumidityReading, TemperatureReading, AirQuality
admin.site.register(Device)
admin.site.register(HumidityReading)
admin.site.register(TemperatureReading)
admin.site.register(AirQuality)

