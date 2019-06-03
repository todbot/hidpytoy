#
# HIDPyToy -
#   2019 Tod E. Kurt, todbot.com 
#

from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore, uic, QtWidgets

import sys
import textwrap

# Generate with:  pyuic5 HIDToyWindow.ui -o HIDToyWindow.py
from HIDToyWindow import Ui_HIDToyWindow

import hid

class MyHIDToyWindow(Ui_HIDToyWindow):
    def __init__(self):
        self.isConnected = False

    def connectMySignals(self):
        self.buttonReScan.clicked.connect(self.onReScan)
        self.buttonConnect.clicked.connect(self.onConnect)
        self.buttonSendOutReport.clicked.connect(self.onSendOutReport)
        self.buttonSendFeatureReport.clicked.connect(self.onSendFeatureReport)
        self.buttonGetFeatureReport.clicked.connect(self.onGetFeatureReport)
        self.buttonReadInReport.clicked.connect(self.onReadInReport)
        #self.textSendData.returnPressed.connect(self.onSendReport)
        self.comboSendData.activated.connect(self.onComboActivated)

        self.textGetData.ensureCursorVisible()  # make sure scrolls to bottom
        self.textGetData.setStyleSheet('font: 14pt "Courier";')

        self.enableButtons(False)

    def enableButtons(self,state):
        self.buttonSendOutReport.setEnabled(state)
        self.buttonSendFeatureReport.setEnabled(state)
        self.buttonGetFeatureReport.setEnabled(state)
        self.buttonReadInReport.setEnabled(state)

    def close(self): # not used yet
        self.isConnected = False
        self.enableButtons(False)

    def onReScan(self):
        devs = hid.enumerate()
        self.deviceList.clear()
        # revese sort by vid, then pid, then usage (with 0 in case libusb w/ no usage)
        devs.sort( key=lambda x: (x['vendor_id'],x['product_id'],x.get('usage',0)), reverse=True )
        for d in devs:
           # str = f"vid/pid:{d['vendor_id']}/{d['product_id']} usage:{d['usage_page']}/{d['usage']} {d['manufacturer_string']} {d['product_string']}"
            str = f"{d['manufacturer_string']} {d['product_string']}  vid/pid:{d['vendor_id']}/{d['product_id']} usage:{d['usage_page']}/{d['usage']} "
            self.deviceList.addItem(str,d['path'])

    def status(self,str):
        print(str)
        self.statusbar.showMessage(str)

    def onConnect(self):
        print("onConnect: ", self.isConnected, self.deviceList.currentText(), self.deviceList.currentData())
        if self.isConnected:  # already connected, so disconnect
            self.isConnected = False
            print("disconnecting...")
            self.buttonConnect.setText("Connect")
            self.enableButtons(False)
            try:
                self.device.close()
                self.status(f"disconnected.")
            except OSError as e:
                self.status(f"disconnect error: {e}")
        else:
            self.buttonConnect.setText("Disconnect")
            self.enableButtons(True)
            try:
                self.device = hid.device()
                hidpath = self.deviceList.currentData()
                self.device.open_path(hidpath)
                self.isConnected = True
                self.status(f"connected to {self.deviceList.currentText()}")
            except OSError as e:
                self.status(f"connect error: {e}")

    def parseUserBuf(self,bufraw,bufsize):
        # do sanity checks on user-typed bufraw
        buf = [0] * bufsize  # make fixed-size buffer
        try:
            bufraw = eval( bufraw, {}) # safer eval
            print('bufraw:',bufraw)
            if type(bufraw) is list or type(bufraw) is tuple:
                for i in range(0,len(buf)):
                    if type(buf[i]) is str:
                        buf[i] = 0
            else:
                self.status("Parse error: input is not a list")
        except Exception as e:
            self.status(f"Parse error: {e}")
            return []

        # copy over user-typed bufraw to fixed-size buf
        for i in range(0, min(bufsize,len(bufraw))):
            buf[i] = bufraw[i]

        return buf

    def onComboActivated(self):
        print(f"comboActivated! currentText {self.comboSendData.currentText()}")
        # we don't need this do we?

    def onSendOutReport(self):
        bufsize = self.spinSizeOut.value()
        bufraw = self.comboSendData.currentText()
        buf = self.parseUserBuf(bufraw, bufsize)
        if buf:
            self.comboSendData.addItem(bufraw)

        self.status(f"Sending {bufsize}-byte OUT report:{buf}")
        try:
            self.device.write(buf)
        except OSError as e:
            self.status(f"Send out report error: {e}")

    def onSendFeatureReport(self):
        bufsize = self.spinSizeOut.value()
        bufraw = self.comboSendData.currentText()
        buf = self.parseUserBuf(bufraw, bufsize)
        if buf:
            self.comboSendData.addItem(bufraw)

        self.status(f"Sending {bufsize}-byte FEATURE report:{buf}")
        try:
            self.device.send_feature_report(buf)
        except OSError as e:
            self.status(f"Send feature report error: {e}")

    def onGetFeatureReport(self):
        bufsize = self.spinSizeIn.value()
        report_id = self.spinReportId.value()

        self.status(f"Getting {bufsize}-byte FEATURE report, reportId {report_id}")
        try:
            buf = self.device.get_feature_report(report_id,bufsize)
            print('buf',buf)
            bufstr = " ".join('%02x' % v for v in buf)
            self.textGetData.append(f"\n{bufstr}")
        except Exception as e:
            self.status(f"Get FEATURE report error: {e}")

    def onReadInReport(self):
        bufsize = self.spinSizeIn.value()
        timeout_ms = 200
        self.status(f"Getting {bufsize}-byte IN report...")
        try:
            buf = self.device.read(bufsize, timeout_ms)
            self.status(f"Getting {bufsize}-byte IN report... got {len(buf)} bytes")
            if len(buf) > 0:
                bufstr = " ".join('%02x' % v for v in buf)
                print('bufstr',bufstr)
                for s in textwrap.wrap(bufstr, width=3*16):
                    print(f"s={s}")
                    self.textGetData.append(s)
                self.textGetData.append("") # add newline
        except OSError as e:
            self.status(f"Get IN report error: {e}")


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyHIDToyWindow()
    ui.setupUi(MainWindow)
    ui.connectMySignals()
    ui.onReScan()
    MainWindow.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
