import pytest
import time
from temp import TemperatureSensor

# Define a maximum acceptable execution time for critical functions
MAX_READ_TIME = 0.002  # 2 milliseconds
MAX_FILTER_TIME = 0.002
MAX_LOG_TIME = 0.005

@pytest.fixture
def sensor():
    """Fixture to create a sensor instance for testing."""
    return TemperatureSensor()

def test_read_temperature_performance(sensor):
    """Test that reading temperature completes within acceptable time."""
    start_time = time.perf_counter()
    _ = sensor.read_temperature()
    end_time = time.perf_counter()
    assert (end_time - start_time) < MAX_READ_TIME, "Temperature reading is too slow!"

def test_filter_temperature_performance(sensor):
    """Test that filtering operation completes within acceptable time."""
    start_time = time.perf_counter()
    _ = sensor.filter_temperature(25.0)
    end_time = time.perf_counter()
    assert (end_time - start_time) < MAX_FILTER_TIME, "Filtering is too slow!"

def test_log_temperature_performance(sensor, capsys):
    """Test that logging operation completes within acceptable time."""
    start_time = time.perf_counter()
    sensor.log_temperature(25.5)
    end_time = time.perf_counter()
    assert (end_time - start_time) < MAX_LOG_TIME, "Logging is too slow!"