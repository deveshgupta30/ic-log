# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ICLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import admin_login, student_login, about

class Ui_ICLog(object):
    def openStudentLogin(self):
        self.window=QtWidgets.QWidget()
        self.ui=student_login.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        ICLog.hide()
    def openAdminLogin(self):
        self.window1=QtWidgets.QWidget()
        self.ui1=admin_login.Ui_Form()
        self.ui1.setupUi(self.window1)
        self.window1.show()
        ICLog.hide()
    def openAbout(self):
        self.window2=QtWidgets.QWidget()
        self.ui2=about.Ui_About()
        self.ui2.setupUi(self.window2)
        self.window2.show()
    def setupUi(self, ICLog):
        ICLog.setObjectName("ICLog")
        ICLog.resize(1030, 576)
        w=random.randint(1,6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ICLog.sizePolicy().hasHeightForWidth())
        ICLog.setSizePolicy(sizePolicy)
        ICLog.setMinimumSize(QtCore.QSize(1030, 576))
        ICLog.setMaximumSize(QtCore.QSize(1030, 576))
        ICLog.setSizeIncrement(QtCore.QSize(0, 0))
        ICLog.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/APP ICON_EDIT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ICLog.setWindowIcon(icon)
        font.setFamily("Coolvetica")
        font.setPointSize(30)
        ICLog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ICLog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ICLog.setFont(font)
        ICLog.setAutoFillBackground(True)
        ICLog.setStyleSheet("")
        self.aboutLink = QtWidgets.QPushButton(ICLog)
        self.aboutLink.setGeometry(QtCore.QRect(400, 10, 200, 80))
        self.aboutLink.setAutoFillBackground(False)
        self.aboutLink.setStyleSheet("#aboutLink{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"    font: 36pt \"Slate For OnePlus Bk\";\n"
"\n"
"}\n"
"#aboutLink:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #e3f2fd;\n"
"    font: 36pt \"Slate For OnePlus Bk\";\n"
"\n"
"\n"
"}\n"
"#aboutLink:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #04326D;\n"
"font: 36pt \"Slate For OnePlus Bk\";\n"
"\n"
"}\n"
"")
        self.aboutLink.setObjectName("aboutLink")
        self.label = QtWidgets.QLabel(ICLog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1030, 576))
        self.label.setStyleSheet("#label{\n"
"border-image: url(:/Wallpaper/w"+str(w)+".jpg);\n"
"\n"
"border-radius:15px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.student = QtWidgets.QPushButton(ICLog)
        self.student.setGeometry(QtCore.QRect(550, 150, 312, 321))
        self.student.setMinimumSize(QtCore.QSize(300, 300))
        self.student.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.student.setMouseTracking(True)
        self.student.setStyleSheet("background-color: transparent;\n"
"border-image: transparent;")
        self.student.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/student/student_metro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.student.setIcon(icon)
        self.student.setIconSize(QtCore.QSize(300, 300))
        self.student.setObjectName("student")
        self.exitWindow = QtWidgets.QPushButton(ICLog)
        self.exitWindow.setGeometry(QtCore.QRect(1000, 10, 21, 21))
        self.exitWindow.setStyleSheet("#exitWindow{\n"
"border-image: url(:/Window/Circle Close - 01.png);\n"
"background-color: transparent;\n"
"}\n"
"#exitWindow:hover{\n"
"border-image: url(:/Window/Circle Close - 02.png);\n"
"background-color: transparent;\n"
"}\n"
"#exitWindow:pressed{\n"
"border-image: url(:/Window/Circle Close - 03.png);\n"
"background-color: transparent;\n"
"}")
        self.exitWindow.setText("")
        self.exitWindow.setObjectName("exitWindow")
        self.admin = QtWidgets.QPushButton(ICLog)
        self.admin.setGeometry(QtCore.QRect(150, 160, 312, 308))
        self.admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.admin.setMouseTracking(True)
        self.admin.setStyleSheet("background-color: transparent;\n"
"border-image:transparent;")
        self.admin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/admin/admin_metro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.admin.setIcon(icon1)
        self.admin.setIconSize(QtCore.QSize(300, 300))
        self.admin.setAutoDefault(False)
        self.admin.setDefault(False)
        self.admin.setFlat(False)
        self.admin.setObjectName("admin")
        self.label.raise_()
        self.aboutLink.raise_()
        self.student.raise_()
        self.admin.raise_()
        self.admin.clicked.connect(self.openAdminLogin)
        self.student.clicked.connect(self.openStudentLogin)
        self.aboutLink.clicked.connect(self.openAbout)
        self.retranslateUi(ICLog)
        QtCore.QMetaObject.connectSlotsByName(ICLog)
        self.exitWindow.raise_()
        self.exitWindow.clicked.connect(ICLog.close)

    def retranslateUi(self, ICLog):
        _translate = QtCore.QCoreApplication.translate
        ICLog.setWindowTitle(_translate("ICLog", "ICLog"))
        self.aboutLink.setText(_translate("ICLog", "ICLog"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ICLog = QtWidgets.QWidget()
    ui = Ui_ICLog()
    ui.setupUi(ICLog)
    ICLog.show()
    sys.exit(app.exec_())

