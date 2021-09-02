# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/22 14:09

from PyQt5.QtCore import QThread,pyqtSignal
import numpy as np
from scipy.io import loadmat
from scipy.signal import medfilt


class DataProcessing(QThread):

    updateProcessBar = pyqtSignal(float)

    BeginCurrent = np.empty([0,500])
    EndCurrent = np.empty([0,500])
    deltaEmat = np.empty([0,503])
    bunchGroup = np.empty([0,2],dtype=int)
    n = 200
    bunchGroupNumber = 10
    energyUnit = 2.8
    position = "Begin"
    rotNumber = 0
    filterValue = 10
    step = 1
    filePath = ""
    flag  = "1"


    def __init__(self):
        super(DataProcessing, self).__init__()

    def run(self):
        try:
            if self.step == 1:
                self.data_processing(self.n,self.position,self.flag)
            else:
                self.cal_deltaE(self.n,self.bunchGroupNumber,self.energyUnit)
        except Exception as e:
            print(e)

    def data_processing(self, n = 200, position = "Begin",flag = "1"):
        '''
        :param n: the number of Bunch
        :param position: the mark of the data from Begin or End
        :return:
        '''
        #存储截取数据的索引
        mark = np.zeros([n,2],dtype= int)
        mark[:,1] = 499
        self.updateProcessBar.emit(0)

        for i in range(1,n+1):
            data = np.loadtxt(self.filePath + "\\dataFromEpics\\img" + flag + "_" + str(i) + ".txt")
            print("img" + flag + "_" + str(i) + ".txt" + "加载成功")
            self.updateProcessBar.emit(i / n)
            #小于10的数据置0
            data[data < self.filterValue] = 0

            #中值滤波
            imgFilt = medfilt(data, [21, 21])
            imgFilt = np.rot90(imgFilt, self.rotNumber)

            #求电流值并归一化
            current = np.sum(imgFilt, axis=0) / np.sum(imgFilt)

            #TODO 寻找截取数据的前后索引(可以利用numpy的函数再优化一下)
            beginFlag = True
            endFlag = True

            for j in range(500):

                if beginFlag:
                    if current[j] < 5e-4:
                        mark[i - 1,0] = j

                    elif current[j] > 1e-3:
                        beginFlag = False

                if endFlag:
                    if current[499 - j] < 5e-4:
                        mark[i - 1,1] = 499 - j

                    elif current[499 - j] > 1e-3:
                        endFlag = False

                if (not beginFlag) and (not endFlag):
                    break

            # 对电流进行截取
            print(i)

            current = current[mark[i - 1, 0] + 1:mark[i - 1, 1]]

            #进行插值
            current = np.interp(np.linspace(1,500,500,endpoint=True),np.linspace(1,500,len(current),endpoint=True),current)

            #归一化
            current = current / np.sum(current)
            # globals()['DataProcessing.' + position + 'Current'] = np.vstack(( globals()['DataProcessing.' + position + 'Current'],current))

            np.savetxt(self.filePath + "\\firstDataProcessing\\imgFilt_" + position + "_" + str(i) + ".txt", imgFilt)
            np.savetxt(self.filePath + "\\firstDataProcessing\\current_" + position + "_" + str(i) + ".txt", current)

        np.savetxt(self.filePath + "\\firstDataProcessing\\mark" + position + ".txt", mark)

    def cal_deltaE(self,n = 200, bunchGroupNumber = 10, energyUnit = 2.8):

        self.updateProcessBar.emit(0)

        dcSum = np.zeros([n,n])
        bunchGroup = np.zeros([bunchGroupNumber + 1,2],dtype=int)
        bunchSimilarity = np.zeros(bunchGroupNumber + 1)

        for i in range(1, n+1):
            self.updateProcessBar.emit(i / n * 0.5)
            currentBegin = np.loadtxt(self.filePath + "\\firstDataProcessing\\current_Begin_" + str(i) + ".txt")
            print("current_Begin_" + str(i) + ".txt" + "加载成功")

            for j in range(1, n+1):
                currentEnd = np.loadtxt(self.filePath + "\\firstDataProcessing\\current_End_" + str(j) + ".txt")

                deltaCurrent = np.abs(currentEnd - currentBegin)
                dcSum[i - 1, j -1] = np.sum(deltaCurrent)

        minCurrent = np.min(dcSum)
        print(minCurrent)
        print(np.where(dcSum == minCurrent))
        bunchGroup[0, 0] = np.where(dcSum == minCurrent)[0][0]
        bunchGroup[0, 1] = np.where(dcSum == minCurrent)[1][0]
        bunchSimilarity[0] = (1 - minCurrent / 2) * 100
        deltaEmat = np.empty([bunchGroupNumber,503])

        markBegin = np.loadtxt(self.filePath + "\\firstDataProcessing\\markBegin.txt").astype(int)
        markEnd = np.loadtxt(self.filePath + "\\firstDataProcessing\\markEnd.txt").astype(int)

        for k in range(bunchGroupNumber):

            DataProcessing.bunchGroup = np.vstack((DataProcessing.bunchGroup,bunchGroup[k,:]))
            imgFiltBegin = np.loadtxt(self.filePath + "\\firstDataProcessing\\imgFilt_Begin_" + str(bunchGroup[k,0] + 1) + ".txt")
            imgFiltEnd = np.loadtxt(self.filePath + "\\firstDataProcessing\\imgFilt_End_" + str(bunchGroup[k,1] + 1)+ ".txt")


            print(k,bunchGroup[k,:] + 1,markBegin[bunchGroup[k,0],:],markBegin[bunchGroup[k,1],:])
            EBegin = np.zeros([markBegin[bunchGroup[k,0],1] - markBegin[bunchGroup[k,0],0] - 1])
            EEnd = np.zeros([markEnd[bunchGroup[k, 1], 1] - markEnd[bunchGroup[k, 1], 0] - 1])

            EBeginStart = 0
            EEndStart = 0

            for i in range(500):
                EBeginStart = EBeginStart + (500 - i) * imgFiltBegin[i,markBegin[bunchGroup[k,0],0]]
                EEndStart = EEndStart + (500 - i) * imgFiltEnd[i, markEnd[bunchGroup[k, 1], 0]]

            EBeginStart = EBeginStart / np.sum(imgFiltBegin[:,markBegin[bunchGroup[k,0],0]])
            EEndStart = EEndStart / np.sum(imgFiltEnd[:, markEnd[bunchGroup[k, 1], 0]])
            x = EBeginStart - EEndStart

            for i in range(markBegin[bunchGroup[k,0],0] + 1,markBegin[bunchGroup[k,0],1]):
                Ej = 0
                for j in range(500):
                    Ej = Ej + (500 - j - x) * imgFiltBegin[j,i]

                Ej = Ej / np.sum(imgFiltBegin[:,i])

                EBegin[i - markBegin[bunchGroup[k,0],0] - 1] = Ej

            EBeginNew = np.interp(np.linspace(1, 500, 500, endpoint=True),
                                np.linspace(1, 500, len(EBegin), endpoint=True), EBegin)

            for i in range(markEnd[bunchGroup[k, 1], 0] + 1, markEnd[bunchGroup[k, 1], 1]):
                Ej = 0
                for j in range(500):
                    Ej = Ej + (500 - j) * imgFiltEnd[j, i]


                Ej = Ej / np.sum(imgFiltEnd[:, i])

                EEnd[i - markEnd[bunchGroup[k, 1], 0] - 1] = Ej

            EEndNew = np.interp(np.linspace(1, 500, 500, endpoint=True),
                                  np.linspace(1, 500, len(EEnd), endpoint=True), EEnd)

            deltaE = EBeginNew - EEndNew
            deltaE = medfilt(deltaE,25) / 100 * energyUnit
            deltaEmat[k,:] = np.concatenate(([bunchGroup[k,0],bunchGroup[k,1],bunchSimilarity[k]],deltaE))
            DataProcessing.deltaEmat = np.vstack((DataProcessing.deltaEmat,deltaEmat[k,:]))
            # print(deltaEmat[k,:])
            print(bunchGroup[k, 0], bunchGroup[k, 1])
            print(dcSum[bunchGroup[k, 0], bunchGroup[k, 1]])
            dcSum[bunchGroup[k,0],bunchGroup[k,1]] = 1
            print(dcSum[bunchGroup[k,0],bunchGroup[k,1]])

            minCurrent = np.min(dcSum)
            print("最小值索引",np.where(dcSum == minCurrent))
            bunchGroup[k + 1, 0] = np.where(dcSum == minCurrent)[0][0]
            bunchGroup[k + 1, 1] = np.where(dcSum == minCurrent)[1][0]
            bunchSimilarity[k + 1] = (1 - minCurrent / 2) * 100

            self.updateProcessBar.emit((k + 1) / bunchGroupNumber * 0.5 + 0.5)

        np.savetxt(self.filePath + "\\firstDataProcessing\\deltaEmat.txt",deltaEmat)




if __name__ == '__main__':

    w = DataProcessing()
    # w.data_processing(200,"Begin")
    w.cal_deltaE(200,15)






