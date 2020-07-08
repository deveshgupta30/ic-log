# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_portal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_student_portal(object):
    def setupUi(self, student_portal):
        student_portal.setObjectName("student_portal")
        student_portal.resize(1000, 700)
        student_portal.setMinimumSize(QtCore.QSize(1000, 700))
        student_portal.setMaximumSize(QtCore.QSize(1000, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/student/Student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_portal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(student_portal)
        self.centralwidget.setObjectName("centralwidget")
        self.studentProfile = QtWidgets.QPushButton(self.centralwidget)
        self.studentProfile.setGeometry(QtCore.QRect(60, 0, 331, 51))
        self.studentProfile.setStyleSheet("#studentProfile{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"#studentProfile:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #73e8ff;\n"
"    font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"\n"
"}\n"
"#studentProfile:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"")
        self.studentProfile.setObjectName("studentProfile")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 190, 211, 31))
        self.label_7.setStyleSheet("font: 57 9pt \"Slate For OnePlus Medium\";\n"
"color: #000063;")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 160, 211, 20))
        self.line.setStyleSheet("color: rgb(190, 190, 190);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 231, 581))
        self.label_2.setStyleSheet("border-color: #002171;\n"
"background-color: white;\n"
"border-style: inset;\n"
"border-radius: 30px;\n"
"border-color:white")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1001, 71))
        self.label_4.setStyleSheet("background-color: #1a237e;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/alert_box/Student3.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.signOut = QtWidgets.QPushButton(self.centralwidget)
        self.signOut.setGeometry(QtCore.QRect(855, 10, 135, 35))
        self.signOut.setStyleSheet("#signOut{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"font: 14pt \"Slate For OnePlus Bk\";\n"
"}\n"
"#signOut:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #73e8ff;\n"
"    font: 14pt \"Slate For OnePlus Bk\";\n"
"    text-decoration: underline;\n"
"}\n"
"#signOut:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 14pt \"Slate For OnePlus Bk\";\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/alert_box/signout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signOut.setIcon(icon)
        self.signOut.setIconSize(QtCore.QSize(25, 25))
        self.signOut.setObjectName("signOut")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 231, 31))
        self.label_3.setStyleSheet("color: #000063;\n"
"font: 57 15pt \"Slate For OnePlus Medium\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 1001, 661))
        self.label.setStyleSheet("background-color: #e3f2fd;\n"
"border-style: inset;\n"
"border-radius: 10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 80, 621, 581))
        self.label_8.setStyleSheet("border-color: #002171;\n"
"border-style: inset;\n"
"border-radius: 30px;\n"
"border-color:white;\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.registerLab = QtWidgets.QLineEdit(self.centralwidget)
        self.registerLab.setGeometry(QtCore.QRect(450, 230, 401, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.registerLab.setFont(font)
        self.registerLab.setStyleSheet("#registerLab{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 10px;\n"
"padding-left: 10px;\n"
"}\n"
"#registerLab:hover {\n"
"    border-style: inset;\n"
"}\n"
"#registerLab:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.registerLab.setObjectName("registerLab")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 290, 241, 16))
        self.label_6.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 100, 371, 40))
        self.label_9.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Slate For OnePlus Medium\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.reqList = QtWidgets.QListView(self.centralwidget)
        self.reqList.setGeometry(QtCore.QRect(650, 310, 271, 201))
        self.reqList.setStyleSheet("#reqList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 2px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#reqList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.reqList.setObjectName("reqList")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 520, 251, 41))
        self.label_10.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 290, 101, 16))
        self.label_11.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_11.setObjectName("label_11")
        self.searchComp = QtWidgets.QLineEdit(self.centralwidget)
        self.searchComp.setGeometry(QtCore.QRect(450, 170, 401, 40))
        self.searchComp.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.searchComp.setFont(font)
        self.searchComp.setStyleSheet("#searchComp{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 10px;\n"
"padding-left: 10px;\n"
"}\n"
"#searchComp:hover {\n"
"    border-style: inset;\n"
"}\n"
"#searchComp:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.searchComp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.searchComp.setClearButtonEnabled(True)
        self.searchComp.setObjectName("searchComp")
        self.sugList = QtWidgets.QListWidget(self.centralwidget)
        self.sugList.setGeometry(QtCore.QRect(339, 310, 271, 201))
        self.sugList.setStyleSheet("#sugList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 2px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#sugList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.sugList.setObjectName("sugList")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 520, 271, 41))
        self.label_12.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(590, 590, 101, 41))
        self.submitButton.setStyleSheet("#submitButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 15px;\n"
"}\n"
"#submitButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#submitButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.submitButton.setObjectName("submitButton")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 400, 211, 31))
        self.label_13.setStyleSheet("font: 57 9pt \"Slate For OnePlus Medium\";\n"
"color: #000063;")
        self.label_13.setObjectName("label_13")
        self.lcdRequested = QtWidgets.QLabel(self.centralwidget)
        self.lcdRequested.setGeometry(QtCore.QRect(60, 240, 171, 151))
        self.lcdRequested.setStyleSheet("color: #64dd17;\n"
"\n"
"font: 25 36pt \"Slate For OnePlus Thin\";")
        self.lcdRequested.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcdRequested.setObjectName("lcdRequested")
        self.lcdBorrowed = QtWidgets.QLabel(self.centralwidget)
        self.lcdBorrowed.setGeometry(QtCore.QRect(60, 460, 171, 151))
        self.lcdBorrowed.setStyleSheet("color: red;\n"
"font: 25 36pt \"Slate For OnePlus Thin\";")
        self.lcdBorrowed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lcdBorrowed.setObjectName("lcdBorrowed")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(460, 0, 81, 51))
        self.aboutButton.setStyleSheet("#aboutButton{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"#aboutButton:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #73e8ff;\n"
"    font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"\n"
"}\n"
"#aboutButton:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"")
        self.aboutButton.setObjectName("aboutButton")
        self.label_4.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.studentProfile.raise_()
        self.aboutButton.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.signOut.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_7.raise_()
        self.registerLab.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.reqList.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.searchComp.raise_()
        self.sugList.raise_()
        self.label_12.raise_()
        self.submitButton.raise_()
        self.label_13.raise_()
        self.lcdRequested.raise_()
        self.lcdBorrowed.raise_()
        student_portal.setCentralWidget(self.centralwidget)
        self.actionRequest_Components = QtWidgets.QAction(student_portal)
        self.actionRequest_Components.setObjectName("actionRequest_Components")
        self.actionView_Profile = QtWidgets.QAction(student_portal)
        self.actionView_Profile.setObjectName("actionView_Profile")
        self.actionChange_Password = QtWidgets.QAction(student_portal)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionComponent_History = QtWidgets.QAction(student_portal)
        self.actionComponent_History.setObjectName("actionComponent_History")
        self.actionAbout = QtWidgets.QAction(student_portal)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSign_Out = QtWidgets.QAction(student_portal)
        self.actionSign_Out.setObjectName("actionSign_Out")
        self.signOut.clicked.connect(lambda: self.openIndex(student_portal))
        self.studentProfile.clicked.connect(lambda: self.openStudentProfile())
        self.searchComp.textChanged.connect(self.searchDB)
        self.sugList.clicked.connect(self.addItem)
        self.reqList.doubleClicked.connect(self.clearItem)
        self.aboutButton.clicked.connect(self.openAbout)
        self.submitButton.clicked.connect(lambda: self.requestComponents(student_portal))
        self.retranslateUi(student_portal)
        QtCore.QMetaObject.connectSlotsByName(student_portal)

    def openAbout(self):
        self.window12=QtWidgets.QWidget()
        self.ui12=about.Ui_About()
        self.ui12.setupUi(self.window12)
        self.window12.show()
        
    def openIndex(self, student_portal):
        
        from student_login import Ui_Form
        self.window4=QtWidgets.QWidget()
        self.ui4=Ui_Form()
        self.ui4.setupUi(self.window4)
        self.window4.show()
        student_portal.close()
        
    def requestComponents(self,requestComp):
        import db
        
        if(self.registerLab.text()==''):
            QtWidgets.QMessageBox.about(requestComp, 'Error!', "Enter the Lab Number!")      
        else:
            i=0
            x=db.getComponentsinLab(self.registerLab.text())
            for i in range(self.reqList.count()):
                item=self.reqList.item(i)    
                if(item.text() not in x):
                    QtWidgets.QMessageBox.about(requestComp, 'Error!', "Component ID "  + item.text() +  " not available in lab!")

                else:
                    db.requestComponent(item.text(),regNo, self.registerLab.text())
                    QtWidgets.QMessageBox.about(requestComp, 'Components Requested!', "Component ID "  + item.text() +  " succesfully requested!")
                    self.lcdRequested.display(int(self.lcdRequested.value())+1)
                    
    def clearItem(self):
        self.reqList.takeItem((self.reqList.currentRow()))
    def addItem(self):
        import db
        self.reqList.addItem(db.fetchCompID(self.sugList.currentItem().text()))
    def searchDB(self):
        self.sugList.clear()
        import db
        a=db.searchCompDB(self.searchComp.text())
        self.sugList.addItems(a)
    def openStudentProfile(self):
        import db
        from student_profile import Ui_student_profile
        self.window1=QtWidgets.QWidget()
        self.ui1=Ui_student_profile()
        self.ui1.setupUi(self.window1)
        self.ui1.setDetails(list(db.fetchStudentDetails(regNo)))
        self.window1.show()   
    
    def setTitle(self,text,student_portal):
        student_portal.setWindowTitle(text)
    def setName(self,text):
        self.studentProfile.setText(text)
    def setRegNo(self,text):
        global regNo
        regNo=text
    def setDashDetails(self, req,bor):
        self.lcdBorrowed.setText(str(bor))
        self.lcdRequested.setText(str(req))

    def retranslateUi(self, student_portal):
        _translate = QtCore.QCoreApplication.translate
        student_portal.setWindowTitle(_translate("student_portal", "Student Portal - ICLog"))
        self.studentProfile.setText(_translate("student_portal", "Student"))
        self.label_7.setText(_translate("student_portal", "Total Requested Components"))
        self.signOut.setText(_translate("student_portal", "Sign Out"))
        self.label_3.setText(_translate("student_portal", "DASHBOARD"))
        self.registerLab.setPlaceholderText(_translate("student_portal", "Lab No."))
        self.label_6.setText(_translate("student_portal", "Component Name Suggestions"))
        self.label_9.setText(_translate("student_portal", "REQUEST COMPONENTS"))
        self.aboutButton.setText(_translate("student_portal", "ICLog"))
        self.label_10.setText(_translate("student_portal", "Click the Component name to add it to the request list."))
        self.label_11.setText(_translate("student_portal", "Request List"))
        self.searchComp.setPlaceholderText(_translate("student_portal", "Name of Component"))
        self.label_12.setText(_translate("student_portal", "Double click the Component ID to remove the component from the request list."))
        self.submitButton.setText(_translate("student_portal", "✔  SUBMIT"))
        self.label_13.setText(_translate("student_portal", "Total Borrowed Components"))
        self.lcdRequested.setText(_translate("student_portal", "0"))
        self.lcdBorrowed.setText(_translate("student_portal", "0"))
        self.actionRequest_Components.setText(_translate("student_portal", "Request Components"))
        self.actionRequest_Components.setShortcut(_translate("student_portal", "Ctrl+N"))
        self.actionView_Profile.setText(_translate("student_portal", "View Profile"))
        self.actionView_Profile.setShortcut(_translate("student_portal", "Ctrl+P"))
        self.actionChange_Password.setText(_translate("student_portal", "Change Password"))
        self.actionComponent_History.setText(_translate("student_portal", "Borrowed Components"))
        self.actionAbout.setText(_translate("student_portal", "About"))
        self.actionAbout.setShortcut(_translate("student_portal", "F1"))
        self.actionSign_Out.setText(_translate("student_portal", "Sign Out"))

import icons_rc, about

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_portal = QtWidgets.QMainWindow()
    ui = Ui_student_portal()
    ui.setupUi(student_portal)
    student_portal.show()
    sys.exit(app.exec_())

