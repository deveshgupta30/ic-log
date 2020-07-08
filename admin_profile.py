# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin_profile(object):
    def setupUi(self, admin_profile):
        admin_profile.setObjectName("admin_profile")
        admin_profile.resize(650, 550)
        admin_profile.setMinimumSize(QtCore.QSize(650, 550))
        admin_profile.setMaximumSize(QtCore.QSize(650, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_profile.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(admin_profile)
        self.closeButton.setGeometry(QtCore.QRect(260, 440, 121, 51))
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
        self.formLayoutWidget = QtWidgets.QWidget(admin_profile)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 230, 631, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelEid = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelEid.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelEid.setFont(font)
        self.labelEid.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelEid.setObjectName("labelEid")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelEid)
        self.showEid = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showEid.setFont(font)
        self.showEid.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showEid.setObjectName("showEid")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.showEid)
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
        self.labelLab = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLab.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelLab.setFont(font)
        self.labelLab.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelLab.setObjectName("labelLab")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelLab)
        self.showLab = QtWidgets.QLabel(self.formLayoutWidget)
        self.showLab.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showLab.setFont(font)
        self.showLab.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showLab.setObjectName("showLab")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.showLab)
        self.labelName = QtWidgets.QLabel(admin_profile)
        self.labelName.setGeometry(QtCore.QRect(0, 80, 651, 49))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #001970;\n"
"")
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName("labelName")
        self.label_4 = QtWidgets.QLabel(admin_profile)
        self.label_4.setGeometry(QtCore.QRect(280, 140, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/admin/admin.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(admin_profile)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Wallpaper/l3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.changePassword = QtWidgets.QPushButton(admin_profile)
        self.changePassword.setGeometry(QtCore.QRect(10, 430, 185, 41))
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
        self.label.raise_()
        self.closeButton.raise_()
        self.formLayoutWidget.raise_()
        self.labelName.raise_()
        self.label_4.raise_()
        self.changePassword.raise_()
        self.closeButton.clicked.connect(admin_profile.close)
        self.changePassword.clicked.connect(self.openChangePassword)
        self.retranslateUi(admin_profile)
        QtCore.QMetaObject.connectSlotsByName(admin_profile)

    def openChangePassword(self):
        from forgot_password_admin import Ui_forgotpassword  
        self.window2=QtWidgets.QWidget()
        self.ui2=Ui_forgotpassword()
        self.ui2.setupUi(self.window2)
        self.window2.show()     
              
    def setDetails(self, a):
        self.showEid.setText(a[0])
        self.labelName.setText(a[1])
        self.showEmail.setText(a[2])
        self.showContact.setText(a[3])
        self.showLab.setText(a[4])
        
    def retranslateUi(self, admin_profile):
        _translate = QtCore.QCoreApplication.translate
        admin_profile.setWindowTitle(_translate("admin_profile", "My Profile"))
        self.closeButton.setText(_translate("admin_profile", "CLOSE"))
        self.closeButton.setShortcut(_translate("admin_profile", "Esc"))
        self.labelEid.setText(_translate("admin_profile", "Employee ID:"))
        self.showEid.setText(_translate("admin_profile", "Reg. No."))
        self.labelEmail.setText(_translate("admin_profile", "E-Mail ID:"))
        self.showEmail.setText(_translate("admin_profile", "Please enter Student Registration No."))
        self.labelContact.setText(_translate("admin_profile", "Contact Number:"))
        self.showContact.setText(_translate("admin_profile", "Please enter Student Registration No."))
        self.labelLab.setText(_translate("admin_profile", "Lab:"))
        self.showLab.setText(_translate("admin_profile", "Lab"))
        self.labelName.setText(_translate("admin_profile", "My Profile"))
        self.changePassword.setText(_translate("admin_profile", "CHANGE PASSWORD"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_profile = QtWidgets.QWidget()
    ui = Ui_admin_profile()
    ui.setupUi(admin_profile)
    admin_profile.show()
    sys.exit(app.exec_())

