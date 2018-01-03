import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np 
import cv2
import matplotlib.pyplot as plt


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

class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        h = 400
        w = 400
        self.myPenWidth = 13
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
        self.image.fill(Qt.black)  ## switch it to else
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

    def sizeHint(self):
        return QSize(300, 300)

#############################################################################################################


class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

################################################################################################################    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        fileName = 'Screenshot.png'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1807, 1607)
        #self.createActions()
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        #self.createActions()
        #self.createMenus()
        #self.createActions()
        #self.createMenus()
       #######################################################################################################""
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 1261, 641))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 281, 601))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 266, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 85, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 20, 85, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(570, 20, 37, 27))
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


        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(330, 70, 381, 291))
        self.graphicsView.setObjectName("graphicsView")

        
        self.pushButton_14 = QtWidgets.QPushButton(self.tab)
        self.pushButton_14.setGeometry(QtCore.QRect(640, 20, 85, 27))
        self.pushButton_14.setObjectName("pushButton_14")



        self.tabWidget.addTab(self.tab, "")
##################################################################################""

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)#,Qt.AlignmentLeft)
        
        self.graphicsView2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView2.setGeometry(QtCore.QRect(870, 40, 300, 300))
        self.graphicsView2.setObjectName("graphicsView2")
        
        self.graphicsView3 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView3.setGeometry(QtCore.QRect(170, 10, 300, 300))
        self.graphicsView3.setObjectName("graphicsView3")
        
        self.graphicsView4 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView4.setGeometry(QtCore.QRect(70, 320, 300, 300))
        self.graphicsView4.setObjectName("graphicsView4")
        
        
        
        #self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        #self.pushButton_15.setSizePolicy(sizePolicy2)
        #self.pushButton_15.setObjectName("pushButton_15")
        #self.gridLayout.addWidget(self.pushButon_15,2,0,1,1)
        
        self.draw2=Drawer(self.tab_2)
        self.draw2.clearImage()
        #self.draw = Drawer(self.tab_2)
        #self.scribbleArea.clearImage()
        self.draw2.mainWindow = self  # maybe not using this?
        #self.tab_2.setCentralWidget(self.scribbleArea)
        self.draw2.setObjectName("drawArea2")
        #self.draw.setBackground(self,QtGui.QColor(0,0,0), QtCore.Qt.SolidPattern)
        al=QtCore.Qt.AlignCenter
        self.gridLayout.addWidget(self.draw2, 4, 1, 1, 1,al)

        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setSizePolicy(sizePolicy2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 0, 1, 1)


        self.tabWidget.addTab(self.tab_2, "")

#####################################################################################""



        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        sizePolicy3 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.draw3=Drawer(self.tab_3)
        self.draw3.mainWindow = self  # maybe not using this?
        #self.tab_2.setCentralWidget(self.scribbleArea)
        self.draw3.setObjectName("drawArea3")
        self.draw3.clearImage()
        #self.draw.setBackground(self,QtGui.QColor(0,0,0), QtCore.Qt.SolidPattern)
        al=QtCore.Qt.AlignCenter
        self.gridLayout_2.addWidget(self.draw3, 2, 1, 1, 1,al)
        self.tabWidget.addTab(self.tab_3, "")




        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        #self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_6.setObjectName("pushButton_6")
        #self.gridLayout_4.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        sizePolicy4 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        #self.pushButton_7.setGeometry(QtCore.QRect(260, 60, 99, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_8.setGeometry(QtCore.QRect(260, 110, 99, 27))
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_9.setGeometry(QtCore.QRect(260, 170, 99, 27))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setSizePolicy(sizePolicy4)
        self.gridLayout_4.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_10.setGeometry(QtCore.QRect(260, 230, 99, 27))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setSizePolicy(sizePolicy4)
        self.gridLayout_4.addWidget(self.pushButton_10, 3, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_11.setGeometry(QtCore.QRect(260, 280, 99, 27))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setSizePolicy(sizePolicy4)
        self.gridLayout_4.addWidget(self.pushButton_11, 4, 1, 1, 1)
        #self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        #self.pushButton_12.setGeometry(QtCore.QRect(260, 280, 99, 27))
        #self.pushButton_12.setObjectName("pushButton_12")
        #self.pushButton_12.setSizePolicy(sizePolicy4)
        #self.gridLayout_4.addWidget(self.pushButton_12, 5, 1, 1, 1)

        self.draw4=Drawer(self.tab_4)
        self.draw4.mainWindow = self  # maybe not using this?
        #self.tab_2.setCentralWidget(self.scribbleArea)
        self.draw4.setObjectName("drawArea4")
        self.draw4.clearImage()
        #self.draw.setBackground(self,QtGui.QColor(0,0,0), QtCore.Qt.SolidPattern)
        #al=QtCore.Qt.AlignCenter
        #self.gridLayout_4.addWidget(self.draw4, 0, 0, 1, 1)#,al)
        #self.gridLayout_4.addWidget(self.pushButton_12, 5, 1, 1, 1)
        self.draw5=Drawer(self.tab_4)
        self.draw5.mainWindow = self  # maybe not using this?
        #self.tab_2.setCentralWidget(self.scribbleArea)
        self.draw5.setObjectName("drawArea5")
        self.draw5.clearImage()
        #self.draw.setBackground(self,QtGui.QColor(0,0,0), QtCore.Qt.SolidPattern)
        #al=QtCore.Qt.AlignCenter
        #self.gridLayout_4.addWidget(self.draw5, 0, 2, 1, 1)#,al)

        self.display = QLineEdit('Result')
        self.display.setReadOnly(True)
        #self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(7)
        self.gridLayout_4.addWidget(self.draw4, 0, 0, 1, 1)#,al)
        #self.gridLayout_4.addWidget(self.pushButton_12, 5, 1, 1, 1)

        self.gridLayout_4.addWidget(self.draw5, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.display,6,1,1,1)





        self.tabWidget.addTab(self.tab_4, "")



####################################################################################


        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 707, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "import"))
        self.pushButton.clicked.connect(self.SingleBrowse)
        self.pushButton_2.setText(_translate("MainWindow", "add"))
        self.pushButton_14.setText(_translate("MainWindow", "Filter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "DataBase"))
        self.pushButton_5.setText(_translate("MainWindow", "Clear Board"))
        self.pushButton_5.clicked.connect(self.draw2.clearImage)
        self.pushButton_3.setText(_translate("MainWindow", "save image"))
        #self.pushButton_3.clicked.connect(self.saveFile)
        self.pushButton_3.clicked.connect(lambda: self.draw2.saveImage("image.png", "PNG"))
        #btnSave.clicked.connect(lambda: drawer.saveImage("image.png", "PNG"))
        #btnClear.clicked.connect(drawer.clearImage)
        self.pushButton_4.setText(_translate("MainWindow", "classify"))
        self.pushButton_4.clicked.connect(self.classify)
        #self.pushButton_15.setText(_translate("MainWindow", "save"))
        self.pushButton_13.setText(_translate("MainWindow", "add"))
        #self.pushButton_13.clicked.connect(self.take_screenshot_draw)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Classification"))
        self.pushButton_6.setText(_translate("MainWindow", "Mine"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Pattern Mining"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "-"))
        self.pushButton_9.setText(_translate("MainWindow", "*"))
        self.pushButton_10.setText(_translate("MainWindow", "/"))
        self.pushButton_11.setText(_translate("MainWindow", "="))
        #self.pushButton_12.setText(_translate("MainWindow", "Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Calculator"))

   
    
    
    

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
        fileName="ar.png"
       
        self.draw2.saveImage(fileName,fileFormat)
        '''
        print("youpi")
        
        print(QtCore.QDir.currentPath())
        print("file format is ","PNG")
        initialPath = QtCore.QDir.currentPath() + '/untitled.' + 'PNG'

        #fileName = QtWidgets.QFileDialog.getSaveFileName(self, "Save As",
        #    initialPath,
        #    "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        fileName="test2.PNG"
        if fileName:
            return self.draw2.saveImage(fileName, fileFormat)
        
        return False
        '''

    def printsimilair(self,fileName):
       
        #self.fileName, _  = QFileDialog.getOpenFileName(None, 'Open file', '/home',filters,selected_filter)
        #if files:
        #print(fileName)
        
        #self.fileName=fileName 
        #print(self.fileName)#,_)
        fname = open(fileName)
        #print(self.pushButton.setText("ee"))
        print("pass")
        self.scene=QGraphicsScene()
        self.scene.addPixmap(QPixmap(fileName))
        self.graphicsView2.setScene(self.scene)



    def classify(self):
       fileName="1.png"
       self.printsimilair(fileName)
       
       
       
    def CreateHist(self):
    
     from collections import Counter
     import linecache
     import matplotlib.pyplot as plt    
     line = linecache.getline(self,1)
     line = list(line)
    
     d = dict(Counter(line))
     del d['\n']
     plt.bar(list(d.keys()), d.values(), color='b')
     plt.xlabel("code")
     plt.ylabel("frequency")
     plt.show()

#digit_zero=CreateHist('/home/dell1/Desktop/hist.txt')    
       
    
    def freeman(self,img):
      image =  cv2.imread(img,0)
      #image = cv2.dilate(image,np.ones((3,3),np.uint8),iterations=1)
      resized = cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)
      ret,img = cv2.threshold(resized,127,255,0)
      image = cv2.dilate(img,np.ones((3,3),np.uint8),iterations=1)
      for i  in range(len(image)):
          image[i, 0] = 0
          image[i, len(image)-1] = 0
          image[0, i] = 0
          image[len(image)-1,i] = 0
      connectivity = 4  
      output = cv2.connectedComponentsWithStats(image, connectivity, cv2.CV_32S)
      num_labels = output[0]
      labels = output[1]
      stats = output[2]
      max_area = np.argmax(stats[1:].max(axis=1)) + 1
      for i in range(1,num_labels):
        if (max_area == i):
            labels[labels == i] = 255
        else:
            labels[labels == i] = 0
      for i, row in enumerate(labels):
        for j, value in enumerate(row):
            if value == 255 or value == 1 :
                start_point = (i, j)
                break
            else:
              continue
            break
    
      directions = [ 0,  1,  2,
                     7,      3,
                     6,  5,  4]
      dir2idx = dict(zip(directions, range(len(directions))))

      change_j =   [-1,  0,  1, # x or columns
                    -1,      1,
                    -1,  0,  1]

      change_i =   [-1, -1, -1, # y or rows
                     0,      0,
                     1,  1,  1]

      border = []
      chain = []
      curr_point = start_point
      for direction in directions:
        idx = dir2idx[direction]
        new_point = (start_point[0]+change_i[idx], start_point[1]+change_j[idx])
        if labels[new_point] != 0: # if is ROI
            border.append(new_point)
            chain.append(direction)
            curr_point = new_point
            break

      count = 0
      while curr_point != start_point:
        b_direction = (direction + 5) % 8 
        dirs_1 = range(b_direction,8)
        dirs_2 = range(0, b_direction)
        dirs = []
        dirs.extend(dirs_1)
        dirs.extend(dirs_2)
        for direction in dirs:
            idx = dir2idx[direction]
            new_point = (curr_point[0]+change_i[idx], curr_point[1]+change_j[idx])
            if labels[new_point] != 0:
                border.append(new_point)
                chain.append(direction)
                curr_point = new_point
                break
        if count == 1000: break
        count += 1
      self.CreateHist('/home/dell1/Desktop/MLpr/hist.txt')   
      return border,chain,labels
    
    
    
    
    
    
    def draw(self,img):
      
      
      pattern,code,label = self.freeman(img)   
      na = plt.imshow(label,cmap='Greys')
      plt.plot([i[1] for i in pattern],[i[0] for i in pattern ])
      plt.show()   
   
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





 #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")