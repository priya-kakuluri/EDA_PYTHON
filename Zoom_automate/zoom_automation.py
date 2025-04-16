from pywinauto.application import Application
import time
from test import my_password

Zoom_app=Application(backend='uia').start(r'C:\Users\Admin\Downloads\ZoomInstallerFull').connect(title='Zoom Workplace',timeout=30)
Zoom_app.ZoomWorkplace.print_control_identifiers()

SignIn=Zoom_app.ZoomWorkplace.child_window(title="Sign in", control_type="Button").wrapper_object()
SignIn.click_input()
time.sleep(1)

Zoom_app.ZoomWorkplace.print_control_identifiers()
email_box=zoom_app.ZoomWorkplace.child_window(title="Enter your email", control_type="Edit").wrapper_object()
email_box.click_input()
email_box.type_keys("^a{BACKSPACE")
email_box.type_keys("vishnupriya@gmail.com")
time.sleep(1)


password=zoom_app.ZoomWorkplace.child_window(title="Enter your password", control_type="Edit").wrapper.object()
password.click_input()
password.type_keys("^a{BACKSPACE")
password.type_keys(my_password)
time.sleep(1)


sign_in=zoom_app.ZoomWorkplace.child_window(title="Sign in", control_type="Button").wrapper.object()
sign_in.click_input()
time.sleep(1)

Zoom_app.ZoomWorkplace.print_control_identifiers()

