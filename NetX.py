# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admire.BLAZE.000\Desktop\QT\NetX\netx.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen
from qtmodern.styles import dark,light
from qtmodern.windows import ModernWindow
from Core import about
import os
import subprocess
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 518)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/netx.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Code = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.Code.setFont(font)
        self.Code.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Code.setPlainText("")
        self.Code.setCursorWidth(3)
        self.Code.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Code.setBackgroundVisible(False)
        self.Code.setCenterOnScroll(False)
        self.Code.setObjectName("Code")
        self.verticalLayout.addWidget(self.Code)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.Terminal = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Terminal.setEnabled(True)
        self.Terminal.setFrameShape(QtWidgets.QFrame.Box)
        self.Terminal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Terminal.setReadOnly(True)
        self.Terminal.setCursorWidth(0)
        self.Terminal.setBackgroundVisible(False)
        self.Terminal.setCenterOnScroll(True)
        self.Terminal.setObjectName("Terminal")
        self.verticalLayout.addWidget(self.Terminal)
        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(2, 10)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuRun = QtWidgets.QMenu(self.menuBar)
        self.menuRun.setObjectName("menuRun")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menuOptions.setTearOffEnabled(True)
        self.menuOptions.setSeparatorsCollapsible(True)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionRun_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/run_code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_2.setIcon(icon1)
        self.actionRun_2.setObjectName("actionRun_2")
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRun_2)
        self.menuOptions.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionRun_2.triggered.connect(self.run_code)
        self.actionAbout.triggered.connect(self.about)
		
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ".NetX"))
        self.Code.setToolTip(_translate("MainWindow", "Enter your code here"))
        self.Code.setStatusTip(_translate("MainWindow", "Console"))
        self.Code.setPlaceholderText(_translate("MainWindow", "Type Code here"))
        self.Terminal.setToolTip(_translate("MainWindow", "code results show up here"))
        self.Terminal.setStatusTip(_translate("MainWindow", "Console"))
        self.Terminal.setWhatsThis(_translate("MainWindow", "A console for showing core results"))
        self.Terminal.setPlaceholderText(_translate("MainWindow", "Terminal>>"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionRun_2.setText(_translate("MainWindow", "Run"))
        self.actionRun_2.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        os.chdir("core/xengine/temp/")
		
#import images_rc
    def run_code(self):
        
        code = self.Code.document().toPlainText()
        file = open("temp.cs","w")
        #file.write(code)
        #file.close()
        self.write_code(code,file)
        #compile_file = r"./core/xengine/temp/temp.cs"
        #print(os.getcwd())
        compile_ = subprocess.run("csc *.cs",stdout=subprocess.PIPE,shell=True).stdout.decode("utf-8")
        #print(compile_)
        #self.Terminal.setPlainText(f"{compile_}")
        sleep(0.3)
        results = subprocess.run("temp",stdout=subprocess.PIPE,shell=True).stdout.decode("utf-8")
        
        self.Terminal.setPlainText(f"{results}")
        subprocess.run("del temp.exe",stdout=subprocess.PIPE,shell=True).stdout.decode("utf-8")
        
    def write_code(self,code_txt,code_file):
        code_file.write(code_txt)
        code_file.close()
        return

    def about(self):
	    about.Frame.show()
		
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    dark(app)
    MainWindow.show()
    sys.exit(app.exec_())
