# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/6 11:26

from PyQt5.Qt import  QWidget,QApplication, QFileDialog,QHBoxLayout,pyqtSlot,QMessageBox
from PyQt5.QtGui import QStandardItemModel, QColor
from PyQt5.QtCore import Qt
import numpy as np
import sys
import mainWindow
from InitialDataProcessing import DataProcessing
from figure import figureCanvas

class tpCal(QWidget):
    def __init__(self):
        super(tpCal, self).__init__()
        self.initUI()


    def initUI(self):
        self.ui = mainWindow.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("t-p相空间")

        self.ui.progressBar.hide()

        self.dataProcessing = DataProcessing()
        self.dataProcessing.updateProcessBar.connect(self.update_progressBar)


        self.selectBunch = [] #存储选中的Bunch
        self.ui.isUsed.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.useBunchNumberSpinBox.valueChanged.connect(self.bunchnNumber_change)
        self.ui.calUsingBunchBtn.clicked.connect(self.data_processing)
        self.ui.comboBox.currentIndexChanged.connect(self.cal_current)

        self.ui.savePathBtn.clicked.connect(self.selectSavePath)
        self.ui.useBunchNumberSpinBox.valueChanged.connect(self.on_usingBunchNumber_slot)
        self.ui.isUsed.stateChanged.connect(self.on_isUsed_slot)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combobox_slot)

        self.beginFigure = figureCanvas()
        self.hLayout = QHBoxLayout()
        # 设置布局的边框宽度为0
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.addWidget(self.beginFigure)
        self.ui.beginWidget.setLayout(self.hLayout)

        self.endFigure = figureCanvas()
        self.hLayout = QHBoxLayout()
        # 设置布局的边框宽度为0
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.addWidget(self.endFigure)
        self.ui.endWidget.setLayout(self.hLayout)

        self.currentWakeFigure = figureCanvas()
        self.hLayout = QHBoxLayout()
        # 设置布局的边框宽度为0
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.addWidget(self.currentWakeFigure)
        self.ui.currentWakeWidget.setLayout(self.hLayout)

        self.meanWakeFigure = figureCanvas()
        self.hLayout = QHBoxLayout()
        # 设置布局的边框宽度为0
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout.addWidget(self.meanWakeFigure)
        self.ui.meanWakeWidget.setLayout(self.hLayout)

    def selectSavePath(self):
        fileName = QFileDialog.getExistingDirectory(self,"save path","c:")
        self.ui.savePathLineEdit.setText(fileName)


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
            if index not in self.selectBunch:
                self.selectBunch.append(index)
        else:
            self.ui.comboBox.setItemData(index, QColor(Qt.white), Qt.BackgroundRole)
            if index in self.selectBunch:
                self.selectBunch.remove(index)
        print(self.selectBunch)


        try:
            if len(self.selectBunch) > 0:
                Emean = np.sum(self.dataProcessing.deltaEmat[np.array(self.selectBunch) - 1, 3:],axis=0) / len(self.selectBunch)
                self.meanWakeFigure.current = Emean
                self.meanWakeFigure.t = np.arange(1,len(Emean) + 1)
            else:
                self.meanWakeFigure.current = []
                self.meanWakeFigure.t = []

            self.meanWakeFigure.update_figure(kind="wake")
        except Exception as e:
            print(e)


    def on_combobox_slot(self):
        try:
            index = self.ui.comboBox.currentIndex()
            if index == 0:
                self.ui.isUsed.setEnabled(False)
                self.ui.bunchSimilarity.setText("")
            else:
                self.ui.isUsed.setEnabled(True)
                self.ui.bunchSimilarity.setText('%.4f%%' % self.dataProcessing.deltaEmat[index - 1,2])
            if index in self.selectBunch:
                self.ui.isUsed.setChecked(True)
            else:
                self.ui.isUsed.setChecked(False)
        except Exception as e:
            print(e)

    def cal_current(self):
        try:
            if self.ui.comboBox.currentIndex() > 0:

                p = self.dataProcessing.bunchGroup[self.ui.comboBox.currentIndex() - 1, 0] + 1
                q = self.dataProcessing.bunchGroup[self.ui.comboBox.currentIndex() - 1, 1] + 1
                print(p,q)

                beginCurrent = np.loadtxt("./firstDataProcessing/current_Begin_" + str(p) + ".txt")
                endCurrent = np.loadtxt("./firstDataProcessing/current_End_" + str(q) + ".txt")

                FWHM = np.sum(endCurrent >= np.max(endCurrent) / 2)
                t = np.arange(1,501) * self.ui.FWHMSPinBox.value()
                delta_t = self.ui.FWHMSPinBox.value() / FWHM
                beginCurrent = beginCurrent * self.ui.ChargeSpinBox.value() / delta_t
                endCurrent = endCurrent * self.ui.ChargeSpinBox.value() / delta_t

                self.beginFigure.current = beginCurrent
                self.beginFigure.t = t
                # print('self.beginFigure.current',self.beginFigure.current)
                # print('self.beginFigure.t', self.beginFigure.t)

                self.endFigure.current = endCurrent
                self.endFigure.t = t
                # print('self.endFigure.current', self.endFigure.current)
                # print('self.endFigure.t', self.endFigure.t)

                self.beginFigure.update_figure(kind="current")
                self.endFigure.update_figure(kind="current")

                self.currentWakeFigure.current = self.dataProcessing.deltaEmat[self.ui.comboBox.currentIndex() - 1,3:]
                self.currentWakeFigure.t = np.arange(1,501)
                self.currentWakeFigure.update_figure(kind="wake")
            else:
                self.beginFigure.current = []
                self.beginFigure.t = []

                self.endFigure.current = []
                self.endFigure.t = []

                self.currentWakeFigure.current = []
                self.currentWakeFigure.t = []
                self.currentWakeFigure.update_figure(kind="wake")

                self.beginFigure.update_figure(kind="current")
                self.endFigure.update_figure(kind="current")

        except Exception as e:
            print(e)


    def data_processing(self):
        try:
            self.ui.calUsingBunchBtn.setEnabled(False)
            # self.dataProcessing.cal_deltaE(200,self.ui.useBunchNumberSpinBox.value())
            self.dataProcessing.n = self.ui.pickBunchNumberSpinBox.value()
            self.dataProcessing.bunchGroupNumber = self.ui.useBunchNumberSpinBox.value()
            self.dataProcessing.energyUnit = self.ui.EnergyUnitSpinBox.value()
            self.dataProcessing.start()

        except Exception as e:
            print(e)


    def bunchnNumber_change(self):
        self.ui.comboBox.setEnabled(False)

    @pyqtSlot(float)
    def update_progressBar(self,n):
        self.ui.progressBar.setValue(n * 100)
        if n == 0:
            self.ui.progressBar.show()
        elif n == 1:
            self.ui.progressBar.hide()
            self.dataProcessing.quit()
            self.ui.comboBox.setEnabled(True)
            self.ui.calUsingBunchBtn.setEnabled(True)
            QMessageBox.information(self,"Tip","Calculate done!")




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