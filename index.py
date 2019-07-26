# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import admin_login, student_login, about

class Ui_index(object):
    def openStudentLogin(self):
        self.window=QtWidgets.QWidget()
        self.ui=student_login.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        index.hide()
    def openAdminLogin(self):
        self.window1=QtWidgets.QWidget()
        self.ui1=admin_login.Ui_Form()
        self.ui1.setupUi(self.window1)
        self.window1.show()
        index.hide()
    def openAbout(self):
        self.window2=QtWidgets.QWidget()
        self.ui2=about.Ui_About()
        self.ui2.setupUi(self.window2)
        self.window2.show()
    def setupUi(self, index):
        index.setObjectName("index")
        index.resize(1030, 576)
        w=random.randint(1,6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(index.sizePolicy().hasHeightForWidth())
        index.setSizePolicy(sizePolicy)
        index.setMinimumSize(QtCore.QSize(1030, 576))
        index.setMaximumSize(QtCore.QSize(1030, 576))
        index.setSizeIncrement(QtCore.QSize(0, 0))
        index.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/APP ICON_EDIT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        index.setWindowIcon(icon)
        font.setFamily("Coolvetica")
        font.setPointSize(30)
        index.setFont(font)
        index.setAutoFillBackground(True)
        index.setStyleSheet("")
        self.aboutLink = QtWidgets.QPushButton(index)
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
        self.label = QtWidgets.QLabel(index)
        self.label.setGeometry(QtCore.QRect(0, 0, 1031, 581))
        self.label.setStyleSheet("border-image: url(:/Wallpaper/w"+str(w)+".jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.student = QtWidgets.QPushButton(index)
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
        self.admin = QtWidgets.QPushButton(index)
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
        self.retranslateUi(index)
        QtCore.QMetaObject.connectSlotsByName(index)

    def retranslateUi(self, index):
        _translate = QtCore.QCoreApplication.translate
        index.setWindowTitle(_translate("index", "ICLog"))
        self.aboutLink.setText(_translate("index", "ICLog"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    index = QtWidgets.QWidget()
    ui = Ui_index()
    ui.setupUi(index)
    index.show()
    sys.exit(app.exec_())

