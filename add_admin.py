# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_admin(object):
    def setupUi(self, add_admin):
        add_admin.setObjectName("add_admin")
        add_admin.resize(650, 550)
        add_admin.setMinimumSize(QtCore.QSize(650, 550))
        add_admin.setMaximumSize(QtCore.QSize(650, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_admin.setWindowIcon(icon)
        self.confirmButton = QtWidgets.QPushButton(add_admin)
        self.confirmButton.setEnabled(True)
        self.confirmButton.setGeometry(QtCore.QRect(450, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.confirmButton.setFont(font)
        self.confirmButton.setStyleSheet("#confirmButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#confirmButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#confirmButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(add_admin)
        self.cancelButton.setGeometry(QtCore.QRect(550, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("#cancelButton{\n"
"background-color:white;\n"
"color:#0277BD;\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    color: #0277BD;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"#cancelButton:hover{\n"
"background-color:#01579B;\n"
"    font: 87 8pt \"Roboto Black\";\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#cancelButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.formLayoutWidget = QtWidgets.QWidget(add_admin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 631, 344))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.labelName = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelName.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.enterName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterName.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterName.setFont(font)
        self.enterName.setStyleSheet("#enterName{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterName:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterName:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterName.setClearButtonEnabled(True)
        self.enterName.setObjectName("enterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enterName)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
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
        self.enterEid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterEid.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterEid.setFont(font)
        self.enterEid.setStyleSheet("#enterEid{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterEid:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterEid:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterEid.setClearButtonEnabled(True)
        self.enterEid.setObjectName("enterEid")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enterEid)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem2)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelEmail)
        self.enterEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterEmail.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterEmail.setFont(font)
        self.enterEmail.setStyleSheet("#enterEmail{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterEmail:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterEmail:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterEmail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterEmail.setClearButtonEnabled(True)
        self.enterEmail.setObjectName("enterEmail")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.enterEmail)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem3)
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
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelContact)
        self.enterContact = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterContact.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterContact.setFont(font)
        self.enterContact.setStyleSheet("#enterContact{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterContact:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterContact:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterContact.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterContact.setClearButtonEnabled(True)
        self.enterContact.setObjectName("enterContact")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.enterContact)
        
        self.enterLab = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterLab.setMinimumSize(QtCore.QSize(0, 40))
        self.enterLab.setStyleSheet("#enterLab{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterLab:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterLab:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterLab.setClearButtonEnabled(True)
        self.enterLab.setObjectName("enterLab")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.enterLab)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelLab = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLab.setMinimumSize(QtCore.QSize(0, 40))
        self.labelLab.setFont(font)
        self.labelLab.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelLab.setObjectName("labelLab")
        self.labelPass = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelPass.setMinimumSize(QtCore.QSize(0, 40))
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelPass.setObjectName("labelPass")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.labelPass)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.enterPass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterPass.setMinimumSize(QtCore.QSize(0, 40))
        self.enterPass.setStyleSheet("#enterPass{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterPass:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterPass:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterPass.setClearButtonEnabled(True)
        self.enterPass.setObjectName("enterPass")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.enterPass)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelLab)
        self.MAINLABEL = QtWidgets.QLabel(add_admin)
        self.MAINLABEL.setGeometry(QtCore.QRect(0, 0, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.MAINLABEL.setFont(font)
        self.MAINLABEL.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color:#01579B;")
        self.MAINLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.MAINLABEL.setObjectName("MAINLABEL")
        self.label_2 = QtWidgets.QLabel(add_admin)
        self.label_2.setGeometry(QtCore.QRect(-30, 80, 731, 551))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.confirmButton.raise_()
        self.cancelButton.clicked.connect(add_admin.close)
        self.confirmButton.clicked.connect(lambda: self.addAdmin(add_admin))
        self.enterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(add_admin)
        QtCore.QMetaObject.connectSlotsByName(add_admin)
        
    def addAdmin(self, add_admin):
        import db
        if(self.enterContact.text() == '' or self.enterEid.text()=='' or self.enterName.text()=='' or self.enterEmail.text() == '' or self.enterPass.text()=='' or self.enterLab.text()==''):
            QtWidgets.QMessageBox.about(add_admin, "Invalid Entry!", "Please Fill all the details!")
        elif('@' not in self.enterEmail.text()):
            QtWidgets.QMessageBox.about(add_admin, "Invalid Entry!", "Please Enter a valid E-Mail ID!")
        elif(len(self.enterContact.text())!=10 or not (self.enterContact.text().isdigit())):
            QtWidgets.QMessageBox.about(add_admin, "Invalid Entry!", "Please Enter a valid Phone Number!")
        else:
            db.addAdmin([self.enterName.text(), self.enterEid.text(), self.enterEmail.text(), self.enterContact.text(), self.enterLab.text(), self.enterPass.text()])
            QtWidgets.QMessageBox.about(add_admin, "Successfully Added!", self.enterName.text()+ " has been successfully added as admin!")

    def retranslateUi(self, add_admin):
        _translate = QtCore.QCoreApplication.translate
        add_admin.setWindowTitle(_translate("add_admin", "Add Admin"))
        self.confirmButton.setText(_translate("add_admin", "+   ADD"))
        self.confirmButton.setShortcut(_translate("add_admin", "Return"))
        self.cancelButton.setText(_translate("add_admin", "CANCEL"))
        self.labelName.setText(_translate("add_admin", "Name"))
        self.enterName.setPlaceholderText(_translate("add_admin", "Full Name"))
        self.labelEid.setText(_translate("add_admin", "Employee ID"))
        self.enterEid.setPlaceholderText(_translate("add_admin", "Employee ID"))
        self.labelEmail.setText(_translate("add_admin", "E-Mail ID"))
        self.enterEmail.setPlaceholderText(_translate("add_admin", "E-Mail ID"))
        self.labelContact.setText(_translate("add_admin", "Contact Number"))
        self.enterContact.setPlaceholderText(_translate("add_admin", "Contact Number"))
        self.enterLab.setPlaceholderText(_translate("add_admin", "Laboratory Room No. the Admin belongs to"))
        self.labelLab.setText(_translate("add_admin", "Lab No."))
        self.labelPass.setText(_translate("add_admin", "Login Password"))
        self.enterPass.setPlaceholderText(_translate("add_admin", "Enter New Password"))
        self.MAINLABEL.setText(_translate("add_admin", "Add Admin"))
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_admin = QtWidgets.QWidget()
    ui = Ui_add_admin()
    ui.setupUi(add_admin)
    add_admin.show()
    sys.exit(app.exec_())

