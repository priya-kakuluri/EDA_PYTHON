from pywinauto import Application
import time

exe_path = r"C:\Users\Admin\PycharmProjects\Pywin_testing\dist\AuthApp.exe"

# Start the app
app = Application(backend="win32").start(exe_path)

# Wait for UI to load
time.sleep(5)

# Attach to process instead of searching by window title
app = Application(backend="win32").connect(path=exe_path)

# List all windows again
print("Available Windows:", app.windows())
