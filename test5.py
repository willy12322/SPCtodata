# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DialIndicator = QtWidgets.QGraphicsView(self.centralwidget)
        self.DialIndicator.setGeometry(QtCore.QRect(820, 110, 741, 631))
        self.DialIndicator.setObjectName("DialIndicator")
        self.ReferenceTiltAngle_y = QtWidgets.QGraphicsView(self.centralwidget)
        self.ReferenceTiltAngle_y.setGeometry(QtCore.QRect(230, 110, 350, 300))
        self.ReferenceTiltAngle_y.setObjectName("ReferenceTiltAngle_y")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1150, 230, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1340, 520, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(960, 520, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.DialIndicator_12 = QtWidgets.QLabel(self.centralwidget)
        self.DialIndicator_12.setGeometry(QtCore.QRect(1110, 310, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DialIndicator_12.setFont(font)
        self.DialIndicator_12.setAlignment(QtCore.Qt.AlignCenter)
        self.DialIndicator_12.setObjectName("DialIndicator_12")
        self.DialIndicator_04 = QtWidgets.QLabel(self.centralwidget)
        self.DialIndicator_04.setGeometry(QtCore.QRect(1210, 460, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DialIndicator_04.setFont(font)
        self.DialIndicator_04.setAlignment(QtCore.Qt.AlignCenter)
        self.DialIndicator_04.setObjectName("DialIndicator_04")
        self.DialIndicator_08 = QtWidgets.QLabel(self.centralwidget)
        self.DialIndicator_08.setGeometry(QtCore.QRect(1000, 460, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DialIndicator_08.setFont(font)
        self.DialIndicator_08.setAlignment(QtCore.Qt.AlignCenter)
        self.DialIndicator_08.setObjectName("DialIndicator_08")
        self.value_12 = QtWidgets.QLabel(self.centralwidget)
        self.value_12.setGeometry(QtCore.QRect(1110, 350, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.value_12.setFont(font)
        self.value_12.setAlignment(QtCore.Qt.AlignCenter)
        self.value_12.setObjectName("value_12")
        self.value_04 = QtWidgets.QLabel(self.centralwidget)
        self.value_04.setGeometry(QtCore.QRect(1210, 430, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.value_04.setFont(font)
        self.value_04.setAlignment(QtCore.Qt.AlignCenter)
        self.value_04.setObjectName("value_04")
        self.value_08 = QtWidgets.QLabel(self.centralwidget)
        self.value_08.setGeometry(QtCore.QRect(1000, 430, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.value_08.setFont(font)
        self.value_08.setAlignment(QtCore.Qt.AlignCenter)
        self.value_08.setObjectName("value_08")
        self.ReferenceTiltAngle_x = QtWidgets.QGraphicsView(self.centralwidget)
        self.ReferenceTiltAngle_x.setGeometry(QtCore.QRect(230, 470, 350, 300))
        self.ReferenceTiltAngle_x.setObjectName("ReferenceTiltAngle_x")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1010, 50, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 40, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 410, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 220, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 580, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(130, 580, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 110, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.x_value = QtWidgets.QLabel(self.centralwidget)
        self.x_value.setGeometry(QtCore.QRect(230, 470, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.x_value.setFont(font)
        self.x_value.setAlignment(QtCore.Qt.AlignCenter)
        self.x_value.setObjectName("x_value")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 20, 161, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "12 o\'clock"))
        self.label_2.setText(_translate("MainWindow", "04 o\'clock"))
        self.label_3.setText(_translate("MainWindow", "08 o\'clock"))
        self.DialIndicator_12.setText(_translate("MainWindow", "DialIndicator_12"))
        self.DialIndicator_04.setText(_translate("MainWindow", "DialIndicator_04"))
        self.DialIndicator_08.setText(_translate("MainWindow", "DialIndicator_08"))
        self.value_12.setText(_translate("MainWindow", "value12_wait"))
        self.value_04.setText(_translate("MainWindow", "value04_wait"))
        self.value_08.setText(_translate("MainWindow", "value08_wait"))
        self.label_4.setText(_translate("MainWindow", "DialIndicator_Value"))
        self.label_5.setText(_translate("MainWindow", "Reference_Roll_Value"))
        self.label_6.setText(_translate("MainWindow", "Reference_Pitch_Value"))
        self.label_7.setText(_translate("MainWindow", "y_12 o\'clock"))
        self.label_8.setText(_translate("MainWindow", "y_06 o\'clock"))
        self.label_9.setText(_translate("MainWindow", "x_03 o\'clock"))
        self.label_10.setText(_translate("MainWindow", "x_09 o\'clock"))
        self.label_11.setText(_translate("MainWindow", "y_value"))
        self.x_value.setText(_translate("MainWindow", "x_value"))
        self.pushButton.setText(_translate("MainWindow", "Read data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
