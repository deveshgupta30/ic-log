# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_modify_admin(object):
    def setupUi(self, modify_admin):
        modify_admin.setObjectName("modify_admin")
        modify_admin.resize(650, 550)
        modify_admin.setMinimumSize(QtCore.QSize(650, 550))
        modify_admin.setMaximumSize(QtCore.QSize(650, 550))
        self.confirmButton = QtWidgets.QPushButton(modify_admin)
        self.confirmButton.setEnabled(False)
        self.confirmButton.setGeometry(QtCore.QRect(450, 490, 101, 41))
        font = QtGui.QFont()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        modify_admin.setWindowIcon(icon)
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
        self.cancelButton = QtWidgets.QPushButton(modify_admin)
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
        self.formLayoutWidget = QtWidgets.QWidget(modify_admin)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 218, 631, 251))
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
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelName)
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
"}")
        self.enterName.setClearButtonEnabled(True)
        self.enterName.setObjectName("enterName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enterName)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
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
"}")
        self.enterEmail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterEmail.setClearButtonEnabled(True)
        self.enterEmail.setObjectName("enterEmail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.enterEmail)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem1)
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
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelContact)
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
"}")
        self.enterContact.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterContact.setClearButtonEnabled(True)
        self.enterContact.setObjectName("enterContact")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.enterContact)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem2)
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
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelLab)
        self.enterLab = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterLab.setEnabled(False)
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
"}\n"
"#enterLab:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}")
        self.enterLab.setClearButtonEnabled(True)
        self.enterLab.setObjectName("enterLab")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.enterLab)
        self.MAINLABEL = QtWidgets.QLabel(modify_admin)
        self.MAINLABEL.setGeometry(QtCore.QRect(0, -2, 651, 91))
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
        self.label_2 = QtWidgets.QLabel(modify_admin)
        self.label_2.setGeometry(QtCore.QRect(-30, 82, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(modify_admin)
        self.line.setGeometry(QtCore.QRect(-100, 200, 931, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.searchButton = QtWidgets.QPushButton(modify_admin)
        self.searchButton.setGeometry(QtCore.QRect(470, 150, 171, 51))
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
        self.labelEid = QtWidgets.QLabel(modify_admin)
        self.labelEid.setGeometry(QtCore.QRect(10, 110, 121, 40))
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
        self.enterEid = QtWidgets.QLineEdit(modify_admin)
        self.enterEid.setGeometry(QtCore.QRect(150, 110, 491, 40))
        self.enterEid.setMinimumSize(QtCore.QSize(300, 40))
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
"\n"
"}\n"
"#enterEid:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterEid:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")

        self.enterEid.setObjectName("enterEid")
        self.searchEid = QtWidgets.QPushButton(modify_admin)
        self.searchEid.setGeometry(QtCore.QRect(550, 110, 93, 40))
        self.searchEid.setMinimumSize(QtCore.QSize(0, 40))
        self.searchEid.setStyleSheet("#searchEid{background-color: transparent;\n"
"border-color: transparent;\n"
"font: 57 10pt \"Slate For OnePlus Medium\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"color:#8aacc8;\n"
"}\n"
"#searchEid:hover{\n"
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
"#searchEid:pressed {\n"
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
        self.searchEid.setObjectName("searchEid")
        self.label_2.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.line.raise_()
        self.searchButton.raise_()
        self.labelEid.raise_()
        self.enterEid.raise_()
        self.searchEid.raise_()
        self.searchButton.clicked.connect(lambda: self.searchAdmin(modify_admin))
        self.confirmButton.clicked.connect(lambda: self.modifyAdmin(modify_admin))
        self.searchEid.clicked.connect(lambda: self.openSearch(modify_admin))
        self.cancelButton.clicked.connect(modify_admin.close)

        self.retranslateUi(modify_admin)
        QtCore.QMetaObject.connectSlotsByName(modify_admin)

    def openSearch(self,modify_admin):
        from get_admin import Ui_getAdmin
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getAdmin()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        modify_admin.close()
        
    def changeText(self, a):
        self.enterEid.setText(a)

    def modifyAdmin(self, modify_admin):
        import db
        if(self.enterContact.text() == '' or self.enterName.text()=='' or self.enterEmail.text() == '' or self.enterLab.text()==''):
            QtWidgets.QMessageBox.about(modify_admin, "Invalid Entry!", "Please Fill all the details!")
        elif('@' not in self.enterEmail.text()):
            QtWidgets.QMessageBox.about(modify_admin, "Invalid Entry!", "Please Enter a valid E-Mail ID!")
        elif(len(self.enterContact.text())!=10 or not (self.enterContact.text().isdigit())):
            QtWidgets.QMessageBox.about(modify_admin, "Invalid Entry!", "Please Enter a valid Phone Number!")
        else:
            db.modifyAdmin([self.enterName.text(), self.enterEmail.text(),self.enterContact.text(),self.enterLab.text(), self.enterEid.text()])
            QtWidgets.QMessageBox.about(modify_admin, "Successfull!", "Employee Details Succesfully Modified!")
            
    def setDetails(self, a):
            self.enterEid.setText(str(a[0]))
            self.enterEid.setEnabled(False)
            self.enterName.setEnabled(True)
            self.enterName.setText(str(a[1]))
            self.enterEmail.setEnabled(True)
            self.enterEmail.setText(str(a[2]))
            self.enterContact.setEnabled(True)
            self.enterContact.setText(str(a[3]))
            self.enterLab.setEnabled(True)
            self.enterLab.setText(str(a[4]))
            self.confirmButton.setEnabled(True)
            self.searchEid.setEnabled(False)


    def retranslateUi(self, modify_admin):
        _translate = QtCore.QCoreApplication.translate
        modify_admin.setWindowTitle(_translate("modify_admin", "Modify Admin"))
        self.confirmButton.setText(_translate("modify_admin", "MODIFY"))
        self.cancelButton.setText(_translate("modify_admin", "CANCEL"))
        self.cancelButton.setShortcut(_translate("modify_admin", "Esc"))
        self.labelName.setText(_translate("modify_admin", "Name"))
        self.enterName.setPlaceholderText(_translate("modify_admin", "Full Name"))
        self.labelEmail.setText(_translate("modify_admin", "E-Mail ID"))
        self.enterEmail.setPlaceholderText(_translate("modify_admin", "E-Mail ID"))
        self.labelContact.setText(_translate("modify_admin", "Contact Number"))
        self.enterContact.setPlaceholderText(_translate("modify_admin", "Contact Number"))
        self.labelLab.setText(_translate("modify_admin", "Lab No."))
        self.enterLab.setPlaceholderText(_translate("modify_admin", "Laboratory Room No. the Admin belongs to"))
        self.MAINLABEL.setText(_translate("modify_admin", "Modify Admin"))
        self.searchButton.setText(_translate("modify_admin", "Search"))
        self.searchButton.setShortcut(_translate("modify_admin", "Return"))
        self.labelEid.setText(_translate("modify_admin", "Employee ID"))
        self.enterEid.setPlaceholderText(_translate("modify_admin", "Employee ID"))
        self.searchEid.setText(_translate("modify_admin", "Get ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modify_admin = QtWidgets.QWidget()
    ui = Ui_modify_admin()
    ui.setupUi(modify_admin)
    modify_admin.show()
    sys.exit(app.exec_())

