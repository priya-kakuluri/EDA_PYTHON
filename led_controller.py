# File: led_controller.py
class LEDController:
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.led_state = False  # False = OFF, True = ON

    def turn_on(self):
        """Turn the LED on."""
        self.led_state = True
        print(f"LED on GPIO {self.gpio_pin} is ON")

    def turn_off(self):
        """Turn the LED off."""
        self.led_state = False
        print(f"LED on GPIO {self.gpio_pin} is OFF")

    def get_state(self):
        """Get the current state of the LED."""
        return self.led_state