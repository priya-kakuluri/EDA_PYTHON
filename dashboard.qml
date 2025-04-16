import QtQuick 6.0
import QtQuick.Controls 6.0
import QtQuick.Layouts 6.0
import QtQuick.Controls.Material 6.0

ApplicationWindow {
    visible: true
    width: 1200
    height: 700
    title: "Honeywell | Masterlink"
    ListModel {
        id: alarmModel
    }

    onClosing: {
        console.log("🔴 Closing application...");
        backend.close_connection();  // ✅ Ensure backend disconnects properly
    }
    Connections {
        target: backend
        function onDataUpdated() {
            if (!backend) {
                console.log("❌ Backend not available yet.");
                return;
            }

            console.log("Data updated, refreshing UI...");
            correctedVolumeLabel.text = "Corrected Volume: " + backend.get_corrected_volume();
            gasPressureLabel.text = "Gas Pressure: " + backend.get_gas_pressure();
            dialRateLabel.text = "Dial Rate: " + backend.get_dial_rate();
            gasTemperatureLabel.text = "Gas Temperature: " + backend.get_gas_temperature();
            flowRateLabel.text = "Flow Rate: " + backend.get_flow_rate();
            instrumentPowerLabel.text = backend.get_instrument_power();
            dataTransferLabel.text = backend.get_data_transfer_status();
            firmwareLabel.text = backend.get_firmware_version();
            timeSyncLabel.text = backend.get_time_sync();
            configStatusLabel.text = backend.get_config_status();
        }


        function onAlarmUpdated() {
            if (!backend) {
                console.log("❌ Backend not connected");
                return;
            }

            var newAlarms = backend.get_last_5_alarms();
            console.log("🚨 QML Received Alarms:", newAlarms);

            if (alarmModel.count !== newAlarms.length) {  // ✅ Update only if changed
                alarmModel.clear();  // ✅ Clear old alarms safely

                for (var i = 0; i < newAlarms.length; i++) {
                    alarmModel.append({ alarmText: newAlarms[i] });
                }
            }
            // ✅ Convert the list into a multi-line string
            alarmsLabel.text = "" + newAlarms.join("\n");
            console.log("🔴 Alarm Count:", alarmModel.count); // Debugging UI updates
        }

    }

    Rectangle {
        width: parent.width
        height: parent.height
        color: "#f0f0f0"

        RowLayout {
            anchors.fill: parent

            // Sidebar
            Rectangle {
                width: 180
                Layout.fillHeight: true
                color: "#333"
                ColumnLayout {
                    width: parent.width
                    Layout.fillHeight: true
                    spacing: 10
                    Repeater {
                        model: ["Dashboard", "Site", "View/Edit", "Calibrate", "Read Data", "Live Data", "Administrator"]
                        delegate: Rectangle {
                            width: parent.width
                            height: 50
                            color: "#444"
                            radius: 5
                            Label {
                                anchors.centerIn: parent
                                text: modelData
                                color: "white"
                                font.pixelSize: 16
                            }
                            MouseArea {
                                anchors.fill: parent
                                onClicked: console.log(modelData + " Clicked")
                            }
                        }
                    }
                }
            }

            ColumnLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true

                // Header Bar
                Rectangle {
                    Layout.fillWidth: true
                    height: 50
                    color: "#222"
                    RowLayout {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        Layout.margins: 10
                        spacing: 10
                        Item { Layout.fillWidth: true } // Spacer
                        Label {
                            text: "EC350 Serial No: " + backend.get_serial_number()
                            color: "white"
                            font.pixelSize: 16
                        }
                        Button {
                            text: "Refresh"
                            background: Rectangle { color: "#0080FF"; radius: 5 }
                            contentItem: Label { text: parent.text; color: "white" }
                            onClicked: backend.refresh_data()
                        }
                    }
                }

                // First Row (Instrument Data + Alarms)
                RowLayout {
                    Layout.fillWidth: true
                    Layout.preferredHeight: parent.height * 0.45 // 45% of screen height
                    spacing: 10

                    // Instrument Data
                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Instrument Data"; font.bold: true }
                            Label { id: correctedVolumeLabel; text: "Corrected Volume: " + backend.get_corrected_volume() }
                            Label { id: gasPressureLabel; text: "Gas Pressure: " + backend.get_gas_pressure() }
                            Label { id: dialRateLabel; text: "Dial Rate: " + backend.get_dial_rate() }
                            Label { id: gasTemperatureLabel; text: "Gas Temperature: " + backend.get_gas_temperature() }
                            Label { id: flowRateLabel; text: "Flow Rate: " + backend.get_flow_rate() }
                        }
                    }

                    // Alarms
                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Alarms"; font.bold: true }
                            Label { id: alarmsLabel; font.bold:true;font.pixelSize: 16; text: "" + backend.get_last_5_alarms() }
                            ListView {
                                id: alarmListView
                                width: parent.width
                                height: parent.height - 30
                                model: alarmModel

                                delegate: Rectangle {
                                    width: parent.width
                                    height: 40  // Increased height for visibility
                                    color: "white"
                                    border.color: "gray"
                                    border.width: 1

                                    Label {
                                        text: alarmText  // ✅ Ensure it binds to `alarmText`
                                        color: "red"
                                        font.pixelSize: 16
                                        anchors.centerIn: parent  // ✅ Center text in the box
                                    }
                                }
                            }


                        }
                    }
                }

                // Second Row (Instrument Power, Data Transfer, Firmware, Time Sync, Config Check)
                RowLayout {
                    Layout.fillWidth: true
                    Layout.preferredHeight: parent.height * 0.4 // 40% of screen height
                    spacing: 10

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Instrument Power"; font.bold: true }
                            Label { id: instrumentPowerLabel; text: backend.get_instrument_power() }
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Data Transfer"; font.bold: true }
                            Label { id: dataTransferLabel; text: backend.get_data_transfer_status() }
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Firmware"; font.bold: true }
                            Label { id: firmwareLabel; text: backend.get_firmware_version() }
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Time Sync"; font.bold: true }
                            Label { id: timeSyncLabel; text: backend.get_time_sync() }
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: "white"
                        border.color: "#aaa"
                        radius: 5
                        ColumnLayout {
                            anchors.fill: parent
                            Label { text: "Configuration Check"; font.bold: true }
                            Label { id: configStatusLabel; text: backend.get_config_status() }
                        }
                    }
                }
            }
        }
    }
}
