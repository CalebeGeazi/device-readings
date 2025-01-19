import pytest

from datetime import datetime
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.unit

def test_create_device_reading(api_client, create_device_readings,
                               create_device_readings_w_duplicates, create_device_readings_final):
    url = reverse('devices')
    response = api_client.post(url, create_device_readings.model_dump(), format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['devices']['id-1'] == create_device_readings.model_dump()
    response = api_client.post(url, create_device_readings_w_duplicates.model_dump(), format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['devices']['id-1'] == create_device_readings_final.model_dump()

def test_get_all_devices(api_client, create_device_readings_final):
    url = reverse('devices')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['devices']['id-1'] == create_device_readings_final.model_dump()

def test_create_device_reading_invalid_input(api_client, invalid_input):
    url = reverse('devices')
    response = api_client.post(url, invalid_input, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Invalid Input' in response.data['error']

def test_get_single_device_readings(api_client, create_device_readings_final):
    url = reverse('device', kwargs={'id': 'id-1'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == create_device_readings_final.model_dump()

def test_get_single_device_readings_404(api_client):
    url = reverse('device', kwargs={'id': 'some-nonexistent-id'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == 'Device Not Found some-nonexistent-id'

def test_sum_device_readings(api_client):
    url = reverse('device_sum', kwargs={'id': 'id-1'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'cumulative_count': 21}

def test_sum_device_readings_404(api_client):
    url = reverse('device_sum', kwargs={'id': 'some-nonexistent-id'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == 'Device Not Found some-nonexistent-id'

def test_latest_timestamp(api_client):
    url = reverse('device_latest', kwargs={'id': 'id-1'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'latest_timestamp': datetime(2020, 10, 10, 4, 0, 0, 0).isoformat()}

def test_latest_timestamp_404(api_client):
    url = reverse('device_latest', kwargs={'id': 'some-nonexistent-id'})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == 'Device Not Found some-nonexistent-id'
