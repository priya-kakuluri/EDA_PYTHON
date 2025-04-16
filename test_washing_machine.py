import pytest
import serial
from washing_machine import WashingMachine

class MockSerial:
    """Mock class to simulate pyserial.Serial."""
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.responses = iter([
            b"TEMP: 40.0, WATER: 75\n",
            b"TEMP: 30.5, WATER: 50\n",
        ])

    def write(self, command):
        return len(command)

    def readline(self):
        return next(self.responses, b"TEMP: 40.0, WATER: 75\n")

    def close(self):
        pass

@pytest.fixture
def mock_serial(monkeypatch):
    """Replace serial.Serial with MockSerial."""
    monkeypatch.setattr(serial, "Serial", MockSerial)


import psutil

@pytest.fixture
def monitor_resources():
    """Monitor CPU & memory usage before and after test execution"""
    start_cpu = psutil.cpu_percent(interval=1)  # 1-second delay for accuracy
    start_mem = psutil.virtual_memory().used
    yield  # Run the test
    end_cpu = psutil.cpu_percent(interval=1)
    end_mem = psutil.virtual_memory().used

    print(f"\nCPU Usage Change: {abs(end_cpu - start_cpu)}%")
    print(f"Memory Usage Change: {abs(end_mem - start_mem)} bytes")



@pytest.mark.parametrize("expected_temp, expected_water", [
    (40.0, 75),
    (30.5, 50)
])
def test_read_sensors(mock_serial, expected_temp, expected_water):
    """Test sensor reading with a mocked serial port."""
    machine = WashingMachine(port="COM3", baudrate=9600)
    result = machine.read_sensors()
    assert result == {"temperature": expected_temp, "water_level": expected_water}, \
        f"Expected {expected_temp}, {expected_water} but got {result}"


@pytest.mark.parametrize("speed, expected_output", [
    (50, "Motor Running"),
    (100, "Motor Running"),
    (-1, "Invalid Speed"),
    (120, "Invalid Speed")
])
def test_control_motor(mock_serial, speed, expected_output):
    """Test motor speed control logic"""
    machine = WashingMachine(port="COM3", baudrate=9600)
    assert machine.control_motor(speed) == expected_output
    machine.close()

@pytest.mark.parametrize("lock, expected_output", [
    (True, "Door Locked"),
    (False, "Door Unlocked")
])
def test_lock_door(mock_serial, lock, expected_output):
    """Test door lock functionality"""
    machine = WashingMachine(port="COM3", baudrate=9600)
    assert machine.lock_door(lock) == expected_output
    machine.close()


@pytest.mark.benchmark
def test_performance_benchmark(benchmark):
    """Benchmark performance of sensor reading."""
    machine = WashingMachine(port="COM3", baudrate=9600)

    result = benchmark(machine.read_sensors)

    assert isinstance(result, dict)
    assert "temperature" in result
    assert "water_level" in result

