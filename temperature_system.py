# File: temperature_system.py

class TemperatureSensor:
    """Simulates a temperature sensor."""
    def __init__(self):
        self.temperature = 25.0  # Default temperature in Celsius

    def read_temperature(self):
        """Read the current temperature."""
        return self.temperature

    def set_temperature(self, temperature):
        """Set the temperature (for simulation purposes)."""
        self.temperature = temperature

class FanController:
    """Controls a fan based on temperature readings."""
    def __init__(self, sensor, threshold=30.0):
        self.sensor = sensor
        self.threshold = threshold
        self.fan_state = False  # False = OFF, True = ON

    def check_temperature(self):
        """Check the temperature and control the fan."""
        current_temp = self.sensor.read_temperature()
        if current_temp > self.threshold:
            self.turn_on_fan()
        else:
            self.turn_off_fan()

    def turn_on_fan(self):
        """Turn the fan on."""
        self.fan_state = True
        print("Fan is ON")

    def turn_off_fan(self):
        """Turn the fan off."""
        self.fan_state = False
        print("Fan is OFF")

    def get_fan_state(self):
        """Get the current state of the fan."""
        return self.fan_state