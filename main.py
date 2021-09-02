# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/6 11:26
import os

from PyQt5.Qt import  QWidget,QApplication, QFileDialog,QHBoxLayout,pyqtSlot,QMessageBox
from PyQt5.QtGui import QStandardItemModel, QColor
from PyQt5.QtCore import Qt
import numpy as np
from scipy import io
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

        #获取当前路径
        self.filePath = os.getcwd()
        self.ui.savePathLineEdit.setText(self.filePath)

        self.ui.progressBar.hide()
        self.ui.processBarLabel.setText("")
        self.processBarLabel = ""
        self.ui.calMeanBtn.setEnabled(False)


        self.dataProcessing = DataProcessing()
        self.dataProcessing.updateProcessBar.connect(self.update_progressBar)


        self.selectBunch = [] #存储选中的Bunch
        self.ui.isUsed.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        # self.ui.comboBox_2.valueChanged.connect(self.bunchnNumber_change)
        self.ui.calUsingBunchBtn.clicked.connect(self.data_processing_2)
        self.ui.comboBox.currentIndexChanged.connect(self.cal_current)

        self.ui.savePathBtn.clicked.connect(self.selectSavePath)
        # self.ui.useBunchNumberSpinBox.valueChanged.connect(self.on_usingBunchNumber_slot)
        self.ui.isUsed.stateChanged.connect(self.on_isUsed_slot)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combobox_slot)

        self.ui.pickTPBeginBtn.clicked.connect(self.on_pick_data_slot)
        self.ui.pickTPEndBtn.clicked.connect(self.on_pick_data_slot)

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

        self.ui.pickBunchNumberSpinBox.valueChanged.connect(self.bunchGroupNumberChange)


        for i in range(1,201):
            self.ui.beginInitialTp.addItem(str(i))
            self.ui.endInitialTp.addItem(str(i))
            self.ui.beginAfterTp.addItem(str(i))
            self.ui.endAfterTp.addItem(str(i))
        self.ui.beginInitialTp.currentIndexChanged.connect(self.tpShowBegin)
        self.ui.beginAfterTp.currentIndexChanged.connect(self.tpShowBegin)
        self.ui.endInitialTp.currentIndexChanged.connect(self.tpShowEnd)
        self.ui.endAfterTp.currentIndexChanged.connect(self.tpShowEnd)

        self.ui.beginDataProcessing.clicked.connect(self.data_processing_1)
        self.ui.endDataProcessing.clicked.connect(self.data_processing_1)

        self.ui.calMeanBtn.clicked.connect(self.on_mean_slot)

    def selectSavePath(self):
        self.filePath = QFileDialog.getExistingDirectory(self,"save path","c:")
        self.ui.savePathLineEdit.setText(self.filePath)

        os.mkdir(self.filePath + "\\dataFromEpics")
        os.mkdir(self.filePath + "\\firstDataProcessing")
        os.mkdir(self.filePath + "\\result")

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

        if len(self.selectBunch) > 1:
            self.ui.calMeanBtn.setEnabled(True)
        else:
            self.ui.calMeanBtn.setEnabled(False)


        # try:
        #     if len(self.selectBunch) > 0:
        #         Emean = np.sum(self.dataProcessing.deltaEmat[np.array(self.selectBunch) - 1, 3:],axis=0) / len(self.selectBunch)
        #         self.meanWakeFigure.current = Emean
        #         self.meanWakeFigure.t = np.arange(1,len(Emean) + 1)
        #     else:
        #         self.meanWakeFigure.current = []
        #         self.meanWakeFigure.t = []
        #
        #     self.meanWakeFigure.update_figure(kind="wake")
        # except Exception as e:
        #     print(e)

    def on_mean_slot(self):

        Emean = np.sum(self.dataProcessing.deltaEmat[np.array(self.selectBunch) - 1, 3:], axis=0) / len(self.selectBunch)
        self.meanWakeFigure.current = Emean
        self.meanWakeFigure.t = np.arange(1,len(Emean) + 1)
        self.meanWakeFigure.update_figure(kind = "wake", label1= "Mean ")


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

                beginCurrent = np.loadtxt(self.filePath + "\\firstDataProcessing\\current_Begin_" + str(p) + ".txt")
                endCurrent = np.loadtxt(self.filePath + "\\firstDataProcessing\\current_End_" + str(q) + ".txt")

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

                # self.beginFigure.update_figure(kind="current")
                # self.endFigure.update_figure(kind="current")

                self.currentWakeFigure.current = beginCurrent
                self.currentWakeFigure.current1 = endCurrent
                self.currentWakeFigure.t = np.arange(1,501)
                self.currentWakeFigure.update_figure(kind="twoCurrent",label1=str(p),label2=str(q))

                self.meanWakeFigure.current = self.dataProcessing.deltaEmat[self.ui.comboBox.currentIndex()-1,3:]
                self.meanWakeFigure.t = np.arange(1,501)
                self.meanWakeFigure.update_figure(kind = "wake")
            else:
                self.beginFigure.current = []
                self.beginFigure.t = []

                self.endFigure.current = []
                self.endFigure.t = []

                self.currentWakeFigure.current = []
                self.currentWakeFigure.current1 = []
                self.currentWakeFigure.t = []
                self.currentWakeFigure.update_figure(kind="twoCurrent")

                self.meanWakeFigure.current = []
                self.meanWakeFigure.t = []
                self.meanWakeFigure.update_figure(kind = "wake")

                # self.beginFigure.update_figure(kind="current")
                # self.endFigure.update_figure(kind="current")

        except Exception as e:
            print(e)


    def data_processing_2(self):
        try:
            self.ui.calUsingBunchBtn.setEnabled(False)
            self.processBarLabel = "Finding similar bunches "
            # self.dataProcessing.cal_deltaE(200,self.ui.useBunchNumberSpinBox.value()) 已经使用线程表示
            self.dataProcessing.n = self.ui.pickBunchNumberSpinBox.value()
            self.dataProcessing.bunchGroupNumber = self.ui.useBunchNumberSpinBox.value()
            self.dataProcessing.energyUnit = self.ui.EnergyUnitSpinBox.value()
            self.dataProcessing.step = 2
            self.dataProcessing.filePath = self.filePath
            self.dataProcessing.start()

        except Exception as e:
            print(e)

    def data_processing_1(self):

        try:
            self.ui.calUsingBunchBtn.setEnabled(False)
            self.dataProcessing.n = self.ui.pickBunchNumberSpinBox.value()

            if self.sender().objectName() == "beginDataProcessing":
                self.dataProcessing.position = "Begin"
                self.processBarLabel = "Data 1 Processing"
                self.dataProcessing.rotNumber = self.ui.beginRot.currentIndex()
                self.dataProcessing.filterValue = self.ui.beginFiltValue.value()
                self.ui.beginDataProcessing.setEnabled(False)
                self.dataProcessing.flag = "1"
            else:
                self.dataProcessing.position = "End"
                self.processBarLabel = "Data 2 Processing"
                self.dataProcessing.rotNumber = self.ui.endRot.currentIndex()
                self.dataProcessing.filterValue = self.ui.endFiltValue.value()
                self.ui.endDataProcessing.setEnabled(False)
                self.dataProcessing.flag = "2"
            self.dataProcessing.filePath = self.filePath
            self.dataProcessing.step = 1
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
            self.ui.processBarLabel.setText(self.processBarLabel)
        elif n == 1:
            self.ui.progressBar.hide()
            self.ui.processBarLabel.setText("")
            self.dataProcessing.quit()
            self.ui.comboBox.setEnabled(True)
            if not self.ui.calUsingBunchBtn.isEnabled():
                self.on_usingBunchNumber_slot()
            self.ui.calUsingBunchBtn.setEnabled(True)
            self.ui.beginDataProcessing.setEnabled(True)
            self.ui.endDataProcessing.setEnabled(True)
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

    def tpShowBegin(self):
        if self.sender().objectName() == "beginInitialTp":
            beginMat = np.loadtxt(self.filePath + "\\dataFromEpics\\img1_" + self.ui.beginInitialTp.currentText() + ".txt")
        else:
            beginMat = np.loadtxt(self.filePath + "\\firstDataProcessing\\imgFilt_Begin_" + self.ui.beginAfterTp.currentText() + ".txt")
        self.beginFigure.img = beginMat
        self.beginFigure.update_figure(kind="tp")

    def tpShowEnd(self):

        if self.sender().objectName() == "endInitialTp":
            endMat = np.loadtxt(self.filePath + "\\dataFromEpics\\img2_" + self.ui.endInitialTp.currentText() + ".txt")
        else:
            endMat = np.loadtxt(self.filePath + "\\firstDataProcessing\\imgFilt_End_" + self.ui.endAfterTp.currentText() + ".txt")
        self.endFigure.img = endMat
        self.endFigure.update_figure(kind="tp")

    def bunchGroupNumberChange(self):
        pass

        # for i in range(1,self.ui.pickBunchNumberSpinBox.value() + 1):
        #     self.ui.beginInitialTp.addItem(str(i))
        #     self.ui.endInitialTp.addItem(str(i))
        #     self.ui.beginAfterTp.addItem(str(i))
        #     self.ui.endAfterTp.addItem(str(i))

    def on_pick_data_slot(self):
        if self.sender().objectName() == "pickTPBeginBtn":
            flag = "2"
            saveFlag = "1"
        else:
            flag = "1"
            saveFlag = "2"

        for i in range(1,self.ui.pickBunchNumberSpinBox.value() + 1):
            Mat = io.loadmat("./dataFromEpics1/img" + flag + "_" + str(i) + ".mat")["img_g"]
            np.savetxt(self.filePath + "\\dataFromEpics\\img" + saveFlag + "_" +  str(i) + ".txt",Mat)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = tpCal()
    w.show()
    sys.exit(app.exec_())