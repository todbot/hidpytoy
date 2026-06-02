# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HIDToyWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_HIDToyWindow(object):
    def setupUi(self, HIDToyWindow):
        if not HIDToyWindow.objectName():
            HIDToyWindow.setObjectName(u"HIDToyWindow")
        HIDToyWindow.resize(700, 600)
        HIDToyWindow.setMinimumSize(QSize(700, 600))
        HIDToyWindow.setMaximumSize(QSize(700, 600))
        self.centralwidget = QWidget(HIDToyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boxReceiveData = QGroupBox(self.centralwidget)
        self.boxReceiveData.setObjectName(u"boxReceiveData")
        self.boxReceiveData.setGeometry(QRect(20, 280, 661, 261))
        self.verticalLayoutWidget_2 = QWidget(self.boxReceiveData)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 641, 211))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonReadInReport = QPushButton(self.verticalLayoutWidget_2)
        self.buttonReadInReport.setObjectName(u"buttonReadInReport")

        self.horizontalLayout_5.addWidget(self.buttonReadInReport)

        self.buttonGetFeatureReport = QPushButton(self.verticalLayoutWidget_2)
        self.buttonGetFeatureReport.setObjectName(u"buttonGetFeatureReport")

        self.horizontalLayout_5.addWidget(self.buttonGetFeatureReport)

        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.spinReportId = QSpinBox(self.verticalLayoutWidget_2)
        self.spinReportId.setObjectName(u"spinReportId")
        sizePolicy.setHeightForWidth(self.spinReportId.sizePolicy().hasHeightForWidth())
        self.spinReportId.setSizePolicy(sizePolicy)
        self.spinReportId.setMaximum(255)
        self.spinReportId.setValue(0)

        self.horizontalLayout_5.addWidget(self.spinReportId)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.spinSizeIn = QSpinBox(self.verticalLayoutWidget_2)
        self.spinSizeIn.setObjectName(u"spinSizeIn")
        sizePolicy.setHeightForWidth(self.spinSizeIn.sizePolicy().hasHeightForWidth())
        self.spinSizeIn.setSizePolicy(sizePolicy)
        self.spinSizeIn.setMinimum(1)
        self.spinSizeIn.setMaximum(128)
        self.spinSizeIn.setValue(64)

        self.horizontalLayout_5.addWidget(self.spinSizeIn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.textGetData = QTextEdit(self.verticalLayoutWidget_2)
        self.textGetData.setObjectName(u"textGetData")

        self.verticalLayout_4.addWidget(self.textGetData)

        self.boxSendData = QGroupBox(self.centralwidget)
        self.boxSendData.setObjectName(u"boxSendData")
        self.boxSendData.setGeometry(QRect(20, 140, 661, 141))
        self.verticalLayoutWidget_3 = QWidget(self.boxSendData)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 30, 641, 101))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.comboSendData = QComboBox(self.verticalLayoutWidget_3)
        self.comboSendData.setObjectName(u"comboSendData")
        self.comboSendData.setEditable(True)
        self.comboSendData.setInsertPolicy(QComboBox.InsertAtTop)

        self.verticalLayout_3.addWidget(self.comboSendData)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonSendOutReport = QPushButton(self.verticalLayoutWidget_3)
        self.buttonSendOutReport.setObjectName(u"buttonSendOutReport")
        self.buttonSendOutReport.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.buttonSendOutReport)

        self.buttonSendFeatureReport = QPushButton(self.verticalLayoutWidget_3)
        self.buttonSendFeatureReport.setObjectName(u"buttonSendFeatureReport")

        self.horizontalLayout_2.addWidget(self.buttonSendFeatureReport)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.spinSizeOut = QSpinBox(self.verticalLayoutWidget_3)
        self.spinSizeOut.setObjectName(u"spinSizeOut")
        self.spinSizeOut.setMinimum(1)
        self.spinSizeOut.setMaximum(256)
        self.spinSizeOut.setValue(64)

        self.horizontalLayout_2.addWidget(self.spinSizeOut)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.boxDevices = QGroupBox(self.centralwidget)
        self.boxDevices.setObjectName(u"boxDevices")
        self.boxDevices.setGeometry(QRect(20, 50, 661, 91))
        self.verticalLayoutWidget = QWidget(self.boxDevices)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 641, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonReScan = QPushButton(self.verticalLayoutWidget)
        self.buttonReScan.setObjectName(u"buttonReScan")
        sizePolicy.setHeightForWidth(self.buttonReScan.sizePolicy().hasHeightForWidth())
        self.buttonReScan.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.buttonReScan)

        self.deviceList = QComboBox(self.verticalLayoutWidget)
        self.deviceList.setObjectName(u"deviceList")

        self.horizontalLayout.addWidget(self.deviceList)

        self.buttonConnect = QPushButton(self.verticalLayoutWidget)
        self.buttonConnect.setObjectName(u"buttonConnect")
        sizePolicy.setHeightForWidth(self.buttonConnect.sizePolicy().hasHeightForWidth())
        self.buttonConnect.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.buttonConnect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(20, 10, 591, 31))
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.attribution = QLabel(self.centralwidget)
        self.attribution.setObjectName(u"attribution")
        self.attribution.setGeometry(QRect(630, 540, 60, 16))
        self.attribution.setOpenExternalLinks(True)
        HIDToyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HIDToyWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        HIDToyWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HIDToyWindow)
        self.statusbar.setObjectName(u"statusbar")
        HIDToyWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(HIDToyWindow)

        QMetaObject.connectSlotsByName(HIDToyWindow)
    # setupUi

    def retranslateUi(self, HIDToyWindow):
        HIDToyWindow.setWindowTitle(QCoreApplication.translate("HIDToyWindow", u"HIDToy", None))
        self.boxReceiveData.setTitle(QCoreApplication.translate("HIDToyWindow", u"Receive data:", None))
        self.buttonReadInReport.setText(QCoreApplication.translate("HIDToyWindow", u"Read IN Reports", None))
        self.buttonGetFeatureReport.setText(QCoreApplication.translate("HIDToyWindow", u"Get FEATURE Report", None))
        self.label_10.setText(QCoreApplication.translate("HIDToyWindow", u"reportId:", None))
        self.label_7.setText(QCoreApplication.translate("HIDToyWindow", u"reportSize:", None))
        self.boxSendData.setTitle(QCoreApplication.translate("HIDToyWindow", u"Send data:", None))
        self.buttonSendOutReport.setText(QCoreApplication.translate("HIDToyWindow", u"Send OUT Report", None))
        self.buttonSendFeatureReport.setText(QCoreApplication.translate("HIDToyWindow", u"Send FEATURE Report", None))
        self.label_6.setText(QCoreApplication.translate("HIDToyWindow", u"reportSize:", None))
        self.label_8.setText(QCoreApplication.translate("HIDToyWindow", u"Send data format is Python list, e.g. \"1,99,0xff,0,0\". 1st byte is reportId (if using reportIds)", None))
        self.boxDevices.setTitle(QCoreApplication.translate("HIDToyWindow", u"Devices:", None))
        self.buttonReScan.setText(QCoreApplication.translate("HIDToyWindow", u"Rescan", None))
        self.buttonConnect.setText(QCoreApplication.translate("HIDToyWindow", u"Connect", None))
        self.labelTitle.setText(QCoreApplication.translate("HIDToyWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">HIDPyToy</span> - List HID devices. Send data. Receive data. Use IN, OUT, or FEATURE reports!</p></body></html>", None))
        self.attribution.setText(QCoreApplication.translate("HIDToyWindow", u"<html><head/><body><p>by <a href=\"https://github.com/todbot/hidpytoy/\"><span style=\" text-decoration: underline; color:#0000ff;\">todbot</span></a></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("HIDToyWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("HIDToyWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("HIDToyWindow", u"View", None))
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

