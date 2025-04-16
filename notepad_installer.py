from pywinauto import Application
import time

# Path to the Notepad++ installer
npp_installer_path = r"C:\Users\Admin\Downloads\npp.8.7.7.Installer.x64.exe"

# Start the installer
app = Application().start(npp_installer_path)

# Wait for the "Installer Language" dialog
time.sleep(2)
dlg_lang = app.window(title_re="Installer Language")
dlg_lang.OK.click()  # Click "OK" to select default English
print("Language selected successfully.")

# Wait for the "Welcome to Notepad++ Setup" window
time.sleep(2)
dlg_setup = app.window(title_re="Notepad\+\+.*Setup")
dlg_setup.Next.click()
print("Clicked 'Next' on the setup wizard.")

# Wait for the "License Agreement" window
time.sleep(2)
dlg_license = app.window(title_re="Notepad\+\+.*Setup")
dlg_license.IAgree.click()
print("Accepted the license agreement and proceeded with installation.")

# Wait for the "Choose Install Location" window
time.sleep(2)
dlg_install_location = app.window(title_re="Notepad\+\+.*Setup")
dlg_install_location.Next.click()
print("Proceeding with the default install location.")

# Wait for the "Choose Components" window
time.sleep(2)
dlg_components = app.window(title_re="Notepad\+\+.*Setup")
dlg_components.Next.click()
print("Proceeding with default components selection.")

# Wait for the "Choose Components" window (with checkbox)
time.sleep(2)
dlg_components = app.window(title_re="Notepad\+\+.*Setup")

# Debugging: Print available controls
print("Available elements in 'Choose Components':")
dlg_components.print_control_identifiers()

# Try selecting the "Create Shortcut on Desktop" checkbox
try:
    chkbox = dlg_components.child_window(title="Create Shortcut on Desktop", class_name="Button").wrapper_object()

    # Ensure it's a checkbox and check its state
    if chkbox.get_check_state() == 0:  # 0 = Unchecked, 1 = Checked
        chkbox.click()
        print("Checked 'Create Shortcut on Desktop'.")
    else:
        print("'Create Shortcut on Desktop' was already checked.")
except Exception as e:
    print(f"Error selecting the checkbox: {e}")

# Click the "Install" button
dlg_components.Install.click()
print("Installation started.")

time.sleep(5)  # Adjust if needed

# Wait for the "Installation Complete" window
dlg_finish = app.window(title_re="Notepad\+\+.*Setup")

# Click the "Finish" button
dlg_finish.Finish.click()
print("Installation completed successfully.")