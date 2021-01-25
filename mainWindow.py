# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(639, 665)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(521, 540))
        Form.setMaximumSize(QtCore.QSize(9999, 999))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(375, 50, 251, 111))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.widget.setObjectName("widget")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 6, 101, 20))
        self.label_6.setObjectName("label_6")
        self.FWHMSPinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.FWHMSPinBox.setGeometry(QtCore.QRect(111, 6, 51, 21))
        self.FWHMSPinBox.setDecimals(1)
        self.FWHMSPinBox.setObjectName("FWHMSPinBox")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(181, 5, 21, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 43, 81, 16))
        self.label_8.setObjectName("label_8")
        self.EnergyUnitSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.EnergyUnitSpinBox.setGeometry(QtCore.QRect(110, 43, 51, 21))
        self.EnergyUnitSpinBox.setDecimals(1)
        self.EnergyUnitSpinBox.setObjectName("EnergyUnitSpinBox")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(170, 43, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(20, 175, 211, 21))
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(63, 176, 81, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(440, 174, 101, 21))
        self.label_15.setObjectName("label_15")
        self.bunchSimilarity = QtWidgets.QLineEdit(Form)
        self.bunchSimilarity.setGeometry(QtCore.QRect(540, 175, 71, 20))
        self.bunchSimilarity.setReadOnly(True)
        self.bunchSimilarity.setObjectName("bunchSimilarity")
        self.widget_6 = QtWidgets.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(13, 50, 351, 111))
        self.widget_6.setStyleSheet("QWidget#widget_6{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.widget_6.setObjectName("widget_6")
        self.layoutWidget = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 76, 331, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.useBunchNumberSpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.useBunchNumberSpinBox.setMinimumSize(QtCore.QSize(0, 20))
        self.useBunchNumberSpinBox.setMinimum(0)
        self.useBunchNumberSpinBox.setMaximum(1000000)
        self.useBunchNumberSpinBox.setProperty("value", 10)
        self.useBunchNumberSpinBox.setObjectName("useBunchNumberSpinBox")
        self.horizontalLayout_3.addWidget(self.useBunchNumberSpinBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.calUsingBunchBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.calUsingBunchBtn.setObjectName("calUsingBunchBtn")
        self.horizontalLayout_3.addWidget(self.calUsingBunchBtn)
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget_2.setGeometry(QtCore.QRect(8, 0, 331, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.pickTPBeginBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pickTPBeginBtn.setObjectName("pickTPBeginBtn")
        self.gridLayout_3.addWidget(self.pickTPBeginBtn, 0, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.pickTPEndBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pickTPEndBtn.setObjectName("pickTPEndBtn")
        self.gridLayout_3.addWidget(self.pickTPEndBtn, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(15, 10, 611, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.savePathLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.savePathLineEdit.setReadOnly(True)
        self.savePathLineEdit.setObjectName("savePathLineEdit")
        self.horizontalLayout.addWidget(self.savePathLineEdit)
        self.savePathBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.savePathBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("savePath.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savePathBtn.setIcon(icon)
        self.savePathBtn.setObjectName("savePathBtn")
        self.horizontalLayout.addWidget(self.savePathBtn)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pickBunchNumberSpinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.pickBunchNumberSpinBox.setMinimum(0)
        self.pickBunchNumberSpinBox.setMaximum(1000000)
        self.pickBunchNumberSpinBox.setProperty("value", 200)
        self.pickBunchNumberSpinBox.setObjectName("pickBunchNumberSpinBox")
        self.horizontalLayout.addWidget(self.pickBunchNumberSpinBox)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(15, 210, 611, 411))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.beginWidget = QtWidgets.QWidget(self.layoutWidget2)
        self.beginWidget.setStyleSheet("QWidget#beginWidget{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.beginWidget.setObjectName("beginWidget")
        self.label_10 = QtWidgets.QLabel(self.beginWidget)
        self.label_10.setGeometry(QtCore.QRect(70, 60, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.beginWidget, 0, 0, 1, 1)
        self.endWidget = QtWidgets.QWidget(self.layoutWidget2)
        self.endWidget.setStyleSheet("QWidget#endWidget{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.endWidget.setObjectName("endWidget")
        self.label_11 = QtWidgets.QLabel(self.endWidget)
        self.label_11.setGeometry(QtCore.QRect(70, 60, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.endWidget, 0, 1, 1, 1)
        self.currentWakeWidget = QtWidgets.QWidget(self.layoutWidget2)
        self.currentWakeWidget.setStyleSheet("QWidget#currentWakeWidget{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.currentWakeWidget.setObjectName("currentWakeWidget")
        self.label_12 = QtWidgets.QLabel(self.currentWakeWidget)
        self.label_12.setGeometry(QtCore.QRect(50, 50, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.currentWakeWidget, 1, 0, 1, 1)
        self.meanWakeWidget = QtWidgets.QWidget(self.layoutWidget2)
        self.meanWakeWidget.setStyleSheet("QWidget#meanWakeWidget\n"
"{\n"
"    border: 2px solid #000000; border-radius: 5px;}")
        self.meanWakeWidget.setObjectName("meanWakeWidget")
        self.label_13 = QtWidgets.QLabel(self.meanWakeWidget)
        self.label_13.setGeometry(QtCore.QRect(50, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.meanWakeWidget, 1, 1, 1, 1)
        self.isUsed = QtWidgets.QCheckBox(Form)
        self.isUsed.setGeometry(QtCore.QRect(255, 178, 51, 16))
        self.isUsed.setObjectName("isUsed")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(430, 636, 191, 20))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "FWHM(Current):"))
        self.label_7.setText(_translate("Form", "ps"))
        self.label_8.setText(_translate("Form", "Energy Unit:"))
        self.label_9.setText(_translate("Form", "MeV/100pixel"))
        self.label_14.setText(_translate("Form", "展示第                相似的束团组"))
        self.comboBox.setItemText(0, _translate("Form", "NULL"))
        self.comboBox.setItemText(1, _translate("Form", "1"))
        self.comboBox.setItemText(2, _translate("Form", "2"))
        self.comboBox.setItemText(3, _translate("Form", "3"))
        self.comboBox.setItemText(4, _translate("Form", "4"))
        self.comboBox.setItemText(5, _translate("Form", "5"))
        self.comboBox.setItemText(6, _translate("Form", "6"))
        self.comboBox.setItemText(7, _translate("Form", "7"))
        self.comboBox.setItemText(8, _translate("Form", "8"))
        self.comboBox.setItemText(9, _translate("Form", "9"))
        self.comboBox.setItemText(10, _translate("Form", "10"))
        self.label_15.setText(_translate("Form", "该组束团相似度："))
        self.label_16.setText(_translate("Form", "拟采用束团组数："))
        self.calUsingBunchBtn.setText(_translate("Form", "Data Processing"))
        self.comboBox_2.setItemText(0, _translate("Form", "0°"))
        self.comboBox_2.setItemText(1, _translate("Form", "90°"))
        self.comboBox_2.setItemText(2, _translate("Form", "180°"))
        self.comboBox_2.setItemText(3, _translate("Form", "270°"))
        self.pickTPBeginBtn.setText(_translate("Form", "Start"))
        self.comboBox_3.setItemText(0, _translate("Form", "0°"))
        self.comboBox_3.setItemText(1, _translate("Form", "90°"))
        self.comboBox_3.setItemText(2, _translate("Form", "180°"))
        self.comboBox_3.setItemText(3, _translate("Form", "270°"))
        self.label_17.setText(_translate("Form", "采集始端t-p相空间："))
        self.pickTPEndBtn.setText(_translate("Form", "Start"))
        self.label_18.setText(_translate("Form", "采集末端t-p相空间："))
        self.label_3.setText(_translate("Form", "旋转"))
        self.label_4.setText(_translate("Form", "旋转"))
        self.label.setText(_translate("Form", "保存路径："))
        self.label_2.setText(_translate("Form", "采集束团组数："))
        self.label_10.setText(_translate("Form", "始端"))
        self.label_11.setText(_translate("Form", "末端"))
        self.label_12.setText(_translate("Form", "当前wake"))
        self.label_13.setText(_translate("Form", "平均wake"))
        self.isUsed.setText(_translate("Form", "采用"))
