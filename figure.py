# -*- coding: utf-8 -*-
# @Author  : xuliang
# @Email   : xuliang@sinap.ac.cn 
# @Time    : 2021/1/24 14:20

import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class XYCanvas(FigureCanvas):

    def __init__(self):
        self.figure = plt.figure(figsize=(8,4),frameon = False)
        plt.subplots_adjust(left=0.09, right=0.98, bottom=0.15, top=0.9)
        plt.grid()
        plt.ylabel("x/y")
        plt.ylim(0,500)
        plt.xlim(0,500)
        self.ax = self.figure.add_subplot()
        self.compute_initial_figure()

        FigureCanvas.__init__(self, self.figure)
        FigureCanvas.updateGeometry(self)

        def compute_initial_figure(self):
            pass
        
class figureCanvas(XYCanvas):
    def __init__(self):
        XYCanvas.__init__(self)
        plt.subplots_adjust(left=0.2, right=0.92, bottom=0.2, top=0.9)
        self.t = []
        self.current = []
        self.current1 = []
        self.img = np.array([])

    def compute_initial_figure(self):
        plt.plot([], [])


    def update_figure(self,kind = "current",label1 = "",label2 = ""):
        try:
            self.ax.cla()
            self.ax.grid()
            if kind == "tp":
                self.ax.set_title("t-p",fontsize = 7)
                self.ax.set_xlabel("t",fontsize = 7)
                self.ax.set_ylabel("energy",fontsize = 7)
                # self.ax.plot(self.t,self.current,'r')
                self.ax.imshow(self.img,cmap="hot_r",vmin = 0,origin="lower")
                self.ax.grid(None)
            elif kind == "wake":
                self.ax.set_title(label1 + " ΔE", fontsize=7)
                self.ax.set_xlabel("s[um]", fontsize=7)
                self.ax.set_ylabel("energy[MeV]", fontsize=7)
                self.ax.plot(self.t, self.current, 'g')
            elif kind == "twoCurrent":
                self.ax.set_title("Current", fontsize=7)
                self.ax.set_xlabel("t[ps]", fontsize=7)
                self.ax.set_ylabel("current[A]", fontsize=7)
                self.ax.plot(self.t, self.current, c = 'r',label = label1)
                self.ax.plot(self.t,self.current1, c = 'b',label = label2)
                self.ax.legend(loc = 8)


            self.draw()
        except Exception as e:
            print(e)

