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
        Form.resize(411, 601)
        Form.setMinimumSize(QtCore.QSize(411, 601))
        Form.setMaximumSize(QtCore.QSize(411, 601))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        Form.setStyleSheet("")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(149, 430, 111, 45))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
        self.f_pass.setGeometry(QtCore.QRect(150, 480, 111, 28))
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
        self.label.setGeometry(QtCore.QRect(0, 120, 411, 81))
        self.label.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"\n"
"color: #00004f")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 111, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/admin/admin1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(79, 320, 251, 40))
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
        self.password.setGeometry(QtCore.QRect(79, 370, 251, 40))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 601))
        self.label_2.setStyleSheet("#label_2{\n"
"border-image: url(:/Wallpaper/l1w.png);\n"
"border-radius: 15px;\n"
"}")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.exitWindow = QtWidgets.QPushButton(Form)
        self.exitWindow.setGeometry(QtCore.QRect(380, 10, 21, 21))
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
        self.minWindow = QtWidgets.QPushButton(Form)
        self.minWindow.setGeometry(QtCore.QRect(350, 10, 21, 21))
        self.minWindow.setStyleSheet("#minWindow{\n"
"border-image: url(:/Window/Minus_1.png);\n"
"background-color: transparent;\n"
"}\n"
"#minWindow:hover{\n"
"border-image: url(:/Window/Minus_2.png);\n"
"background-color: transparent;\n"
"}\n"
"#minWindow:pressed{\n"
"border-image: url(:/Window/Minus_3.png);\n"
"background-color: transparent;\n"
"}")
        self.minWindow.setText("")
        self.minWindow.setObjectName("minWindow")
        self.label_2.raise_()
        self.login.raise_()
        self.f_pass.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.username.raise_()
        self.password.raise_()
        self.exitWindow.raise_()
        self.minWindow.raise_()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.exitWindow.clicked.connect(Form.close)
        self.minWindow.clicked.connect(Form.showMinimized)
        self.login.clicked.connect(lambda: self.checkAdminLogin(Form))
        self.f_pass.clicked.connect(self.openFPass)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def checkAdminLogin(self, Form):
        if(is_connected()==False):
            QtWidgets.QMessageBox.about(Form, "Error!", "Please connect to the Internet first!")
        else:
            import db
            try:
                a=db.adminLogin(self.username.text(), self.password.text())
                if a==True: 
                    self.openAdminPortal(Form)
                elif a==False:
                    QtWidgets.QMessageBox.about(Form, "Inorrect", "Your password is incorrect")
                else:
                    QtWidgets.QMessageBox.about(Form, "Error!", a)
            except:
                QtWidgets.QMessageBox.about(Form, "Error!", "We are facing some server side technical issues. Please try again later.")

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
        self.exitWindow.setShortcut(_translate("add_admin", "Esc"))
        self.login.setShortcut(_translate("Form", "Return"))
        self.f_pass.setText(_translate("Form", "Forgot Password?"))
        self.label.setText(_translate("Form", "Hello there, Admin!"))
        self.username.setPlaceholderText(_translate("Form", "E-Mail/Employee ID"))
        self.password.setPlaceholderText(_translate("Form", "Password"))

import icons_rc, socket

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

