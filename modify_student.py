# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_modify_student(object):
    def setupUi(self, modify_student):
        modify_student.setObjectName("modify_student")
        modify_student.resize(650, 550)
        modify_student.setMinimumSize(QtCore.QSize(650, 550))
        modify_student.setMaximumSize(QtCore.QSize(650, 550))
        self.confirmButton = QtWidgets.QPushButton(modify_student)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        modify_student.setWindowIcon(icon)
        self.confirmButton.setEnabled(False)
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
"}\n"
"#confirmButton:disabled{\n"
"background-color:#bbdefb;\n"
"color: #eeffff;\n"
"}\n"
"")
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(modify_student)
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
        self.formLayoutWidget = QtWidgets.QWidget(modify_student)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 230, 631, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.enterName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterName.setEnabled(False)
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
"}\n"
"#enterName:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.enterName.setClearButtonEnabled(True)
        self.enterName.setObjectName("enterName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enterName)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem)
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
        self.enterEmail.setEnabled(False)
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
"}\n"
"#enterEmail:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.enterEmail.setClearButtonEnabled(True)
        self.enterEmail.setObjectName("enterEmail")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.enterEmail)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem1)
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
        self.enterContact.setEnabled(False)
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
"}\n"
"#enterContact:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.enterContact.setClearButtonEnabled(True)
        self.enterContact.setObjectName("enterContact")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.enterContact)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.MAINLABEL = QtWidgets.QLabel(modify_student)
        self.MAINLABEL.setGeometry(QtCore.QRect(0, -2, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MAINLABEL.setFont(font)
        self.MAINLABEL.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color:#01579B;font: 30pt \"Calibri\";\n"
"color: #ffffff")
        self.MAINLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.MAINLABEL.setObjectName("MAINLABEL")
        self.label_2 = QtWidgets.QLabel(modify_student)
        self.label_2.setGeometry(QtCore.QRect(-30, 82, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(modify_student)
        self.line.setGeometry(QtCore.QRect(-20, 210, 681, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.searchRgno = QtWidgets.QPushButton(modify_student)
        self.searchRgno.setGeometry(QtCore.QRect(540, 110, 101, 40))
        self.searchRgno.setMinimumSize(QtCore.QSize(0, 40))
        self.searchRgno.setStyleSheet("#searchRgno{background-color: transparent;\n"
"border-color: transparent;\n"
"font: 57 10pt \"Slate For OnePlus Medium\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"color:#8aacc8;\n"
"}\n"
"#searchRgno:hover{\n"
"background-color: #003c8f;\n"
"border-color: #003c8f;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus Medium\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"color:white\n"
"}\n"
"#searchRgno:pressed {\n"
"   background-color: #000051;\n"
"border-color: #000051;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus Medium\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"color:white\n"
"}")
        self.searchRgno.setObjectName("searchRgno")
        self.searchButton = QtWidgets.QPushButton(modify_student)
        self.searchButton.setGeometry(QtCore.QRect(470, 160, 171, 51))
        self.searchButton.setMinimumSize(QtCore.QSize(0, 40))
        self.searchButton.setStyleSheet("#searchButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 20px;\n"
"}\n"
"#searchButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#searchButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.searchButton.setObjectName("searchButton")
        self.enterReg = QtWidgets.QLineEdit(modify_student)
        self.enterReg.setGeometry(QtCore.QRect(220, 110, 421, 40))
        self.enterReg.setMinimumSize(QtCore.QSize(300, 40))
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
"\n"
"}\n"
"#enterReg:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterReg:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")

        self.enterReg.setObjectName("enterReg")
        self.labelReg = QtWidgets.QLabel(modify_student)
        self.labelReg.setGeometry(QtCore.QRect(10, 110, 191, 40))
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
        self.label_2.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.line.raise_()
        self.searchButton.raise_()
        self.enterReg.raise_()
        self.labelReg.raise_()
        self.searchRgno.raise_()
        self.searchButton.clicked.connect(lambda: self.searchStudent(modify_student))
        self.confirmButton.clicked.connect(lambda: self.modifyStudent(modify_student))
        self.searchRgno.clicked.connect(lambda: self.openSearch(modify_student))
        self.cancelButton.clicked.connect(modify_student.close)

        self.retranslateUi(modify_student)
        QtCore.QMetaObject.connectSlotsByName(modify_student)
        
    def openSearch(self, modify_student):
        from get_student import Ui_getStudent
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getStudent()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        modify_student.close()
        
    def setDetails(self,a):
        self.enterReg.setText(a[0])
        self.enterReg.setEnabled(False)
        self.enterName.setEnabled(True)
        self.enterName.setText(a[1])
        self.enterEmail.setEnabled(True)
        self.enterEmail.setText(a[2])
        self.enterContact.setEnabled(True)
        self.enterContact.setText(a[3])
        self.confirmButton.setEnabled(True)
        self.searchRgno.setEnabled(False)       
        
    def changeText(self, a):
        self.enterReg.setText(a)

    def modifyStudent(self, modify_student):
        import db
        if(self.enterContact.text() == '' or self.enterReg.text()=='' or self.enterName.text()=='' or self.enterEmail.text() == ''):
            QtWidgets.QMessageBox.about(modify_student, "Invalid Entry!", "Please Fill all the details!")
        elif('@' not in self.enterEmail.text()):
            QtWidgets.QMessageBox.about(modify_student, "Invalid Entry!", "Please Enter a valid E-Mail ID!")
        elif(len(self.enterContact.text())!=10 or not (self.enterContact.text().isdigit())):
            QtWidgets.QMessageBox.about(modify_student, "Invalid Entry!", "Please Enter a valid Phone Number!")
        else:
            db.modifyStudent([self.enterName.text(), self.enterContact.text(), self.enterEmail.text(), self.enterReg.text()])
            QtWidgets.QMessageBox.about(modify_student, "Successfully Added!", "Student Details Succesfully Modified!")
        

    def retranslateUi(self, modify_student):
        _translate = QtCore.QCoreApplication.translate
        modify_student.setWindowTitle(_translate("modify_student", "Modify Student"))
        self.confirmButton.setText(_translate("modify_student", "MODIFY"))
        self.cancelButton.setText(_translate("modify_student", "CANCEL"))
        self.cancelButton.setShortcut(_translate("modify_student", "Esc"))
        self.labelName.setText(_translate("modify_student", "Name"))
        self.enterName.setPlaceholderText(_translate("modify_student", "Full Name"))
        self.labelEmail.setText(_translate("modify_student", "E-Mail ID"))
        self.enterEmail.setPlaceholderText(_translate("modify_student", "E-Mail ID"))
        self.labelContact.setText(_translate("modify_student", "Contact Number"))
        self.enterContact.setPlaceholderText(_translate("modify_student", "Contact Number"))
        self.MAINLABEL.setText(_translate("modify_student", "Modify Student"))
        self.searchRgno.setText(_translate("modify_student", "GET USN"))
        self.searchButton.setText(_translate("modify_student", "Search"))
        self.searchButton.setShortcut(_translate("modify_student", "Return"))
        self.enterReg.setPlaceholderText(_translate("modify_student", "Registration Number"))
        self.labelReg.setText(_translate("modify_student", "Registration Number"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modify_student = QtWidgets.QWidget()
    ui = Ui_modify_student()
    ui.setupUi(modify_student)
    modify_student.show()
    sys.exit(app.exec_())

