import sys
import sqlite3
from PySide6.QtCore import QObject, Slot, Signal, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import random
import datetime

# 🔹 Backend Class with Database Functionality
class AuthBackend(QObject):
    loginSuccess = Signal(bool)
    registerSuccess = Signal(bool)

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)'''
        )
        self.conn.commit()

    @Slot(str, str)
    def login(self, username, password):
        """Check if user credentials exist in the database."""
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = self.cursor.fetchone()
        if result:
            print("✅ Login Successful")
            self.loginSuccess.emit(True)
        else:
            print("❌ Invalid Credentials")
            self.loginSuccess.emit(False)

    @Slot(str, str)
    def register(self, username, password):
        """Register a new user if username is unique."""
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            print("✅ User Registered Successfully")
            self.registerSuccess.emit(True)
        except sqlite3.IntegrityError:
            print("❌ Username already exists")
            self.registerSuccess.emit(False)

    @Slot()
    def logout(self):
        print("User  logged out")
        self.loginSuccess.emit(False)  # Navigate back to login screen

    def close_connection(self):
        self.conn.close()

# Backend Class for Instrument Data
class Backend(QObject):
    dataUpdated = Signal()  # Signal to notify UI to refresh
    alarmUpdated = Signal()  # Signal to notify UI when alarms change

    def __init__(self):
        super().__init__()
        self.serial_number = "EC350-12345"
        self.instrument_data = {
            "corrected_volume": 950,
            "gas_pressure": 50,
            "dial_rate": 0.8,
            "gas_temperature": 25,
            "flow_rate": 1000
        }
        self.alarms = []
        self.instrument_power = "Normal"
        self.data_transfer_status = "Active"
        self.firmware_version = "1.2.3"
        self.config_status = "OK"
        self.time_sync = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        self.timer = QTimer()  # ✅ Initialize Timer
        self.timer.timeout.connect(self.update_values)

        # Log file setup
        self.log_file = "system_log.txt"
        with open(self.log_file, "a") as file:
            file.write("==== System Log Initialized ====\n")

    def log_to_file(self, message):
        """ Writes log messages to the system log file using UTF-8 encoding. """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as file:  # ✅ Force UTF-8 encoding
            file.write(f"[{timestamp}] {message}\n")

    @Slot(result=str)
    def get_serial_number(self):
        return self.serial_number

    @Slot(result=str)
    def get_corrected_volume(self):
        return f"{self.instrument_data['corrected_volume']} m³"

    @Slot(result=str)
    def get_gas_pressure(self):
        return f"{self.instrument_data['gas_pressure']} psi"

    @Slot(result=str)
    def get_dial_rate(self):
        return f"{self.instrument_data['dial_rate']} dial/min"

    @Slot(result=str)
    def get_gas_temperature(self):
        return f"{self.instrument_data['gas_temperature']}°C"

    @Slot(result=str)
    def get_flow_rate(self):
        return f"{self.instrument_data['flow_rate']} SCFH"

    @Slot(result=list)
    def get_last_5_alarms(self):
        return [str(alarm) for alarm in self.alarms[-5:]]

    @Slot(result=str)
    def get_instrument_power(self):
        return self.instrument_power

    @Slot(result=str)
    def get_data_transfer_status(self):
        return self.data_transfer_status

    @Slot(result=str)
    def get_firmware_version(self):
        return self.firmware_version

    @Slot(result=str)
    def get_config_status(self):
        return self.config_status

    @Slot(result=str)
    def get_time_sync(self):
        return self.time_sync

    @Slot()
    def update_values(self):
        """ Updates instrument data, logs it, and triggers UI refresh """
        self.instrument_data["corrected_volume"] = random.randint(1000, 2000)
        self.instrument_data["gas_pressure"] = random.randint(5, 1250)
        self.instrument_data["dial_rate"] = round(random.uniform(0.5, 1.5), 2)
        self.instrument_data["gas_temperature"] = random.randint(-40, 80)
        self.instrument_data["flow_rate"] = random.randint(500, 1500)

        self.time_sync = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")

        # Log updated values
        log_message = (
            f"Updated Values -> "
            f"Corrected Volume: {self.instrument_data['corrected_volume']} m³, "
            f"Gas Pressure: {self.instrument_data['gas_pressure']} psi, "
            f"Dial Rate: {self.instrument_data['dial_rate']} dial/min, "
            f"Gas Temperature: {self.instrument_data['gas_temperature']}°C, "
            f"Flow Rate: {self.instrument_data['flow_rate']} SCFH"
        )
        self.log_to_file(log_message)

        # Check for alarms
        old_alarms = self.alarms[:]
        self.check_for_alarms()

        # Emit signals only when necessary
        self.dataUpdated.emit()
        if self.alarms != old_alarms:
            self.alarmUpdated.emit()
            self.log_to_file(f"New Alarms Detected: {', '.join(self.alarms)}")

    @Slot()
    def check_for_alarms(self):
        """ Checks for alarm conditions and updates the alarm list. """
        new_alarms = []

        if self.instrument_data["gas_temperature"] > 30:
            new_alarms.append("🔥 Temperature Too High!")
        elif self.instrument_data["gas_temperature"] < 0:
            new_alarms.append("❄️ Temperature Too Low!")

        if self.instrument_data["flow_rate"] > 1100:
            new_alarms.append("🌊 Flow Rate Too High!")
        elif self.instrument_data["flow_rate"] < 900:
            new_alarms.append("🚰 Flow Rate Too Low!")

        if self.instrument_data["gas_pressure"] > 1000:
            new_alarms.append("⚠️ Pressure Too High!")
        elif self.instrument_data["gas_pressure"] < 100:
            new_alarms.append("⚠️ Pressure Too Low!")

        if self.instrument_data["corrected_volume"] > 1800:
            new_alarms.append("📈 Corrected Volume Too High!")
        elif self.instrument_data["corrected_volume"] < 1200:
            new_alarms.append("📉 Corrected Volume Too Low!")

        if self.instrument_data["dial_rate"] > 1.3:
            new_alarms.append("⚡ Dial Rate Too High!")
        elif self.instrument_data["dial_rate"] < 0.9:
            new_alarms.append("🐢 Dial Rate Too Low!")

        # Update alarms only if they changed
        if self.alarms != new_alarms:
            self.alarms = new_alarms
            print("🔥 Updated Alarms:", self.alarms)
            self.alarmUpdated.emit()
    @Slot()
    def stop_timer(self):
        """ Stops the timer to prevent updates """
        if self.timer.isActive():
            self.timer.stop()
            print("🛑 Timer Stopped: No more updates")

    @Slot()
    def close_connection(self):
        """ Close database connections and stop updating values """
        print("🔴 Closing backend connection...")

        # Stop the timer before exiting
        self.stop_timer()

        # Add any additional cleanup here (e.g., closing database connections)
        print("✅ Backend shut down successfully")

    @Slot()
    def refresh_data(self):
        """ Manually refresh data when button is clicked """
         # Timer to update values every 5 seconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_values)
        self.timer.start(5000)
        self.update_values()

# Main Application
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    auth_backend = AuthBackend()
    backend = Backend()  # Instantiate the Backend class

    engine.rootContext().setContextProperty("authBackend", auth_backend)
    engine.rootContext().setContextProperty("backend", backend)

    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    app.aboutToQuit.connect(auth_backend.close_connection)
    sys.exit(app.exec())