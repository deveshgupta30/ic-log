# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from forgot_password import Ui_forgotpassword
from requested_component import Ui_requestedComp
import borrowed_component
class Ui_student_profile(object):
    def setupUi(self, student_profile):
        student_profile.setObjectName("student_profile")
        student_profile.resize(700, 600)
        student_profile.setMinimumSize(QtCore.QSize(700, 600))
        student_profile.setMaximumSize(QtCore.QSize(700, 600))
        self.closeButton = QtWidgets.QPushButton(student_profile)
        self.closeButton.setGeometry(QtCore.QRect(290, 490, 121, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/student/Student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_profile.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("#closeButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 20px;\n"
"}\n"
"#closeButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#closeButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.formLayoutWidget = QtWidgets.QWidget(student_profile)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 240, 661, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelRno = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelRno.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelRno.setFont(font)
        self.labelRno.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelRno.setObjectName("labelRno")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelRno)
        self.showRno = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showRno.setFont(font)
        self.showRno.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showRno.setObjectName("showRno")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.showRno)
        self.labelEmail = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelEmail.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelEmail.setFont(font)
        self.labelEmail.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelEmail.setObjectName("labelEmail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelEmail)
        self.showEmail = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showEmail.setFont(font)
        self.showEmail.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showEmail.setObjectName("showEmail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.showEmail)
        self.labelContact = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelContact.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelContact.setFont(font)
        self.labelContact.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelContact.setObjectName("labelContact")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelContact)
        self.showContact = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showContact.setFont(font)
        self.showContact.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showContact.setObjectName("showContact")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.showContact)
        self.showName = QtWidgets.QLabel(student_profile)
        self.showName.setGeometry(QtCore.QRect(0, 80, 701, 49))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showName.setFont(font)
        self.showName.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #001970;\n"
"")
        self.showName.setAlignment(QtCore.Qt.AlignCenter)
        self.showName.setObjectName("showName")
        self.label_4 = QtWidgets.QLabel(student_profile)
        self.label_4.setGeometry(QtCore.QRect(310, 150, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/student/Student.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.changePassword = QtWidgets.QPushButton(student_profile)
        self.changePassword.setGeometry(QtCore.QRect(10, 420, 185, 41))
        self.changePassword.setStyleSheet("#changePassword{\n"
"background-color:white;\n"
"color:#0277BD;\n"
"    font: 57 7pt \"Slate For OnePlus Medium\";\n"
"    color: #0277BD;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"#changePassword:hover{\n"
"background-color:#01579B;\n"
"    font: 87 7pt \"Slate For OnePlus Medium\";\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#changePassword:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.changePassword.setObjectName("changePassword")
        self.borrowedComponents = QtWidgets.QPushButton(student_profile)
        self.borrowedComponents.setGeometry(QtCore.QRect(490, 420, 185, 41))
        self.borrowedComponents.setStyleSheet("#borrowedComponents{\n"
"background-color:white;\n"
"color:#0277BD;\n"
"    font: 57 7pt \"Slate For OnePlus Medium\";\n"
"    color: #0277BD;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"#borrowedComponents:hover{\n"
"background-color:#01579B;\n"
"    font: 87 7pt \"Slate For OnePlus Medium\";\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#borrowedComponents:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.borrowedComponents.setObjectName("borrowedComponents")
        self.requestedComponents = QtWidgets.QPushButton(student_profile)
        self.requestedComponents.setGeometry(QtCore.QRect(250, 420, 185, 41))
        self.requestedComponents.setStyleSheet("#requestedComponents{\n"
"background-color:white;\n"
"color:#0277BD;\n"
"    font: 57 7pt \"Slate For OnePlus Medium\";\n"
"    color: #0277BD;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"#requestedComponents:hover{\n"
"background-color:#01579B;\n"
"    font: 87 7pt \"Slate For OnePlus Medium\";\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 13px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#requestedComponents:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.requestedComponents.setObjectName("requestedComponents")
        self.label = QtWidgets.QLabel(student_profile)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Wallpaper/l4.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.closeButton.raise_()
        self.formLayoutWidget.raise_()
        self.showName.raise_()
        self.label_4.raise_()
        self.changePassword.raise_()
        self.borrowedComponents.raise_()
        self.requestedComponents.raise_()
        self.borrowedComponents.clicked.connect(self.openBorrowedComponents)
        self.requestedComponents.clicked.connect(self.openRequestedComponents)
        self.closeButton.clicked.connect(student_profile.close)
        self.changePassword.clicked.connect(self.openChangePassword)
        self.retranslateUi(student_profile)
        QtCore.QMetaObject.connectSlotsByName(student_profile)
    def openBorrowedComponents(self):
        import db
        self.window4=QtWidgets.QWidget()
        self.ui4=borrowed_component.Ui_requestComp()
        self.ui4.setupUi(self.window4)
        self.ui4.setDetails(list(db.getBorrowedComponents(self.showRno.text())))
        self.window4.show()                     
    def openRequestedComponents(self):
        import db
        self.window3=QtWidgets.QWidget()
        self.ui3=Ui_requestedComp()
        self.ui3.setupUi(self.window3)
        self.ui3.setDetails(list(db.getRequestedComponents(self.showRno.text())))
        self.window3.show()            
        
    def openChangePassword(self):
        self.window2=QtWidgets.QWidget()
        self.ui2=Ui_forgotpassword()
        self.ui2.setupUi(self.window2)
        self.window2.show()     
        
    def setDetails(self,a):
        self.showRno.setText(a[0])
        self.showName.setText(a[1])
        self.showEmail.setText(a[3])
        self.showContact.setText(a[2])
    def retranslateUi(self, student_profile):
        _translate = QtCore.QCoreApplication.translate
        student_profile.setWindowTitle(_translate("student_profile", "My Profile"))
        self.closeButton.setText(_translate("student_profile", "CLOSE"))
        self.closeButton.setShortcut(_translate("student_profile", "Esc"))
        self.labelRno.setText(_translate("student_profile", "Registration Number:"))
        self.showRno.setText(_translate("student_profile", "Reg. No."))
        self.labelEmail.setText(_translate("student_profile", "E-Mail ID:"))
        self.showEmail.setText(_translate("student_profile", "Please enter Student Registration No."))
        self.labelContact.setText(_translate("student_profile", "Contact Number:"))
        self.showContact.setText(_translate("student_profile", "Please enter Student Registration No."))
        self.showName.setText(_translate("student_profile", "My Profile"))
        self.changePassword.setText(_translate("student_profile", "CHANGE PASSWORD"))
        self.borrowedComponents.setText(_translate("student_profile", "BORROWED COMPONENTS"))
        self.requestedComponents.setText(_translate("student_profile", "REQUESTED COMPONENTS"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_profile = QtWidgets.QWidget()
    ui = Ui_student_profile()
    ui.setupUi(student_profile)
    student_profile.show()
    sys.exit(app.exec_())

