from rest_framework import status
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from air_quality.serializers import *

@api_view(['GET', 'POST'])
def addDevice(request):
  device_serializer = DeviceSerializer(data=request.data)
  if device_serializer.is_valid():
    device_serializer.save()
    return Response({"data" : "Device Added Successfully"}, status=status.HTTP_201_CREATED)
  elif(request.method=="GET"):
    device_obj = Device.objects.all()
    device_data = DeviceSerializer(device_obj, many= True).data
    return Response({"data": device_data}, status=status.HTTP_200_OK)
  else:
    return Response({"data" : "failed to return the details"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def update_device(request, uid):
  device_obj = Device.objects.get(uid=uid)

  if(request.method=="GET"):
    device_data = DeviceSerializer(device_obj).data
    return Response({"data" : device_data}, status=status.HTTP_200_OK)
  elif(request.method=="DELETE"):
    device_obj.delete()
    return Response({"data" : "Device delete Successfully"}, status=status.HTTP_200_OK)
  else:
    return Response({"data" : "Failed to show Device data"}, status=status.HTTP_400_BAD_REQUEST)



