# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(370, 450)
        Frame.setMinimumSize(QtCore.QSize(370, 450))
        Frame.setMaximumSize(QtCore.QSize(370, 450))
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 101))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 110, 371, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(75, 0, 30, 0)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_11)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "About"))
        self.label.setText(_translate("Frame", "<html><head/><body><p><img src=\":/images/icons/NETX2.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name:</span></p></body></html>"))
        self.label_7.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt;\">.NetX</span></p></body></html>"))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Version:</span></p></body></html>"))
        self.label_8.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt;\">1.0.0</span></p></body></html>"))
        self.label_9.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt;\">BETA</span></p></body></html>"))
        self.label_10.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt;\">2020.1.0</span></p></body></html>"))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Build:</span></p></body></html>"))
        self.label_5.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State:</span></p></body></html>"))
        self.label_6.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Developer:</span></p></body></html>"))
        self.label_11.setText(_translate("Frame", "<html><head/><body><p><a href=\"https://softaz.herokuapp.com/.netx\"><span style=\" font-size:12pt; text-decoration: underline; color:#00eb72;\">Softaz</span></a></p></body></html>"))
#import images_rc


#if __name__ == "__main__":
import sys
app = QtWidgets.QApplication(sys.argv)
Frame = QtWidgets.QFrame()
ui = Ui_Frame()
ui.setupUi(Frame)
#Frame.show()
#sys.exit(app.exec_())
