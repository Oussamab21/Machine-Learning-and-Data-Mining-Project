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




class Drawer(QWidget):
    newPoint = pyqtSignal(QPoint)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        imageSize = QtCore.QSize(9500, 9500)
        h=400
        w=400
        self.myPenWidth = 8
        self.myPenColor = QtCore.Qt.black
        self.image = QtGui.QImage()
        self.image=QtGui.QImage(w,h,QtGui.QImage.Format_RGB32)



        self.path = QPainterPath()   


    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.path = QPainterPath() 
        self.image.fill(QtGui.qRgb(255, 255, 255))  ## switch it to else 
        self.modified = True
        self.update()

    


    def paintEvent(self, event):
        painter = QPainter(self)
        
        #painter.setPen(QColor(0, 0, 0))
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        #painter.setFont(QFont('Decorative', 10))
        painter.drawImage(event.rect(), self.image)
        painter.drawPath(self.path)

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())
        self.update()

    def sizeHint(self):
        return QSize(200, 200)

    
   
    
'''
#class MyWidget(QWidget):
 #   def __init__(self, parent=None):
 #       QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        label = QLabel(self)
        drawer = Drawer(self)
        drawer.newPoint.connect(lambda p: label.setText('Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.layout().addWidget(label)
        self.layout().addWidget(drawer)
        #p = self.palette()
        #p.setColor(self.backgroundRole(), Qt.red)
        #self.setPalette(p)
   # def clearb(self):#,event):
       # paintEvent(self.draw,event)
   #     self.update()
   #     print("clear")  
   
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        filename = 'Screenshot.jpg'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1807, 1607)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
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
        self.pushButton_3.setText(_translate("MainWindow", "import"))
        self.pushButton_4.setText(_translate("MainWindow", "classify"))
        self.pushButton_13.setText(_translate("MainWindow", "add"))
        self.pushButton_13.clicked.connect(self.take_screenshot_draw)
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

    def take_screenshot_draw(self,MainWindow):
        #screen=QScreen()#QtGuiApplication.primaryScreen())
        im = QtGui.QScreen("fichierImage") 
        p = im.grabWindow(draw2.winId())
        p.save(filename, 'jpg')
        print("snapshoot")

   # def clearI(self,MainWindow):
   #     self.draw2.clearImage
    '''
    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def open(self):
        if self.maybeSave():
            fileName = QtGui.QFileDialog.getOpenFileName(self, "Open File",
                QtCore.QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QtGui.QInputDialog.getInteger(self, "Scribble",
            "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    def about(self):
        QtGui.QMessageBox.about(self, "About Scribble",
            "<p>The <b>Scribble</b> example shows how to use "
            "QMainWindow as the base widget for an application, and how "
            "to reimplement some of QWidget's event handlers to receive "
            "the events generated for the application's widgets:</p>"
            "<p> We reimplement the mouse event handlers to facilitate "
            "drawing, the paint event handler to update the application "
            "and the resize event handler to optimize the application's "
            "appearance. In addition we reimplement the close event "
            "handler to intercept the close events before terminating "
            "the application.</p>"
            "<p> The example also demonstrates how to use QPainter to "
            "draw an image in real time, as well as to repaint "
            "widgets.</p>")

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O",
            triggered=self.open)

        for format in QtGui.QImageWriter.supportedImageFormats():
            format = str(format)

            text = format.upper() + "..."

            action = QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QAction("&Print...", self,
            triggered=self.scribbleArea.print_)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
            triggered=self.close)

        self.penColorAct = QAction("&Pen Color...", self,
            triggered=self.penColor)

        self.penWidthAct = QAction("Pen &Width...", self,
            triggered=self.penWidth)

        self.clearScreenAct = QAction("&Clear Screen", self,
            shortcut="Ctrl+L", triggered=self.scribbleArea.clearImage)

        self.aboutAct = QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
            triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.saveAsMenu = QtGui.QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QtGui.QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QtGui.QMenu("&Help", self)
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

    def maybeSave(self):
        if self.scribbleArea.isModified():
            ret = QtGui.QMessageBox.warning(self, "Scribble",
                "The image has been modified.\n"
                "Do you want to save your changes?",
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                QtGui.QMessageBox.Cancel)
            if ret == QtGui.QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QtGui.QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):
        initialPath = QtCore.QDir.currentPath() + '/untitled.' + fileFormat

        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As",
            initialPath,
            "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))
        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False



    '''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





 #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")