#
# HIDPyToy -
#   2019 Tod E. Kurt, todbot.com
#

from PySide6 import QtWidgets

import sys
import textwrap

# Generate with:  pyside6-uic HIDToyWindow.ui -o HIDToyWindow.py
from .HIDToyWindow import Ui_HIDToyWindow

import hid

class MyHIDToyWindow(Ui_HIDToyWindow):
    def __init__(self):
        self.isConnected = False
        self.device = None

    def connectMySignals(self):
        self.buttonReScan.clicked.connect(self.onReScan)
        self.buttonConnect.clicked.connect(self.onConnect)
        self.buttonSendOutReport.clicked.connect(self.onSendOutReport)
        self.buttonSendFeatureReport.clicked.connect(self.onSendFeatureReport)
        self.buttonGetFeatureReport.clicked.connect(self.onGetFeatureReport)
        self.buttonReadInReport.clicked.connect(self.onReadInReport)

        self.textGetData.ensureCursorVisible()  # make sure scrolls to bottom
        self.textGetData.setStyleSheet('font: 14pt "Courier";')

        self.enableButtons(False)

    def enableButtons(self, state):
        self.buttonSendOutReport.setEnabled(state)
        self.buttonSendFeatureReport.setEnabled(state)
        self.buttonGetFeatureReport.setEnabled(state)
        self.buttonReadInReport.setEnabled(state)

    def close(self):  # not used yet
        self.isConnected = False
        self.enableButtons(False)

    def onReScan(self):
        devs = hid.enumerate()
        self.deviceList.clear()
        # reverse sort by vid, then pid, then usage (with 0 in case libusb w/ no usage)
        devs.sort(key=lambda x: (x['vendor_id'], x['product_id'], x.get('usage', 0)), reverse=True)
        for d in devs:
            s = f"{d['manufacturer_string']} {d['product_string']}  vid/pid:{d['vendor_id']}/{d['product_id']} usage:{d['usage_page']}/{d['usage']} "
            self.deviceList.addItem(s, d['path'])

    def status(self, str):
        print(str)
        self.statusbar.showMessage(str)

    def onConnect(self):
        if self.isConnected:  # already connected, so disconnect
            self.isConnected = False
            self.buttonConnect.setText("Connect")
            self.enableButtons(False)
            if self.device is not None:
                try:
                    self.device.close()
                    self.status("disconnected.")
                except OSError as e:
                    self.status(f"disconnect error: {e}")
            self.device = None
        else:
            hidpath = self.deviceList.currentData()
            if hidpath is None:
                self.status("No device selected — run Rescan first")
                return
            try:
                self.device = hid.device()
                self.device.open_path(hidpath)
                self.isConnected = True
                self.buttonConnect.setText("Disconnect")
                self.enableButtons(True)
                self.status(f"connected to {self.deviceList.currentText()}")
            except OSError as e:
                self.device = None
                self.status(f"connect error: {e}")

    def parseUserBuf(self, bufraw, bufsize):
        buf = [0] * bufsize  # make fixed-size buffer
        try:
            # TODO: replace eval() with ast.literal_eval() for safety
            bufraw = eval(bufraw, {})
            if not (type(bufraw) is list or type(bufraw) is tuple):
                self.status("Parse error: input is not a list")
                return []
            for i, val in enumerate(bufraw):
                if not isinstance(val, int) or not (0 <= val <= 255):
                    self.status(f"Parse error: element {i} ({val!r}) not an int 0-255")
                    return []
        except Exception as e:
            self.status(f"Parse error: {e}")
            return []

        # copy over user-typed bufraw to fixed-size buf
        for i in range(0, min(bufsize, len(bufraw))):
            buf[i] = bufraw[i]

        return buf

    def onSendOutReport(self):
        if not self.isConnected:
            self.status("Not connected")
            return
        bufsize = self.spinSizeOut.value()
        bufraw = self.comboSendData.currentText()
        buf = self.parseUserBuf(bufraw, bufsize)
        if not buf:
            return
        self.comboSendData.addItem(bufraw)
        self.status(f"Sending {bufsize}-byte OUT report:{buf}")
        try:
            self.device.write(buf)
        except OSError as e:
            self.status(f"Send out report error: {e}")

    def onSendFeatureReport(self):
        if not self.isConnected:
            self.status("Not connected")
            return
        bufsize = self.spinSizeOut.value()
        bufraw = self.comboSendData.currentText()
        buf = self.parseUserBuf(bufraw, bufsize)
        if not buf:
            return
        self.comboSendData.addItem(bufraw)
        self.status(f"Sending {bufsize}-byte FEATURE report:{buf}")
        try:
            self.device.send_feature_report(buf)
        except OSError as e:
            self.status(f"Send feature report error: {e}")

    def onGetFeatureReport(self):
        if not self.isConnected:
            self.status("Not connected")
            return
        bufsize = self.spinSizeIn.value()
        report_id = self.spinReportId.value()
        self.status(f"Getting {bufsize}-byte FEATURE report, reportId {report_id}")
        try:
            buf = self.device.get_feature_report(report_id, bufsize)
            bufstr = " ".join('%02x' % v for v in buf)
            self.textGetData.append(f"\n{bufstr}")
        except Exception as e:
            self.status(f"Get FEATURE report error: {e}")

    def onReadInReport(self):
        if not self.isConnected:
            self.status("Not connected")
            return
        bufsize = self.spinSizeIn.value()
        timeout_ms = 200
        self.status(f"Getting {bufsize}-byte IN report...")
        try:
            buf = self.device.read(bufsize, timeout_ms)
            self.status(f"Getting {bufsize}-byte IN report... got {len(buf)} bytes")
            if len(buf) > 0:
                bufstr = " ".join('%02x' % v for v in buf)
                for s in textwrap.wrap(bufstr, width=3*16):
                    self.textGetData.append(s)
                self.textGetData.append("")  # add newline
        except OSError as e:
            self.status(f"Get IN report error: {e}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyHIDToyWindow()
    ui.setupUi(MainWindow)
    ui.connectMySignals()
    ui.onReScan()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
