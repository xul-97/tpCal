# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/6 11:26

from PyQt5.Qt import  QWidget,QApplication, QFileDialog
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

        self.ui.savePathBtn.clicked.connect(self.selectSavePath)

    def selectSavePath(self):
        fileName = QFileDialog.getSaveFileName(self,"save path","c:")
        self.ui.savePathLineEdit.setText(fileName[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = tpCal()
    w.show()
    sys.exit(app.exec_())