# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/6 11:26

from PyQt5.Qt import  QWidget,QApplication, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QColor
from PyQt5.QtCore import Qt
import sys
import mainWindow

class tpCal(QWidget):
    def __init__(self):
        super(tpCal, self).__init__()
        self.initUI()


    def initUI(self):
        self.ui = mainWindow.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("t-p相空间")

        # self.ui.comboBox.setModel(QStandardItemModel(self))
        # self.ui.comboBox.view().pressed.connect(self.handleItemPressed)
        self.selectBunch = [] #存储选中的Bunch
        self.ui.isUsed.setEnabled(False)

        self.ui.savePathBtn.clicked.connect(self.selectSavePath)
        self.ui.useBunchNumberSpinBox.valueChanged.connect(self.on_usingBunchNumber_slot)
        self.ui.isUsed.stateChanged.connect(self.on_isUsed_slot)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combobox_slot)

    def selectSavePath(self):
        fileName = QFileDialog.getSaveFileName(self,"save path","c:")
        self.ui.savePathLineEdit.setText(fileName[0])


    def on_usingBunchNumber_slot(self):
        self.ui.comboBox.clear()
        self.usingBunchNumber = self.ui.useBunchNumberSpinBox.value()
        self.ui.comboBox.addItem("NULL")

        for i in range(self.usingBunchNumber):
            self.ui.comboBox.addItem(str(i + 1))

    def on_isUsed_slot(self):
        index = self.ui.comboBox.currentIndex()

        if self.ui.isUsed.isChecked():
            self.ui.comboBox.setItemData(index, QColor(Qt.red), Qt.BackgroundRole)
            self.selectBunch.append(index)
        else:
            self.ui.comboBox.setItemData(index, QColor(Qt.white), Qt.BackgroundRole)
            if index in self.selectBunch:
                self.selectBunch.remove(index)

    def on_combobox_slot(self):
        index = self.ui.comboBox.currentIndex()
        if index == 0:
            self.ui.isUsed.setEnabled(False)
        else:
            self.ui.isUsed.setEnabled(True)
        if index in self.selectBunch:
            self.ui.isUsed.setChecked(True)
        else:
            self.ui.isUsed.setChecked(False)


    def handleItemPressed(self, index):  # 这个函数是每次选择项目时判断状态时自动调用的，不用管（自动调用）
        try:
            item = self.ui.comboBox.model().itemFromIndex(index)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = tpCal()
    w.show()
    sys.exit(app.exec_())