# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from admin_portal import Ui_student_portal
from forgot_password_admin import Ui_forgotpassword

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        Form.setMinimumSize(QtCore.QSize(400, 600))
        Form.setMaximumSize(QtCore.QSize(400, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(156, 430, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.login.setFont(font)
        self.login.setStyleSheet("\n"
"#login{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:qlineargradient(spread:pad, x1:0.462, y1:1, x2:0.487, y2:0, stop:0 rgba(0, 41, 132, 255), stop:1 rgba(66, 165, 245, 255));\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#login:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#login:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.login.setObjectName("login")
        self.f_pass = QtWidgets.QPushButton(Form)
        self.f_pass.setGeometry(QtCore.QRect(142, 470, 133, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setUnderline(True)
        self.f_pass.setFont(font)
        self.f_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.f_pass.setStyleSheet("color:rgb(0, 174, 255);\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"selection-color: transparent;\n"
"selection-background-color:transparent;\n"
"gridline-color: transparent;")
        self.f_pass.setObjectName("f_pass")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 120, 401, 81))
        self.label.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"\n"
"color: #00004f")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 180, 111, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/admin/admin1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Wallpaper/l1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(80, 320, 250, 40))
        self.username.setStyleSheet("#username{\n"
"background-color: white;\n"
"border-bottom-color: #001970;\n"
"border-top-color: transparent;\n"
"border-left-color: transparent;\n"
"border-right-color: transparent;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#username:hover {\n"
"    border-style: inset;\n"
"}\n"
"#username:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(80, 370, 250, 40))
        self.password.setStyleSheet("#password{\n"
"background-color: white;\n"
"border-bottom-color: #001970;\n"
"border-top-color: transparent;\n"
"border-left-color: transparent;\n"
"border-right-color: transparent;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#password:hover {\n"
"    border-style: inset;\n"
"}\n"
"#password:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.label_2.raise_()
        self.login.raise_()
        self.f_pass.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.username.raise_()
        self.password.raise_()
        self.login.clicked.connect(lambda: self.checkAdminLogin(Form))
        self.f_pass.clicked.connect(self.openFPass)
        self.retranslateUi(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def checkAdminLogin(self, Form):
        if(is_connected()==False):
            QtWidgets.QMessageBox.about(Form, "Error!", "Please connect to the Internet first!")
        else:
            import db
            a=db.adminLogin(self.username.text(), self.password.text())
            if a==True: 
                self.openAdminPortal(Form)
            elif a==False:
                QtWidgets.QMessageBox.about(Form, "Inorrect", "Your password is incorrect")
            else:
                QtWidgets.QMessageBox.about(Form, "Error!", a)
    def openAdminPortal(self,Form):

        import db
        self.eID=db.fetchE_ID(self.username.text())
        self.window1=QtWidgets.QMainWindow()
        self.ui1=Ui_student_portal()
        self.ui1.setupUi(self.window1)
        self.ui1.setEID(self.eID)
        self.ui1.setMame(str(db.fetchAdminName(self.eID)), self.window1)
        self.ui1.setTitle('Welcome, '+ str(db.fetchAdminName(self.eID))+ '!', self.window1)
        self.window1.show()
        lab=db.getAdminLabNumber(self.eID)
        self.ui1.setDashDetails(lab,db.getNoBorrowed(lab),db.getNoRequested(lab))
        Form.hide()
    def openFPass(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_forgotpassword()
        self.ui.setupUi(self.window)
        self.window.show()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Admin Login"))
        self.login.setText(_translate("Form", "LOGIN"))
        self.login.setShortcut(_translate("Form", "Return"))
        self.f_pass.setText(_translate("Form", "Forgot Password?"))
        self.label.setText(_translate("Form", "Hello there, Admin!"))
        self.username.setPlaceholderText(_translate("Form", "E-Mail/Employee ID"))
        self.password.setPlaceholderText(_translate("Form", "Password"))

import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

