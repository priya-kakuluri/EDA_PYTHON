import pytest
import time
from motor_controller import DCMotorController

# Define acceptable performance limits
MAX_UPDATE_PWM_TIME = 0.002  # 2 milliseconds
MAX_SPEED_ERROR = 5  # Maximum allowable error in RPM

@pytest.fixture
def motor():
    """Fixture to create a motor controller instance."""
    return DCMotorController()

def test_update_pwm_performance(motor):
    """Test that the update_pwm function executes within the time limit."""
    start_time = time.perf_counter()
    motor.update_pwm()
    end_time = time.perf_counter()
    assert (end_time - start_time) < MAX_UPDATE_PWM_TIME, "PWM update is too slow!"

def test_motor_reaches_target_speed(motor):
    """Test if the motor reaches its target speed within tolerance."""
    motor.set_speed(50)  # Set desired speed to 50 RPM
    for _ in range(20):  # Simulate 20 control cycles
        motor.update_pwm()
        motor.simulate_motor_response()
        time.sleep(0.1)

    assert abs(motor.target_speed - motor.current_speed) <= MAX_SPEED_ERROR, "Motor speed did not reach target!"