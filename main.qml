import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 1200
    height: 700
    title: "Authentication"

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: loginPage
    }

    // 🔹 Popup Dialog for Errors & Notifications
    Dialog {
        id: messageDialog
        title: "Notification"
        modal: true
        width: 300
        height: 120
        x: (parent.width - width) / 2
        y: 20

        Column {
            anchors.fill: parent
            spacing: 10

            Text {
                id: dialogText
                text: ""
                font.pixelSize: 16
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        standardButtons: Dialog.Ok
        onAccepted: {
            messageDialog.close();
            if (dialogText.text === "✅ Login Successful!") {
                stackView.push(dashboardPage);  // Navigate to Dashboard
            }
        }
    }

    // 🔹 Login Page
    Component {
        id: loginPage

        Rectangle {
            color: "#f0f0f0"
            width: parent.width
            height: parent.height

            Column {
                anchors.centerIn: parent
                spacing: 15

                Text { text: "Honeywell"; font.pixelSize: 24; font.bold: true; anchors.horizontalCenter: parent.horizontalCenter }
                Text { text: "MasterLink"; font.pixelSize: 20; anchors.horizontalCenter: parent.horizontalCenter }
                Text { text: "MasterLinkR515.1"; font.pixelSize: 16; anchors.horizontalCenter: parent.horizontalCenter }
                Text { text: "Please login to get started"; font.pixelSize: 14; anchors.horizontalCenter: parent.horizontalCenter }

                TextField { id: loginUsername; placeholderText: "Username"; width: 200; anchors.horizontalCenter: parent.horizontalCenter }
                TextField { id: loginPassword; placeholderText: "Password"; echoMode: TextInput.Password; width: 200; anchors.horizontalCenter: parent.horizontalCenter }

                Button {
                    text: "Login"
                    width: 200
                    anchors.horizontalCenter: parent.horizontalCenter
                    onClicked: {
                        if (loginUsername.text === "" || loginPassword.text === "") {
                            dialogText.text = "⚠️ Please fill all fields!";
                            messageDialog.open();
                        } else {
                            authBackend.login(loginUsername.text, loginPassword.text);
                        }
                    }
                }

                Button {
                    text: "Signup"
                    width: 200
                    anchors.horizontalCenter: parent.horizontalCenter
                    onClicked: stackView.push(signupPage)
                }
            }
        }
    }

    Component {
    id: signupPage

    Rectangle {
        color: "#f0f0f0"
        width: parent.width
        height: parent.height

        ColumnLayout {
            anchors.centerIn: parent
            spacing: 20

            // 🔹 Title
            Label {
                text: "Register"
                font.pixelSize: 24
                font.bold: true
                Layout.alignment: Qt.AlignHCenter
            }

            // 🔹 First Row (Username & Key)
            RowLayout {
                Layout.alignment: Qt.AlignHCenter
                spacing: 15

                ColumnLayout {
                    spacing: 5
                    Label { text: "Username"; font.pixelSize: 14 }
                    TextField {
                        id: signupUsername
                        placeholderText: "Enter Username"
                        width: 200
                    }
                }

                ColumnLayout {
                    spacing: 5
                    Label { text: "Key"; font.pixelSize: 14 }
                    TextField {
                        id: keyField
                        placeholderText: "Enter key"
                        width: 200
                    }
                }
            }

            // 🔹 Second Row (Password & Confirm Password)
            RowLayout {
                Layout.alignment: Qt.AlignHCenter
                spacing: 15

                ColumnLayout {
                    spacing: 5
                    Label { text: "Password"; font.pixelSize: 14 }
                    TextField {
                        id: signupPassword
                        placeholderText: "Enter Password"
                        echoMode: TextInput.Password
                        width: 200
                    }
                }

                ColumnLayout {
                    spacing: 5
                    Label { text: "Confirm Password"; font.pixelSize: 14 }
                    TextField {
                        id: confirmPassword
                        placeholderText: "Confirm Password"
                        echoMode: TextInput.Password
                        width: 200
                    }
                }
            }

            // 🔹 Button Row (Register & Back)
            RowLayout {
                Layout.alignment: Qt.AlignHCenter
                spacing: 20

                Button {
                    text: "Register"
                    width: 120
                    onClicked: {
                        if (signupUsername.text === "" || keyField.text === "" || signupPassword.text === "" || confirmPassword.text === "") {
                            dialogText.text = "⚠️ Please fill all fields!";
                            messageDialog.open();
                        } else if (signupPassword.text !== confirmPassword.text) {
                            dialogText.text = "⚠️ Passwords do not match!";
                            messageDialog.open();
                        } else {
                            authBackend.register(signupUsername.text, signupPassword.text);
                        }
                    }
                }

                Button {
                    text: "Back"
                    width: 120
                    onClicked: stackView.pop()
                }
            }
        }
    }
}


    Component {
        id: dashboardPage

        Rectangle {
            width: parent.width
            height: parent.height
            color: "#F5F5F5"

            RowLayout {
                anchors.fill: parent
                spacing: 10

                // Sidebar
                Rectangle {
                    width: 200
                    height: parent.height
                    color: "#333"

                    ColumnLayout {
                        anchors.fill: parent
                        spacing: 20
                        Label { text: " Dashboard"; color: "white"; font.pixelSize: 18 }
                        Label { text: " Site"; color: "white"; font.pixelSize: 16 }
                        Label { text: " View/Edit"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Calibrate"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Read Data"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Live Data"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Administer"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Setting"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Security"; color: "white"; font.pixelSize: 16 }
                        Label { text: " Update"; color: "white"; font.pixelSize: 16 }
                    }
                }

                // Main Content
                ColumnLayout {
                    anchors.left: parent.left
                    anchors.leftMargin: 220
                    anchors.top: parent.top
                    anchors.topMargin: 20
                    width: parent.width - 240
                    spacing: 20

                    Label {
                        text: "Site Management"
                        font.pixelSize: 18
                        font.bold: true
                    }

                    RowLayout {
                        spacing: 20
                        
                        Image {
                            source: "EC350.png"
                            width: 100
                            height: 100
                            fillMode: Image.PreserveAspectFit
                            smooth: true
                        }
                        
                        ColumnLayout {
                            Label { text: "Location 1"; font.pixelSize: 16 }
                            Label { text: "EC350"; font.pixelSize: 16 }
                        }
                        
                        ColumnLayout {
                            Label { text: "Connect"; font.pixelSize: 16; font.bold: true }
                            RowLayout {
                                spacing: 10
                                Button { text: "Modem" }
                                Button {
                                text: "Serial"
                                contentItem: Text {
                                    text: "Serial"
                                    color: "#0080FF"
                                    font.pixelSize: 16
                                    font.bold: true
                                    horizontalAlignment: Text.AlignHCenter
                                    verticalAlignment: Text.AlignVCenter
                                }
                            }
                                Button { text: "Internet" }
                                Button {
                                text: "IrDA"
                                contentItem: Text {
                                    text: "IrDA"
                                    color: "#0080FF"
                                    font.pixelSize: 16
                                    font.bold: true
                                    horizontalAlignment: Text.AlignHCenter
                                    verticalAlignment: Text.AlignVCenter
                                }
                            }
                            }
                        }
                    }
                    
                    Label {
                        text: "Stand Alone"
                        font.pixelSize: 16
                        font.bold: true
                        color: "#808080"
                    }
                    
                    Rectangle {
                        width: parent.width - 240
                        height: 2
                        color: "gray"
                    }

                    // Two-column Layout
                    RowLayout {
                        spacing: 20

                        ColumnLayout {
                            RowLayout {
                                Label { text: "Instrument Type:" }
                                ComboBox { model: ["EC350"] }
                            }
                            RowLayout {
                                Label { text: "Site Name:" }
                                Label { text: "Location1" }
                            }
                            RowLayout {
                                Label { text: "Site Location:" }
                                Label { text: "Hyd" }
                            }
                            RowLayout {
                                Label { text: "Site ID:" }
                                Label { text: "012345" }
                            }
                            RowLayout {
                                Label { text: "Site ID 2:" }
                                Label { text: "023456" }
                            }
                            RowLayout {
                                Label { text: "User ID:" }
                                Label { text: "0" }
                            }
                            RowLayout {
                                Label { text: "Instrument Access Code:" }
                                Label { text: "*****" }
                            }
                        }

                        ColumnLayout {
                            RowLayout {
                                Label { text: "Internet:" }
                                ComboBox { model: ["None"] }
                            }
                            RowLayout {
                                Label { text: "Site Phone:" }
                                TextField {}
                            }
                            RowLayout {
                                Label { text: "SSL Private Key:" }
                                TextField {}
                            }
                            RowLayout {
                                Label { text: "Modem ID:" }
                                Label { text: "0" }
                            }
                            RowLayout {
                                Label { text: "Modem Port:" }
                                ComboBox { model: ["None"] }
                            }
                            RowLayout {
                                Label { text: "Post Modem Command:" }
                                TextField {}
                            }
                        }
                    }
                }

                // Save and Cancel Buttons
                Row {
                    anchors.bottom: parent.bottom
                    anchors.right: parent.right
                    anchors.margins: 20
                    spacing: 10

                    Button {
                        text: "Save"
                        width: 100
                        height: 40
                        background: Rectangle {
                            color: "#0080FF"
                            radius: 5
                        }
                        contentItem: Text {
                            text: "Save"
                            color: "white"
                            font.pixelSize: 16
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                        onClicked: {
                            stackView.push("dashboard.qml")  // Navigate to dashboard.qml
                            
                        }
                    }


                    Button {
                        text: "Cancel"
                        width: 100
                        height: 40
                        background: Rectangle {
                            color: "#0080FF"
                            radius: 5
                        }
                        contentItem: Text {
                            text: "Cancel"
                            color: "white"
                            font.pixelSize: 16
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                        onClicked: stackView.pop()  // Go back to Login Page
                    }
                }
            }
        }
    }
    
    // 🔹 Connecting Backend Signals to Show Popups
    Connections {
        target: authBackend

        function onLoginSuccess(success) {
            dialogText.text = success ? "✅ Login Successful!" : "❌ Invalid Credentials!";
            messageDialog.open();
        }

        function onRegisterSuccess(success) {
            dialogText.text = success ? "✅ Registration Successful!" : "❌ Username already exists!";
            messageDialog.open();
        }
    }

    
}