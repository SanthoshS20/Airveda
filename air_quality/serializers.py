from rest_framework import serializers
from .models import *

class DeviceSerializer(serializers.Serializer):
  uid = serializers.IntegerField()
  name = serializers.CharField(max_length=25)

  def create(self, validated_data):
    device_obj = Device(**validated_data)
    device_obj.save()
    return device_obj

  class Meta:
    db_table = "devices"

class TemperatureReadingSerializer(serializers.Serializer):
  temperature_Celcius = serializers.FloatField()
  temperature_Fahrenheit = serializers.FloatField()

  class Meta:
    db_table = "temperatureReadings" 

class HumidityReadingSerializer(serializers.Serializer):
  humidity = serializers.IntegerField()

  class Meta:
    db_table = "humidityReadings"

class AirQualitySerializer(TemperatureReading, HumidityReading):
  DateTime = serializers.DateTimeField()

  class Meta:
    db_table = "airQualityData"
