#from fbs_runtime.application_context import ApplicationContext

from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore, uic, QtWidgets
#from PyQt5.QtCore import pyqtSlot

import sys

# Generate with:  pyuic5 HIDToyWindow.ui -o HIDToyWindow.py
from HIDToyWindow import Ui_HIDToyWindow

# from blink1.blink1 import Blink1
import hid

class MyHIDToyWindow(Ui_HIDToyWindow):
    def __init__(self):
        self.isConnected = False
        self.otherValue = "todbot"

    def connectMySignals(self):
        self.buttonReScan.clicked.connect(self.onReScan)
        self.buttonConnect.clicked.connect(self.onConnect)
        self.buttonSendReport.clicked.connect(self.onSendReport)
        self.buttonGetReport.clicked.connect(self.onGetReport)

        self.buttonSendReport.setEnabled(False)
        self.buttonGetReport.setEnabled(False)

    def onReScan(self):
        devs = hid.enumerate()
        #devstrs = list(map(lambda d:d.get('serial_number'), devs))
        self.deviceList.clear()
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
            self.buttonSendReport.setEnabled(False)
            self.buttonGetReport.setEnabled(False)
            try:
                self.device.close()
                self.status(f"disconnected.")
            except OSError as e:
                self.status(f"disconnect error: {e}")
        else:
            self.buttonConnect.setText("Disconnect")
            self.buttonSendReport.setEnabled(True)
            self.buttonGetReport.setEnabled(True)
            try:
                self.device = hid.device()
                hidpath = self.deviceList.currentData()
                self.device.open_path(hidpath)
                self.isConnected = True
                self.status(f"connected to {self.deviceList.currentText()}")
            except OSError as e:
                self.status(f"connect error: {e}")

    def onSendReport(self):
        print("SendReport!")
        self.statusbar.showMessage("hello!")

        try:
            buf = eval( self.textSendData.text(), {})
            print('buf:',buf)
            if type(buf) is list or type(buf) is tuple:
                for i in range(0,len(buf)):
                    if type(buf[i]) is str:
                        buf[i] = 0
            else:
                print("ERROR")
        except Exception as e:
            self.status(f"Parse error: {e}")
            return

        #buf = [1, 99, 255,0,255,0,0,0,0]
        if self.buttonOutTypeFeature.isChecked():
            self.status(f"Sending FEATURE report:{buf}")
            try:
                self.device.send_feature_report(buf)
            except OSError as e:
                self.status(f"Send feature report error: {e}")
        else:
            self.status(f"Sending OUT report:{buf}")
            try:
                self.device.write(buf)
            except OSError as e:
                self.status(f"Send out report error: {e}")

    def onGetReport(self):
        print("GetReport!")
        bufsize = self.spinSizeIn.value()
        report_id = self.spinReportId.value()

        if self.buttonInTypeFeature.isChecked():
            self.status(f"Getting FEATURE report of {bufsize} bytes on reportId {report_id}")
            try:
                buf = self.device.get_feature_report(report_id,bufsize)
                print('buf',buf)
                print("read: " + ",".join('0x%02x' % v for v in buf))
                bufstr = ",".join('0x%02x' % v for v in buf)
                self.textGetData.append(f"\n{bufstr}")
            except OSError as e:
                self.status(f"Send feature report error: {e}")
        else:
            self.status("Getting OUT report of {bufsize} bytes on reportId {report_id}")
            try:
                buf = self.device.read(buf)
            except OSError as e:
                self.status(f"Send feature report error: {e}")


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
