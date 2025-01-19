from datetime import datetime
import pytest

from rest_framework.test import APIClient

from device_readings.api.models import Device, Reading

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_device_readings():
    r1 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 0, 0, 0, 0), 'count': 3})
    r2 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 1, 0, 0, 0), 'count': 4})
    r3 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 2, 0, 0, 0), 'count': 5})
    d = Device.model_validate({'id': 'id-1', 'readings': [r1, r2, r3]})
    return d

@pytest.fixture
def create_device_readings_w_duplicates():
    r1 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 2, 0, 0, 0), 'count': 3})
    r2 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 3, 0, 0, 0), 'count': 4})
    r3 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 4, 0, 0, 0), 'count': 5})
    d = Device.model_validate({'id': 'id-1', 'readings': [r1, r2, r3]})
    return d

@pytest.fixture
def create_device_readings_final():
    r1 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 0, 0, 0, 0), 'count': 3})
    r2 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 1, 0, 0, 0), 'count': 4})
    r3 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 2, 0, 0, 0), 'count': 5})
    r4 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 3, 0, 0, 0), 'count': 4})
    r5 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 4, 0, 0, 0), 'count': 5})
    d = Device.model_validate({'id': 'id-1', 'readings': [r1, r2, r3, r4, r5]})
    return d

@pytest.fixture
def invalid_input():
    return {
        'id': 'some-id',
        'readings': []
    }
