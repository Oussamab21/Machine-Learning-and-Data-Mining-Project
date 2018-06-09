#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:54:52 2018


"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#import tensorflow as tf
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np 
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import Levenshtein as edit_distance
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap,QScreen
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QGraphicsView,QGraphicsScene,QVBoxLayout
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,QAction)
from PyQt5.QtGui import QPainter, QColor, QPen#,QAction
from PyQt5.QtCore import Qt,QPoint,QSize#,QtAlignment  #AlignmentLeft
from PyQt5.QtGui import QPainter,QPainterPath,QColor, QFont,QBrush
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt  
import random
#from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from pylab import figure, axes, pie, title, show
import pylab

class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        h = 200
        w = 200
        self.myPenWidth = 12
        self.myPenColor = Qt.white
        self.image = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.black)  
        self.update()

    def saveImage(self, fileName, fileFormat):
        print("savetime" )
        self.image.save(fileName, fileFormat)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                      self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()
    '''
    def sizeHint(self):
        return QSize(400, 400)
    '''
#########################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1711, 1527)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1901, 1021))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 1701, 1451))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(200, 0, 271, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/home/dell1/Desktop/best.png"))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        
        #################################################"
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 40, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 70, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 99, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(110, 0, 981, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(10, 130, 461, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(875, 70, 371, 591))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(470, 370, 301, 301))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.draw2=Drawer(self.tab_2)
        self.draw2.clearImage()
        self.draw2.mainWindow = self  
        self.draw2.setObjectName("drawArea2")
        self.draw2.setGeometry(QtCore.QRect(570, 70, 300, 300))
        
        
        
        self.tabWidget.addTab(self.tab_2, "")
        
        
        
        #########################################################
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
      
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QtCore.QRect(0, 10, 99, 27)) 
        self.draw3=Drawer(self.tab_3)
        self.draw3.mainWindow = self  
        self.draw3.setObjectName("drawArea3")
        self.draw3.setGeometry(QtCore.QRect(630, 70, 300, 300))
        self.draw3.clearImage()
      
        self.tabWidget.addTab(self.tab_3, "")
        
        #################################################################
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
    
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 60, 99, 27))
        self.pushButton_7.setObjectName("pushButton_7")
       
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 110, 99, 27))
        
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 170, 99, 27))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setGeometry(QtCore.QRect(350, 280, 99, 27))
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setGeometry(QtCore.QRect(350, 340, 99, 27))
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_11.setGeometry(QtCore.QRect(350, 390, 99, 27))
        self.pushButton_11.setObjectName("pushButton_11")
       

        self.draw4=Drawer(self.tab_4)
        self.draw4.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.draw4.mainWindow = self  
       
        self.draw4.setObjectName("drawArea4")
        self.draw4.clearImage()
        
        self.draw5=Drawer(self.tab_4)
        self.draw5.mainWindow = self  
        self.draw5.setObjectName("drawArea5")
        self.draw5.setGeometry(QtCore.QRect(610, 10, 300, 300))
        self.draw5.clearImage()
       

        self.display = QLineEdit('Result')
        self.display.setReadOnly(True)
       
        self.display.setMaxLength(7)
     
        self.tabWidget.addTab(self.tab_4, "")
        
################################################################        
        
        
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 711, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Machine Learning and Data Mining Project For the Last Year of the International Master Degree at Jean Monnet University Saint Etienne France </p>\n"

"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                               January 2018</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group:                                                                                   Supervisor:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oussama Bouldjedri                                                         Pr.Marc Sebban</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arunava maulik </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">renuka chittimalla</p></body></html>"))
        
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Project"))
        self.pushButton.setText(_translate("MainWindow", "clear Board"))
        self.pushButton.clicked.connect(self.draw2.clearImage)
        self.pushButton_2.setText(_translate("MainWindow", "Save image"))
        self.pushButton_2.clicked.connect(lambda: self.draw2.saveImage("image.png", "PNG"))
        self.pushButton_3.setText(_translate("MainWindow", "Classify"))
        self.pushButton_3.clicked.connect(self.classify)
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Classification"))
        
        self.pushButton_5.setText(_translate("MainWindow", "Mine"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pattern Mining"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "-"))
        self.pushButton_9.setText(_translate("MainWindow", "*"))
        self.pushButton_10.setText(_translate("MainWindow", "/"))
        self.pushButton_11.setText(_translate("MainWindow", "="))
        #self.pushButton_12.setText(_translate("MainWindow", "Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Calculator"))
    
    
    def get_neighbors(self,train_set,labels,test_instance,k):
       distances = []
       for i in range(len(train_set)):
           dist = edit_distance.distance(str(test_instance), str(train_set[i]))
           distances.append((train_set[i], dist,  labels[i],i))
       distances.sort(key=lambda x: x[1])
       neighbors = distances[:k]
       digit=distances[0][2]
       train=distances[0][0]
       dist1=distances[0][1]
       example=distances[0][3]
       return neighbors,digit,train,dist1,example
    

    def  SingleBrowse(self,MainWindow):    
      
           filters = "Text files (*.txt);;Images (*.png *.xpm *.jpg)"
           selected_filter = "Images (*.png *.xpm *.jpg)"
           self.fileName, _  = QFileDialog.getOpenFileName(None, 'Open file', '/home',filters,selected_filter)
           #if files:
           # print(files)
            
           print(self.fileName)#,_)
           fname = open(self.fileName)
           #print(self.pushButton.setText("ee"))
           print("pass")
           self.scene=QGraphicsScene()
           self.scene.addPixmap(QPixmap(self.fileName))
           self.graphicsView.setScene(self.scene)
           
    def save(self):
        action = self.sender()
        #fileFormat = action.data()
        fileFormat="PNG"
        self.saveFile(fileFormat)       
           

    
    def saveFile(self):#, fileFormat):
        
        fileFormat="PNG"
        fileName="current_image.png"
       
        self.draw2.saveImage(fileName,fileFormat)
        
        

    def printsimilair(self,fileName):
       
        
        fname = open(fileName)
       
        print("pass")
        self.scene=QGraphicsScene()
        self.scene.addPixmap(QPixmap(fileName))
        self.graphicsView_3.setScene(self.scene)



    def classify(self):
       #fileName2="1.png"
       self.saveFile()
       img='/Users/vipulvijigiri/current_image.png'
       
       self.draw(img)
       
       
       
       
    def CreateHist(self,code):
    
     from collections import Counter
     import linecache
     import matplotlib.pyplot as plt
     plt.gcf().clear()
     print("hist time")
    
     line=list(code)
   
     print("line is ",line)
     d = dict(Counter(line))
     print("d is ",d)
     #del d['\n']
     plt.bar(list(d.keys()), d.values(), color='b')
     plt.xlabel("code")
     plt.ylabel("frequency")
     #plt.plot()
   
     plt.savefig("hist.png")
     plt.gcf().clear()
     fname = open("hist.png")
        
     print("pass")
     self.scene=QGraphicsScene()
     self.scene.addPixmap(QPixmap("hist.png"))
     self.graphicsView.setScene(self.scene)

     
       
       
    
    def freeman(self,img):
      print("image path is ",img)
      image =  cv2.imread(img,0)
      print(image)
      #print(image.shape())
      print("passed image loading")
      #image = cv2.dilate(image,np.ones((3,3),np.uint8),iterations=1)
      resized_image = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
      ret,img = cv2.threshold(resized_image,127,255,0)
      image_dilated = cv2.dilate(img,np.ones((3,3),np.uint8),iterations=1)
      for i  in range(len(image_dilated)):
          image_dilated[i, 0] = 0
          image_dilated[i, len(image_dilated)-1] = 0
          image_dilated[0, i] = 0
          image_dilated[len(image_dilated)-1,i] = 0
      connectivity = 4  
      output = cv2.connectedComponentsWithStats(image_dilated, connectivity, cv2.CV_32S)
      num_labels = output[0]
      final_image = output[1]
      stats = output[2]
      max_area = np.argmax(stats[1:].max(axis=1)) + 1
      for i in range(1,num_labels):
        if (max_area == i):
            final_image[final_image == i] = 255
        else:
            final_image[final_image == i] = 0
      for i, row in enumerate(final_image):
        for j, value in enumerate(row):
            if value == 255 or value == 1 :
                initial_point = (i, j)
                break
            else:
              continue
            break
    
      NEWS = [ 0,  1,  2,
                     7,      3,
                     6,  5,  4]
      dir2idx = dict(zip(NEWS, range(len(NEWS))))

      change_j =   [-1,  0,  1, # x or columns
                    -1,      1,
                    -1,  0,  1]

      change_i =   [-1, -1, -1, # y or rows
                     0,      0,
                     1,  1,  1]

      outline = []
      freeman = []
      curr_point = initial_point
      for NEWS in NEWS:
        idx = dir2idx[NEWS]
        new_point = (initial_point[0]+change_i[idx], initial_point[1]+change_j[idx])
        if final_image[new_point] != 0: # if is ROI
            outline.append(new_point)
            freeman.append(NEWS)
            current = new_point
            break

      count = 0
      while current != initial_point:
        b_direction = (NEWS + 5) % 8 
        dirs_1 = range(b_direction,8)
        dirs_2 = range(0, b_direction)
        dirs = []
        dirs.extend(dirs_1)
        dirs.extend(dirs_2)
        for NEWS in dirs:
            idx = dir2idx[NEWS]
            new_point = (curr_point[0]+change_i[idx], current[1]+change_j[idx])
            if final_image[new_point] != 0:
                outline.append(new_point)
                freeman.append(NEWS)
                current = new_point
                break
        if count == 1000: break
        count += 1
      #
      return outline,freeman,final_image
    
   
    
    def draw(self,img):
        
        pattern,code,label = self.freeman(img) 
        
        code2=", ".join( repr(e) for e in code )
        code2 = code2.replace(',', '')
        print("code1 is ",code)
        print("code 2 is ",code2 )
        print("type of code2 is ",type(code2))
        code3=code2.replace(' ','')
        print("code3 is ",code3)
        print("type of code3 is ",type(code3))
        #print("label is ",label)
        na = plt.imshow(label,cmap='Greys')
        plt.plot([i[1] for i in pattern],[i[0] for i in pattern ])
        #plt.show()   
    
        plt.savefig('foo.png')
        plt.gcf().clear()
        fname = open('foo.png')
        #print(self.pushButton.setText("ee"))
        print("pass")
        self.scene=QGraphicsScene()
        self.scene.addPixmap(QPixmap('foo.png'))
        self.graphicsView_2.setScene(self.scene)
        #codestr=(", ".join(code))
        codestr=str(code)
        self.textBrowser.setHtml(code2)
        
       
        self.CreateHist(code3)
  
        df2=np.array(code)
        df1=pd.read_csv("/Users/vipulvijigiri/Data_200_12/myseq_train_set02_200_12.csv").values
        df=pd.read_csv("/Users/vipulvijigiri/Data_200_12/my_labels_200_12.csv").values
        algo,digit,train,dist1,example=self.get_neighbors(df1,df,df2,1)
        print("the digit is ",digit)
        digit2=str(digit)
        print(type(digit2))
        
        
        if "1" in digit2:  
          print("yeah it is 1")  
          fileName2="1.png"
          self.printsimilair(fileName2)
          
        if "2" in digit2:
          print("it is 2")  
          fileName2="2.png"
          self.printsimilair(fileName2)
        if "3" in digit2:
          print("it is 3")  
          fileName2="3.png"
          self.printsimilair(fileName2)  
        if "4" in digit2:
          print("it is 4")  
          fileName2="4.png"
          self.printsimilair(fileName2)
        if "5" in digit2: #=="5":
          print("it is a 5")  
          fileName2="5.png"
          self.printsimilair(fileName2)  
        if "6" in digit2:
          print("it is a 6")
          fileName2="6.png"
          self.printsimilair(fileName2)  
        if "7" in digit2:#digit=="7":
          print("it is a 7")  
          fileName2="7.png"
          self.printsimilair(fileName2)  
        if "8" in digit2:#=="8":
          print("it is a 8")  
          fileName2="8.png"
          self.printsimilair(fileName2)  
        if "9" in digit2:#=="9":
          print("it is a 9")  
          fileName2="9.png"
          self.printsimilair(fileName2)  
        if "0" in digit2:
          print("it is a 0")  
          fileName2="0.png"
          self.printsimilair(fileName2)  
        
        








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
