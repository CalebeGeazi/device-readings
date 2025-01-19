import json

from pydantic_core import ValidationError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Device, InMemoryDevices
devices = InMemoryDevices()

@api_view(['GET', 'POST'])
def manage_devices(request):
    if request.method == 'GET':
        return Response(devices.model_dump(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            device = Device(**json.loads(request.body))
            if device.id in devices.devices.keys():
                for r in device.readings:
                    devices.devices[device.id].add(r)
            else:
                devices.devices[device.id] = device

            return Response(devices.model_dump(), status=status.HTTP_201_CREATED)
        except ValidationError as e:
            response = {
                'error': f'Invalid Input: {e}',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def manage_device(request, **kwargs):
    if request.method == 'GET':
        result = get_or_404(**kwargs)
        if isinstance(result, Device):
            return Response(result.model_dump(), status=status.HTTP_200_OK)
        else:
            return result

@api_view(['GET'])
def sum_device(request, **kwargs):
    if request.method == 'GET':
        result = get_or_404(**kwargs)
        if isinstance(result, Device):
            response = {
                'cumulative_count': result.sum()
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return result

@api_view(['GET'])
def latest_device(request, **kwargs):
    if request.method == 'GET':
        result = get_or_404(**kwargs)
        if isinstance(result, Device):
            response = {
                'latest_timestamp': result.get_latest_timestamp()
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return result

def get_or_404(**kwargs) -> Device | Response:
    if kwargs['id']:
        if kwargs['id'] in devices.devices.keys():
            device = devices.devices[kwargs['id']]
            return device
        else:
            response = {
                'error': f'Device Not Found {kwargs["id"]}'
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
