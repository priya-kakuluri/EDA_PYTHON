import pytest
import time
from pywinauto import Application
import os

# ✅ Check if the executable exists before running tests
print(os.path.exists(r"C:\Users\Admin\Downloads\final dashboard\dist\MyApp.exe"))

# Define application path
EXE_PATH = r"C:\Users\Admin\Downloads\final dashboard\dist\MyApp.exe"

@pytest.fixture(scope="module")
def app():
    """Setup and return the application instance."""
    application = Application(backend="uia").start(EXE_PATH)
    time.sleep(8)  # Allow time for the application to load
    yield application
    application.kill()  # Ensure the application closes after tests

@pytest.fixture
def main_window(app):
    """Attach to the Authentication window."""
    app = app.connect(path=EXE_PATH)
    window = app.window(title="Authentication")
    assert window.exists(), "❌ Authentication window not found!"
    return window

def wait_for_popup(main_window, timeout=10):
    """Wait for a popup to appear after clicking a button."""
    for _ in range(timeout):
        popups = main_window.descendants(control_type="Window")
        if popups:
            return popups[0]  # Return the first detected popup
        time.sleep(1)  # Wait 1 sec before rechecking
    return None  # Return None if no popup appears

def test_signup(main_window):
    """Test the Signup functionality."""
    print("Running Signup Test...")

    name = "new user2"
    passwd = "securekey@1232"

    # Click Signup button
    signup_btn = main_window.child_window(title="Signup", control_type="Button")
    assert signup_btn.exists(), "❌ Signup button not found!"
    signup_btn.click_input()
    time.sleep(2)

    # Detect Signup Form fields
    signup_fields = main_window.descendants(control_type="Edit")
    assert len(signup_fields) >= 3, "❌ Signup form fields not found!"

    # Fill in the form
    signup_fields[0].type_keys(name)  # Name
    signup_fields[1].type_keys("1234")  # Email
    signup_fields[2].type_keys(passwd)  # Password
    signup_fields[3].type_keys(passwd)  # Confirm Password

    # Click Register button
    register_btn = main_window.child_window(title="Register", control_type="Button")
    assert register_btn.exists(), "❌ Register button not found!"
    register_btn.click_input()

    # Handle Popup and Validate Message
    popup = wait_for_popup(main_window)
    assert popup, "❌ No popup detected after Signup!"
    
    message = popup.window_text()
    print(f"✅ Signup Popup detected! Message: {message}")

    if "Registration Successful" in message:
        print("✅ Registration was successful.")
    elif "Username already exist" in message:
        print("⚠️ User is already registered.")
    else:
        print("❌ Unexpected Signup popup message!")

    # Click OK in popup
    ok_buttons = popup.descendants(control_type="Button")
    assert ok_buttons, "❌ OK button not found in Signup popup!"
    ok_buttons[0].click_input()
    print("✅ Signup popup closed.")

    # Click Back button after signup
    back_btn = main_window.child_window(title="Back", control_type="Button")
    assert back_btn.exists(), "❌ Back button not found!"
    back_btn.click_input()
    print("✅ Back button clicked, returning to Login page.")

    time.sleep(2)  # Allow time for UI to update

def test_login(main_window):
    """Test the Login functionality."""
    print("Running Login Test...")

    name = "new user2"
    passwd = "securekey@1232"

    # Get login fields
    text_fields = main_window.descendants(control_type="Edit")
    assert len(text_fields) >= 2, "❌ Login form fields not found!"

    # Enter login details
    text_fields[0].type_keys(name)  # Username
    text_fields[1].type_keys(passwd)  # Password

    # Click Login button
    login_btn = main_window.child_window(title="Login", control_type="Button")
    assert login_btn.exists(), "❌ Login button not found!"
    login_btn.click_input()

    # Handle Login Popup and Validate Message
    popup = wait_for_popup(main_window)
    assert popup, "❌ No popup detected after Login!"
    
    message = popup.window_text()
    print(f"✅ Login Popup detected! Message: {message}")

    if "Login Successful" in message:
        print("✅ Login was successful.")
    elif "Invalid Credentials" in message:
        print("❌ Invalid username or password!")
    else:
        print("❌ Unexpected Login popup message!")

    # Click OK in popup
    ok_buttons = popup.descendants(control_type="Button")
    assert ok_buttons, "❌ OK button not found in Login popup!"
    ok_buttons[0].click_input()
    print("✅ Login popup closed.")

def wait_for_window(app, title, timeout=10):
    """Wait for a window with a given title and return it as a Pywinauto window object."""
    for _ in range(timeout):
        windows = app.windows()
        for win in windows:
            if title in win.window_text():
                return app.window(handle=win.handle)  # Convert to Application window
        time.sleep(1)  # Wait and retry
    return None

def test_site_management(main_window):
    """Test navigating to Site Management, saving, refreshing, and closing."""
    print("🔹 Navigating to Site Management...")

    # ✅ Click Save button in Site Management
    save_btn = main_window.child_window(title="Save", control_type="Button")
    assert save_btn.exists(), "❌ Save button not found!"
    save_btn.click_input()
    print("✅ Save button clicked. Navigating to Main Dashboard...")

    # ✅ Wait for "Honeywell | Masterlink" to load as a Pywinauto window
    main_dashboard = wait_for_window(main_window.app, "Honeywell | Masterlink", timeout=10)
    assert main_dashboard, "❌ Main dashboard title is incorrect!"
    print("✅ Main Dashboard loaded successfully!")

    # ✅ Click Refresh button
    refresh_btn = main_dashboard.child_window(title="Refresh", control_type="Button")
    assert refresh_btn.exists(), "❌ Refresh button not found!"
    refresh_btn.click_input()
    print("✅ Refresh button clicked.")

    # ✅ Wait for 10 seconds in Main Dashboard
    print("⏳ Waiting for 10 seconds in the Main Dashboard...")
    time.sleep(20)

    # ✅ Close Main Dashboard
    close_btn = main_dashboard.child_window(title="Close", control_type="Button")
    assert close_btn.exists(), "❌ Close button not found!"
    close_btn.click_input()
    print("✅ Main Dashboard closed.")

    # ✅ Return to Site Management
    print("✅ Navigating back to Site Management after closing Main Dashboard.")


def test_close_app(main_window):
    """Test closing the application using the top-right 'X' close button."""
    print("Closing the application...")

    # ✅ Close the Main Dashboard Window
    try:
        main_window.close()  # Simulates clicking the "X" button
        print("✅ Main Dashboard closed.")
    except Exception as e:
        print(f"⚠️ Failed to close Main Dashboard: {e}")

    time.sleep(3)  # Allow some time for UI updates

    # ✅ Check if Site Management is still open
    site_mgmt = main_window.app.windows()
    site_mgmt_window = None

    for win in site_mgmt:
        if "Site Management" in win.window_text():  # Adjust the title based on actual Site Management window
            site_mgmt_window = main_window.app.window(handle=win.handle)
            break

    if site_mgmt_window:
        print("✅ Site Management is still open, closing it now...")

        # ✅ Close Site Management Window using the 'X' button
        try:
            site_mgmt_window.close()
            print("✅ Site Management closed.")
        except Exception as e:
            print(f"⚠️ Failed to close Site Management: {e}")
    else:
        print("⚠️ Site Management window not found. It may have been closed already.")