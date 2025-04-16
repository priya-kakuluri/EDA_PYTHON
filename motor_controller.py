import time


class DCMotorController:
    def __init__(self, max_pwm=100):
        """
        Initialize the DC Motor Controller.

        :param max_pwm: Maximum PWM duty cycle (0-100%).
        """
        self.current_pwm = 0  # Current PWM duty cycle
        self.max_pwm = max_pwm  # Maximum allowable PWM
        self.target_speed = 0  # Desired motor speed (RPM)
        self.current_speed = 0  # Current measured speed (RPM)

    def set_speed(self, speed):
        """
        Set the target speed for the motor.

        :param speed: Desired speed in RPM.
        """
        self.target_speed = speed

    def update_pwm(self):
        """
        Adjust PWM duty cycle based on the speed error.
        Uses a simple proportional controller (P-control).
        """
        error = self.target_speed - self.current_speed
        pwm_adjustment = error * 0.5  # Proportional gain (Kp = 0.5)
        self.current_pwm = min(max(0, self.current_pwm + pwm_adjustment), self.max_pwm)

    def simulate_motor_response(self):
        """
        Simulates the motor reaching the set speed.
        In a real system, this would be replaced by a sensor reading.
        """
        self.current_speed += (self.current_pwm / self.max_pwm) * 10  # Simulated speed update
        self.current_speed = min(self.current_speed, self.target_speed)  # Limit speed

    def control_loop(self, duration=5):
        """
        Run the motor control loop for a given duration.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            self.update_pwm()
            self.simulate_motor_response()
            print(f"Target Speed: {self.target_speed} RPM, Current Speed: {self.current_speed:.2f} RPM, PWM: {self.current_pwm:.2f}%")
            time.sleep(0.5)  # Simulating control loop delay


# Example usage
if __name__ == "__main__":
    motor = DCMotorController()
    motor.set_speed(50)  # Set target speed to 50 RPM
    motor.control_loop()