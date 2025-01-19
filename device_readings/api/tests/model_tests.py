from datetime import datetime
import pytest

from device_readings.api.models import Reading

pytestmark = pytest.mark.unit

def test_add_device_readings_idempotent(create_device_readings):
    device = create_device_readings
    assert len(device.readings) == 3
    r4 = Reading.model_validate({'timestamp': datetime(2020, 10, 10, 3, 0, 0, 0), 'count': 7})
    device.add(r4)
    assert len(device.readings) == 4
    device.add(r4)
    device.add(r4)
    device.add(r4)
    assert len(device.readings) == 4

def test_sum_device_readings_counts(create_device_readings):
    device = create_device_readings
    assert device.sum() == 12

def test_latest_device_reading(create_device_readings):
    device = create_device_readings
    assert device.get_latest_timestamp() == datetime(2020, 10, 10, 2, 0, 0, 0).isoformat()
