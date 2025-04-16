import pytest
from unittest.mock import patch
from embedded_code import read_temp_simulated  # Replace 'your_module' with the name of your Python file


def test_read_temp_simulated():
    # Mock random.uniform to return a fixed value
    with patch('random.uniform', return_value=25.0):
        temp_c, temp_f = read_temp_simulated()

        # Verify the Celsius value
        assert temp_c == 25.0

        # Verify the Fahrenheit conversion
        assert temp_f == 25.0 * 9.0 / 5.0 + 32.0


def test_read_temp_simulated_range():
    # Test multiple calls to ensure the temperature stays within the expected range
    # for _ in range(10):  # Test 100 random values
    temp_c, temp_f = read_temp_simulated()

        # Check if the temperature is within the expected range
    assert 20.0 <= temp_c <= 30.0
    assert 68.0 <= temp_f <= 86.0  # Corresponding Fahrenheit range