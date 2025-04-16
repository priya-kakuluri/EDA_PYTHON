import pytest
from led_controller import LEDController
def test_led_turn_on():
    led=LEDController(gpio_pin=1)
    led.turn_on()
    assert led.get_state() == True

def test_led_turn_off():
    led=LEDController(gpio_pin=1)
    led.turn_on()
    led.turn_off()
    assert led.get_state() == False

def test_led_toggle():
    led=LEDController(gpio_pin=1)
    led.turn_on()
    assert led.get_state() == True
    led.turn_off()
    assert led.get_state() == False

def test_led_initial_state():
    led=LEDController(gpio_pin=1)
    assert led.get_state() == False