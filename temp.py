import time
import random

class TemperatureSensor:
    def __init__(self):
        self.history = []

    def read_temperature(self):
        """Simulate reading temperature from a sensor."""
        return round(random.uniform(20.0, 30.0), 2)

    def filter_temperature(self, new_temp):
        """Simple moving average filter."""
        self.history.append(new_temp)
        if len(self.history) > 5:
            self.history.pop(0)
        return sum(self.history) / len(self.history)

    def log_temperature(self, filtered_temp):
        """Simulate logging temperature data (in real case, write to a file or memory)."""
        print(f"Logged Temperature: {filtered_temp:.2f}°C")

    def run(self):
        """Main function simulating an embedded loop."""
        while True:
            temp = self.read_temperature()
            filtered_temp = self.filter_temperature(temp)
            self.log_temperature(filtered_temp)
            time.sleep(1)  # Simulating a delay in an embedded system loop

if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.run()