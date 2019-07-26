# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_add_student(object):
    def setupUi(self, add_student):
        add_student.setObjectName("add_student")
        add_student.resize(650, 550)
        add_student.setMinimumSize(QtCore.QSize(650, 550))
        add_student.setMaximumSize(QtCore.QSize(650, 550))
        self.confirmButton = QtWidgets.QPushButton(add_student)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_student.setWindowIcon(icon)
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
        self.cancelButton = QtWidgets.QPushButton(add_student)
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
        self.formLayoutWidget = QtWidgets.QWidget(add_student)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 631, 331))
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
        self.enterName.setObjectName("enterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enterName)
        self.enterReg = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterReg.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterReg.setFont(font)
        self.enterReg.setStyleSheet("#enterReg{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enterReg:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterReg:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterReg.setObjectName("enterReg")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enterReg)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
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
        self.enterEmail.setObjectName("enterEmail")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.enterEmail)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem2)
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
        self.enterContact.setObjectName("enterContact")
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
        
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.enterContact)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.labelPass = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelPass.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelPass.setObjectName("labelPass")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelPass)
        self.enterPass = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterPass.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterPass.setFont(font)
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
        self.enterPass.setObjectName("enterPass")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.enterPass)
        self.labelReg = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelReg.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelReg.setFont(font)
        self.labelReg.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelReg.setObjectName("labelReg")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelReg)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.MAINLABEL = QtWidgets.QLabel(add_student)
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
        self.label_2 = QtWidgets.QLabel(add_student)
        self.label_2.setGeometry(QtCore.QRect(-30, 82, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.confirmButton.clicked.connect(lambda: self.addStudent(add_student))
        self.cancelButton.clicked.connect(add_student.close)
        self.enterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(add_student)
        QtCore.QMetaObject.connectSlotsByName(add_student)
        self.enterName.setClearButtonEnabled(True)
        self.enterContact.setClearButtonEnabled(True)
        self.enterReg.setClearButtonEnabled(True)
        self.enterPass.setClearButtonEnabled(True)
        self.enterEmail.setClearButtonEnabled(True)
        
    def addStudent(self, add_student):
        import db
        if(self.enterContact.text() == '' or self.enterReg.text()=='' or self.enterName.text()=='' or self.enterEmail.text() == '' or self.enterPass.text()==''):
            QtWidgets.QMessageBox.about(add_student, "Invalid Entry!", "Please Fill all the details!")
        elif('@' not in self.enterEmail.text()):
            QtWidgets.QMessageBox.about(add_student, "Invalid Entry!", "Please Enter a valid E-Mail ID!")
        elif(len(self.enterContact.text())!=10 or not (self.enterContact.text().isdigit())):
            QtWidgets.QMessageBox.about(add_student, "Invalid Entry!", "Please Enter a valid Phone Number!")
        else:
            try:
                db.addStudent([self.enterName.text(), self.enterReg.text(), self.enterContact.text(), self.enterEmail.text(), self.enterPass.text()])
            except:
                QtWidgets.QMessageBox.about(add_student, "Invalid Entry!", "Student Already Exists!")
            else:
                QtWidgets.QMessageBox.about(add_student, "Successfully Added!", self.enterName.text()+ " has been successfully added as student!")

    def retranslateUi(self, add_student):
        _translate = QtCore.QCoreApplication.translate
        add_student.setWindowTitle(_translate("add_student", "Add Student"))
        self.confirmButton.setText(_translate("add_student", "+   ADD"))
        self.confirmButton.setShortcut(_translate("add_student", "Return"))
        self.cancelButton.setText(_translate("add_student", "CANCEL"))
        self.cancelButton.setShortcut(_translate("add_student", "Esc"))
        self.labelName.setText(_translate("add_student", "Name"))
        self.enterName.setPlaceholderText(_translate("add_student", "Full Name"))
        self.labelEmail.setText(_translate("add_student", "E-Mail ID"))
        self.enterEmail.setPlaceholderText(_translate("add_student", "E-Mail ID"))
        self.labelContact.setText(_translate("add_student", "Contact Number"))
        self.enterContact.setPlaceholderText(_translate("add_student", "Contact Number"))
        self.labelPass.setText(_translate("add_student", "Login Password"))
        self.enterPass.setPlaceholderText(_translate("add_student", "New Login Password"))
        self.labelReg.setText(_translate("add_student", "Registration Number"))
        self.enterReg.setPlaceholderText(_translate("add_student", "Registration Number"))
        self.MAINLABEL.setText(_translate("add_student", "Add Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_student = QtWidgets.QWidget()
    ui = Ui_add_student()
    ui.setupUi(add_student)
    add_student.show()
    sys.exit(app.exec_())

