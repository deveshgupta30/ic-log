# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_admin(object):
    def setupUi(self, delete_admin):
        delete_admin.setObjectName("delete_admin")
        delete_admin.resize(650, 550)
        delete_admin.setMinimumSize(QtCore.QSize(650, 550))
        delete_admin.setMaximumSize(QtCore.QSize(650, 550))
        self.cancelButton = QtWidgets.QPushButton(delete_admin)
        self.cancelButton.setGeometry(QtCore.QRect(570, 490, 75, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        delete_admin.setWindowIcon(icon)
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
        self.formLayoutWidget = QtWidgets.QWidget(delete_admin)
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
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.MAINLABEL = QtWidgets.QLabel(delete_admin)
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
        self.label_2 = QtWidgets.QLabel(delete_admin)
        self.label_2.setGeometry(QtCore.QRect(-30, 82, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(delete_admin)
        self.line.setGeometry(QtCore.QRect(100, 200, 931, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.searchButton = QtWidgets.QPushButton(delete_admin)
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
        self.labelEid = QtWidgets.QLabel(delete_admin)
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
        self.enterEid = QtWidgets.QLineEdit(delete_admin)
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
        self.enterEid.setText("")
        self.enterEid.setClearButtonEnabled(True)
        self.enterEid.setObjectName("enterEid")
        self.searchEid = QtWidgets.QPushButton(delete_admin)
        self.searchEid.setGeometry(QtCore.QRect(562, 110, 81, 40))
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
        self.addAdmin = QtWidgets.QPushButton(delete_admin)
        self.addAdmin.setGeometry(QtCore.QRect(340, 160, 131, 31))
        self.addAdmin.setStyleSheet("#addAdmin{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: blue;\n"
"font: 8pt \"Slate For OnePlus Bk\";\n"
"}\n"
"#addAdmin:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"font: 8pt \"Slate For OnePlus Bk\";\n"
"text-decoration: underline;\n"
"}\n"
"#addAdmin:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 8pt \"Slate For OnePlus Bk\";\n"
"}")
        self.addAdmin.setObjectName("addAdmin")
        self.deleteAdmin = QtWidgets.QPushButton(delete_admin)
        self.deleteAdmin.setGeometry(QtCore.QRect(150, 485, 50, 50))
        self.deleteAdmin.setStyleSheet("#deleteAdmin {\n"
"background-color:transparent;\n"
"border-color:transparent;\n"
"border-style:outset;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"#deleteAdmin:hover {\n"
"    background-color: red;\n"
"    border-color:transparent;\n"
"    border-radius:25px;\n"
"    border-style:outset;\n"
"}\n"
"\n"
"#deleteAdmin:pressed {\n"
"    background-color: #b80000;\n"
"    border-color:#b80000;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.deleteAdmin.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/Delete-Anti-Revoke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteAdmin.setIcon(icon)
        self.deleteAdmin.setIconSize(QtCore.QSize(50, 50))
        self.deleteAdmin.setObjectName("deleteAdmin")
        self.modifyAdmin = QtWidgets.QPushButton(delete_admin)
        self.modifyAdmin.setGeometry(QtCore.QRect(290, 485, 50, 50))
        self.modifyAdmin.setStyleSheet("#modifyAdmin {\n"
"background-color:transparent;\n"
"\n"
"border-color:transparent;\n"
"border-style:outset;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"#modifyAdmin:hover {\n"
"    background-color:#0277BD;\n"
"    border-color:transparent;\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#modifyAdmin:pressed {\n"
"    background-color:#01579B;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.modifyAdmin.setText("")
        self.deleteAdmin.setEnabled(False)
        self.modifyAdmin.setEnabled(False)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/others/edit_user-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifyAdmin.setIcon(icon1)
        self.modifyAdmin.setIconSize(QtCore.QSize(50, 50))
        self.modifyAdmin.setObjectName("modifyAdmin")
        self.label_2.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.line.raise_()
        self.searchButton.raise_()
        self.labelEid.raise_()
        self.enterEid.raise_()
        self.searchEid.raise_()
        self.addAdmin.raise_()
        self.deleteAdmin.raise_()
        self.modifyAdmin.raise_()
        self.searchButton.clicked.connect(lambda: self.searchAdmin(delete_admin))
        self.searchEid.clicked.connect(lambda: self.openSearch(delete_admin))
        self.deleteAdmin.clicked.connect(lambda: self.delete_Admin(delete_admin))
        self.modifyAdmin.clicked.connect(lambda:self.openModifyAdmin(delete_admin))
        self.addAdmin.clicked.connect(lambda:self.openAddAdmin(delete_admin))
        self.cancelButton.clicked.connect(delete_admin.close)
        self.retranslateUi(delete_admin)
        QtCore.QMetaObject.connectSlotsByName(delete_admin)
        
    def openAddAdmin(self,delete_admin):
        from add_admin import Ui_add_admin
        self.window3=QtWidgets.QWidget()
        self.ui3=Ui_add_admin()
        self.ui3.setupUi(self.window3)
        self.window3.show()     
        
    def openModifyAdmin(self, delete_admin):
        from modify_admin import Ui_modify_admin
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_modify_admin()
        
        self.ui6.setupUi(self.window6)
        self.ui6.setDetails([self.enterEid.text(), self.label_3.text(), self.label_4.text(), self.label_5.text(), self.label_6.text()])
        self.window6.show()
                
    def changeText(self, a):
        self.enterEid.setText(a)      

    def delete_Admin(self, delete_admin):
        from warning_dialogue_admin import Ui_Dialog
        self.window6=QtWidgets.QDialog()
        self.ui6=Ui_Dialog()
        self.ui6.setupUi(self.window6)
        self.ui6.setEid(self.enterEid.text())
        self.window6.show()
        
    def openSearch(self,delete_admin):
        from get_admin1 import Ui_getAdmin
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getAdmin()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        delete_admin.close()
        
    def searchAdmin(self,delete_admin):
        import db
        a=db.fetchAdminDetails(self.enterEid.text())
        if(a==None):
            QtWidgets.QMessageBox.about(delete_admin, "Error!", "Employee ID not found!")
        else:
            self.enterEid.setEnabled(False)
            self.label_3.setText(a[1])
            self.label_4.setText(a[2])
            self.label_5.setText(a[3])
            self.label_6.setText(a[4])
            self.searchEid.setEnabled(False)
            self.deleteAdmin.setEnabled(True)
            self.modifyAdmin.setEnabled(True)            
    def retranslateUi(self, delete_admin):
        _translate = QtCore.QCoreApplication.translate
        delete_admin.setWindowTitle(_translate("delete_admin", "Admin Details"))
        self.cancelButton.setText(_translate("delete_admin", "CANCEL"))
        self.cancelButton.setShortcut(_translate("delete_admin", "Esc"))
        self.labelName.setText(_translate("delete_admin", "Name:"))
        self.labelEmail.setText(_translate("delete_admin", "E-Mail ID:"))
        self.labelContact.setText(_translate("delete_admin", "Contact Number:"))
        self.labelLab.setText(_translate("delete_admin", "Lab No.:"))
        self.label_3.setText(_translate("delete_admin", "Please enter Employee ID "))
        self.label_4.setText(_translate("delete_admin", "Please enter Employee ID "))
        self.label_5.setText(_translate("delete_admin", "Please enter Employee ID "))
        self.label_6.setText(_translate("delete_admin", "Please enter Employee ID "))
        self.MAINLABEL.setText(_translate("delete_admin", "Admin Details"))
        self.searchButton.setText(_translate("delete_admin", "Search"))
        self.searchButton.setShortcut(_translate("delete_admin", "Return"))
        self.labelEid.setText(_translate("delete_admin", "Employee ID"))
        self.enterEid.setPlaceholderText(_translate("delete_admin", "Employee ID"))
        self.searchEid.setText(_translate("delete_admin", "GET ID"))
        self.addAdmin.setText(_translate("delete_admin", "Add New Admin?"))
        self.deleteAdmin.setToolTip(_translate("delete_admin", "<html><head/><body><p>Delete Admin</p></body></html>"))
        self.modifyAdmin.setToolTip(_translate("delete_admin", "<html><head/><body><p>Modify Admin</p></body></html>"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_admin = QtWidgets.QWidget()
    ui = Ui_delete_admin()
    ui.setupUi(delete_admin)
    delete_admin.show()
    sys.exit(app.exec_())

