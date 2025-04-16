import serial
import time
import logging

logging.basicConfig(filename="washing_machine.log", level=logging.INFO, format="%(asctime)s - %(message)s")


class WashingMachine:
    """Simulates an embedded system for a washing machine."""

    def __init__(self, port, baudrate=9600, timeout=2):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(2)  # Allow time for connection
            logging.info("Serial connection established")
        except serial.SerialException as e:
            logging.error(f"Serial connection failed: {e}")
            raise

    def read_sensors(self):
        """Reads water level & temperature from the serial port."""
        try:
            raw_data = self.ser.readline().decode().strip()
            logging.info(f"Received: {raw_data}")
            if "TEMP:" in raw_data and "WATER:" in raw_data:
                temp = float(raw_data.split("TEMP:")[1].split(",")[0])
                water = int(raw_data.split("WATER:")[1])
                return {"temperature": temp, "water_level": water}
        except Exception as e:
            logging.error(f"Error reading sensors: {e}")
        return None

    def control_motor(self, speed):
        """Controls motor speed for washing cycles."""
        if not 0 <= speed <= 100:
            return "Invalid Speed"
        command = f"MOTOR_SPEED:{speed}\n"
        try:
            self.ser.write(command.encode())
            logging.info(f"Sent: {command}")
            return "Motor Running"
        except Exception as e:
            logging.error(f"Error sending motor command: {e}")
            return "Motor Error"

    def lock_door(self, lock):
        """Locks/unlocks the washing machine door."""
        command = "LOCK:ON\n" if lock else "LOCK:OFF\n"
        try:
            self.ser.write(command.encode())
            logging.info(f"Sent: {command}")
            return "Door Locked" if lock else "Door Unlocked"
        except Exception as e:
            logging.error(f"Error locking door: {e}")
            return "Lock Error"

    def close(self):
        """Closes the serial connection."""
        self.ser.close()
        logging.info("Serial connection closed")
