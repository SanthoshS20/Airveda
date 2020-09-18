from django.db import models

class Device(models.Model):
  uid = models.IntegerField(unique="True")
  name = models.CharField(max_length=25)

  class Meta:
    db_table = "devices"

class TemperatureReading(models.Model):
  temperature_id = models.AutoField(primary_key=True)
  temperature_Celcius = models.FloatField()
  temperature_Fahrenheit = models.FloatField()

  class Meta:
    db_table = "temperatureReadings" 

class HumidityReading(models.Model):
  humidity_id = models.AutoField(primary_key=True)
  humidity = models.IntegerField()

  class Meta:
    db_table = "humidityReadings"

class AirQuality(TemperatureReading, HumidityReading):
  DateTime = models.DateTimeField()
  device = models.ForeignKey(Device, on_delete=models.CASCADE)

  class Meta:
    db_table = "airQualityData"
