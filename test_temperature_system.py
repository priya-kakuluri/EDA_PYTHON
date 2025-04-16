# File: test_temperature_system.py

import pytest
from temperature_system import TemperatureSensor, FanController

def test_fan_turns_on_above_threshold(mocker):
    """Test that the fan turns on when the temperature exceeds the threshold."""
    # Mock the TemperatureSensor
    mock_sensor = mocker.MagicMock(spec=TemperatureSensor)
    mock_sensor.read_temperature.return_value = 35.0  # Simulate high temperature

    # Create a FanController instance with the mocked sensor
    fan_controller = FanController(sensor=mock_sensor, threshold=30.0)

    # Check the temperature
    fan_controller.check_temperature()

    # Verify the fan is turned on
    assert fan_controller.get_fan_state() is True

def test_fan_turns_off_below_threshold(mocker):
    """Test that the fan turns off when the temperature is below the threshold."""
    # Mock the TemperatureSensor
    mock_sensor = mocker.MagicMock(spec=TemperatureSensor)
    mock_sensor.read_temperature.return_value = 25.0  # Simulate low temperature

    # Create a FanController instance with the mocked sensor
    fan_controller = FanController(sensor=mock_sensor, threshold=30.0)

    # Check the temperature
    fan_controller.check_temperature()

    # Verify the fan is turned off
    assert fan_controller.get_fan_state() is False

def test_fan_initial_state(mocker):
    """Test the initial state of the fan."""
    # Mock the TemperatureSensor
    mock_sensor = mocker.MagicMock(spec=TemperatureSensor)
    mock_sensor.read_temperature.return_value = 25.0  # Simulate low temperature

    # Create a FanController instance with the mocked sensor
    fan_controller = FanController(sensor=mock_sensor, threshold=30.0)

    # Verify the fan is initially off
    assert fan_controller.get_fan_state() is False