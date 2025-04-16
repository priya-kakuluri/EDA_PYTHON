from pywinauto.application import Application

app=Application(backend='uia').start('notepad.exe').connect(title='Untitled - Notepad',timeout=20)
app.UntitledNotepad.print_control_identifiers()
textEditor=app.UnititledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
textEditor.type_keys("Hi How are you",with_spaces=True)
fileMenu=app.UntitledNotepad.child_window(title="File", control_type="MenuItem")
fileMenu.click_input()
# app.UntitledNotepad.print_control_identifiers()
# newWindow=app.UntitledNotepad.child_window(title="New Window	Ctrl+Shift+N", auto_id="8", control_type="MenuItem").wrapper_object()
# newWindow.click_input()
close=app.UntitledNotepad.child_window(title="Close", control_type="Button").wrapper_object()
close.click_input()
# app.UntitledNotepad.print_control_identifiers()

dontSave=app.UntitledNotepad.child_window(title="Don't Save", auto_id="CommandButton_7", control_type="Button").wrapper_object()
dontSave.click()