# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_student(object):
    def setupUi(self, view_student):
        view_student.setObjectName("view_student")
        view_student.resize(650, 550)
        view_student.setMinimumSize(QtCore.QSize(650, 550))
        view_student.setMaximumSize(QtCore.QSize(650, 550))
        self.cancelButton = QtWidgets.QPushButton(view_student)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        view_student.setWindowIcon(icon)
        self.cancelButton.setGeometry(QtCore.QRect(560, 490, 75, 40))
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
        self.formLayoutWidget = QtWidgets.QWidget(view_student)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 291, 621, 161))
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
        self.showName = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showName.setFont(font)
        self.showName.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showName.setObjectName("showName")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.showName)
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
        self.MAINLABEL = QtWidgets.QLabel(view_student)
        self.MAINLABEL.setGeometry(QtCore.QRect(0, 0, 651, 81))
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
        self.MAINLABEL.setText("")
        self.MAINLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.MAINLABEL.setObjectName("MAINLABEL")
        self.searchButton = QtWidgets.QPushButton(view_student)
        self.searchButton.setGeometry(QtCore.QRect(470, 170, 171, 51))
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
        self.enterRno = QtWidgets.QLineEdit(view_student)
        self.enterRno.setGeometry(QtCore.QRect(220, 120, 421, 40))
        self.enterRno.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterRno.setFont(font)
        self.enterRno.setStyleSheet("#enterRno{\n"
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
"#enterRno:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterRno:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterRno.setClearButtonEnabled(False)
        self.enterRno.setObjectName("enterRno")
        self.labelRno = QtWidgets.QLabel(view_student)
        self.labelRno.setGeometry(QtCore.QRect(10, 120, 201, 40))
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
        self.searchRgno = QtWidgets.QPushButton(view_student)
        self.searchRgno.setGeometry(QtCore.QRect(540, 120, 101, 40))
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
        self.addStudent = QtWidgets.QPushButton(view_student)
        self.addStudent.setGeometry(QtCore.QRect(340, 170, 131, 51))
        self.addStudent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addStudent.setStyleSheet("#addStudent{\n"
"font: 57 8pt \"Slate For OnePlus Medium\";\n"
"color:rgb(65, 131, 197);\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"    text-decoration: underline;\n"
"selection-color: transparent;\n"
"selection-background-color:transparent;\n"
"gridline-color: transparent;\n"
"}\n"
"#addStudent:hover{\n"
"color:rgb(0, 0, 127);\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    text-decoration: underline;\n"
"}\n"
"#addStudent:pressed{\n"
"color:purple;\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    text-decoration: underline;\n"
"}")
        self.addStudent.setObjectName("addStudent")
        self.label = QtWidgets.QLabel(view_student)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 71))
        self.label.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(view_student)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 651, 551))
        self.label_2.setStyleSheet("background-color:#ffffff;\n"
"border-radius: 15px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(view_student)
        self.line.setGeometry(QtCore.QRect(20, 250, 611, 4))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.deleteStudent = QtWidgets.QPushButton(view_student)
        self.deleteStudent.setGeometry(QtCore.QRect(110, 470, 60, 60))
        self.deleteStudent.setStyleSheet("#deleteStudent {\n"
"background-color: transparent;\n"
"\n"
"border-style: inset;\n"
"border-radius:30px;\n"
"border-image:url(:/others/lel_delete.png);\n"
"}\n"
"#deleteStudent:hover {\n"
"    background-color: #DC3333;\n"
"    \n"
"    border-radius:30px;\n"
"    border-style:outset;\n"
"    border-image: url(:/others/lel_delete2.png);\n"
"}\n"
"\n"
"#deleteStudent:pressed {\n"
"    background-color: #b80000;\n"
"    border-color:#b80000;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.deleteStudent.setText("")
        self.deleteStudent.setIconSize(QtCore.QSize(50, 50))
        self.deleteStudent.setObjectName("deleteStudent")
        self.modifyStudent = QtWidgets.QPushButton(view_student)
        self.modifyStudent.setGeometry(QtCore.QRect(250, 470, 60, 60))
        self.modifyStudent.setStyleSheet("#modifyStudent {\n"
"background-color:transparent;\n"
"    border-image: url(:/others/lel_user.png);\n"
"border-color:transparent;\n"
"border-style:outset;\n"
"border-radius:30px;\n"
"}\n"
"#modifyStudent:hover {\n"
"    background-color:white;\n"
"    border-color:transparent;\n"
"    border-radius:30px;\n"
"    border-image: url(:/others/lel_user_2.png);\n"
"}\n"
"\n"
"#modifyStudent:pressed {\n"
"    background-color:#01579B;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.modifyStudent.setText("")
        self.modifyStudent.setIconSize(QtCore.QSize(50, 50))
        self.modifyStudent.setObjectName("modifyStudent")
        self.issueComponent = QtWidgets.QPushButton(view_student)
        self.issueComponent.setGeometry(QtCore.QRect(410, 470, 60, 60))
        self.issueComponent.setStyleSheet("#issueComponent {\n"
"background-color:transparent;\n"
"    border-image: url(:/admin/cart.png);\n"
"border-color:transparent;\n"
"border-style:outset;\n"
"border-radius:30px;\n"
"}\n"
"#issueComponent:hover {\n"
"    background-color:#087F22;\n"
"    border-color:transparent;\n"
"    border-radius:30px;\n"
"    border-style:outset;\n"
"    border-image: url(:/admin/cart2.png);\n"
"}\n"
"\n"
"#issueComponent:pressed {\n"
"    border-style:inset;\n"
"    border-width:10px;\n"
"    border-color:#01579B;\n"
"    border-radius:30px;\n"
"    border-style:inset;\n"
"}")
        self.issueComponent.setText("")
        self.issueComponent.setIconSize(QtCore.QSize(50, 50))
        self.issueComponent.setObjectName("issueComponent")
        self.MAINLABEL.raise_()
        self.label_2.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.searchButton.raise_()
        self.enterRno.raise_()
        self.labelRno.raise_()
        self.searchRgno.raise_()
        self.addStudent.raise_()
        self.label.raise_()
        self.line.raise_()
        self.deleteStudent.raise_()
        self.modifyStudent.raise_()
        self.issueComponent.raise_()
        self.addStudent.clicked.connect(self.openAddStudent)
        self.searchButton.clicked.connect(lambda: self.searchStudent(view_student))
        self.deleteStudent.clicked.connect(lambda: self.delete_Student(view_student))
        self.searchRgno.clicked.connect(lambda: self.openSearch(view_student))
        self.modifyStudent.clicked.connect(lambda:self.openModifyStudent(view_student))
        self.issueComponent.clicked.connect(lambda:self.openIssueComponent(view_student))
        self.cancelButton.clicked.connect(view_student.close)

        self.retranslateUi(view_student)
        QtCore.QMetaObject.connectSlotsByName(view_student)

    def openIssueComponent(self, view_student):
        
        from issue_component import Ui_issueComp
        import db
        self.window=QtWidgets.QWidget()
        self.ui=Ui_issueComp()
        self.ui.setupUi(self.window)
        self.ui.setRegNo(self.enterRno.text())
        self.ui.setTitle(str('Issue Components - '+db.fetchStudentName(self.enterRno.text())) ,self.window)
        self.window.show()
        
    def changeText(self, a):
        self.enterRno.setText(a)      
        
    def openModifyStudent(self, view_studnet):
        from modify_student import Ui_modify_student
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_modify_student()
        
        self.ui6.setupUi(self.window6)
        self.ui6.setDetails([self.enterRno.text(), self.showName.text(), self.showEmail.text(), self.showContact.text()])
        self.window6.show()
        
    def delete_Student(self, delete_comp):
        from warning_dialogue_student import Ui_Dialog
        self.window6=QtWidgets.QDialog()
        self.ui6=Ui_Dialog()
        self.ui6.setupUi(self.window6)
        self.ui6.setRno(self.enterRno.text())
        self.window6.show()
        
    def openSearch(self,delete_comp):
        from get_student1 import Ui_getStudent
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getStudent()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        delete_comp.close()
        
    def openAddStudent(self):
        from add_student import Ui_add_student
        self.window4=QtWidgets.QWidget()
        self.ui4=Ui_add_student()
        self.ui4.setupUi(self.window4)
        self.window4.show()     
                                
    def searchStudent(self,delete_comp):
        import db
        a=db.fetchStudentDetails(self.enterRno.text())
        if(a==None):
            QtWidgets.QMessageBox.about(delete_comp, "Error!", "Student not found!")
        else:
            self.enterRno.setEnabled(False)
            self.showName.setText(a[1])
            self.showContact.setText(a[2])
            self.showEmail.setText(a[3])
            self.searchRgno.setEnabled(False)
            self.deleteStudent.setEnabled(True)
            self.issueComponent.setEnabled(True)
            self.modifyStudent.setEnabled(True)
            

    def retranslateUi(self, view_student):
        _translate = QtCore.QCoreApplication.translate
        view_student.setWindowTitle(_translate("view_student", "Student Details"))
        self.cancelButton.setText(_translate("view_student", "CANCEL"))
        self.cancelButton.setShortcut(_translate("view_student", "Esc"))
        self.labelName.setText(_translate("view_student", "Student Name:"))
        self.showName.setText(_translate("view_student", "Please enter Student Registration No."))
        self.labelEmail.setText(_translate("view_student", "E-Mail ID:"))
        self.showEmail.setText(_translate("view_student", "Please enter Student Registration No."))
        self.labelContact.setText(_translate("view_student", "Contact Number:"))
        self.showContact.setText(_translate("view_student", "Please enter Student Registration No."))
        self.searchButton.setText(_translate("view_student", "Search"))
        self.enterRno.setPlaceholderText(_translate("view_student", "Registration No."))
        self.labelRno.setText(_translate("view_student", "Registration Number:"))
        self.searchRgno.setText(_translate("view_student", "GET USN"))
        self.addStudent.setText(_translate("view_student", "Add New Student?"))
        self.label.setText(_translate("view_student", "Student Details"))
        self.deleteStudent.setWhatsThis(_translate("view_student", "<html><head/><body><p>Delete Component</p></body></html>"))
        self.modifyStudent.setToolTip(_translate("view_student", "<html><head/><body><p>Modify Admin</p></body></html>"))
        self.issueComponent.setToolTip(_translate("view_student", "<html><head/><body><p>Issue Component</p></body></html>"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_student = QtWidgets.QWidget()
    ui = Ui_view_student()
    ui.setupUi(view_student)
    view_student.show()
    sys.exit(app.exec_())

