from pywinauto.application import Application
import time

zoom_path = r"C:\Users\Admin\Downloads\ZoomInstallerFull"
ZOOM_EMAIL = "your_email@example.com"
ZOOM_PASSWORD = "your_password"

try:
    # Start Zoom application
    app = Application(backend="uia").start(zoom_path)
    time.sleep(10)

    # Connect to the main Zoom window
    zoom_window = app.window(title_re=".*Zoom.*")

    # Click the "Sign In" button
    sign_in_button = zoom_window.child_window(title="Sign In", control_type="Button")
    sign_in_button.click_input()
    time.sleep(5)

    # Connect to the login window
    login_window = app.window(title_re=".*Zoom.*")

    # Enter email
    email_field = login_window.child_window(auto_id="inputEmail", control_type="Edit")
    email_field.type_keys(ZOOM_EMAIL, with_spaces=True)

    # Enter password
    password_field = login_window.child_window(auto_id="inputPassword", control_type="Edit")
    password_field.type_keys(ZOOM_PASSWORD, with_spaces=True)

    # Click the "Sign In" button
    sign_in_submit_button = login_window.child_window(title="Sign In", control_type="Button")
    sign_in_submit_button.click_input()

    # Wait for the login process to complete
    time.sleep(10)
    print("Login process completed.")

except Exception as e:
    print(f"An error occurred: {e}")