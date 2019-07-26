# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issue_student.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_issueStudent(object):
    def setupUi(self, issueStudent):
        issueStudent.setObjectName("issueStudent")
        issueStudent.resize(650, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(issueStudent.sizePolicy().hasHeightForWidth())
        issueStudent.setSizePolicy(sizePolicy)
        issueStudent.setMinimumSize(QtCore.QSize(650, 650))
        issueStudent.setMaximumSize(QtCore.QSize(650, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        issueStudent.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(issueStudent)
        self.closeButton.setGeometry(QtCore.QRect(280, 590, 93, 41))
        self.closeButton.setStyleSheet("#closeButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 15px;\n"
"}\n"
"#closeButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#closeButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(issueStudent)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 40))
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 57 10pt \"Slate For OnePlus Medium\";\n"
"color: white;")
        self.label.setObjectName("label")
        self.searchName = QtWidgets.QLineEdit(issueStudent)
        self.searchName.setGeometry(QtCore.QRect(160, 30, 481, 40))
        self.searchName.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.searchName.setFont(font)
        self.searchName.setStyleSheet("#searchName{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#searchName:hover {\n"
"    border-style: inset;\n"
"}\n"
"#searchName:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.searchName.setClearButtonEnabled(True)
        self.searchName.setObjectName("searchName")
        self.label_2 = QtWidgets.QLabel(issueStudent)
        self.label_2.setGeometry(QtCore.QRect(-60, -80, 821, 781))
        self.label_2.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.listStud = QtWidgets.QListWidget(issueStudent)
        self.listStud.setGeometry(QtCore.QRect(10, 100, 631, 471))
        self.listStud.setStyleSheet("#listStud{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 1px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#listStud:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.listStud.setObjectName("listStud")
        self.label_3 = QtWidgets.QLabel(issueStudent)
        self.label_3.setGeometry(QtCore.QRect(140, 570, 421, 21))
        self.label_3.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.closeButton.raise_()
        self.label.raise_()
        self.searchName.raise_()
        self.listStud.raise_()
        self.label_3.raise_()
        self.searchName.textChanged.connect(self.searchStudent)
        self.listStud.itemDoubleClicked.connect(lambda: self.issueComponent(issueStudent))
        self.closeButton.clicked.connect(issueStudent.close)
        self.retranslateUi(issueStudent)
        QtCore.QMetaObject.connectSlotsByName(issueStudent)

    def retranslateUi(self, issueStudent):
        _translate = QtCore.QCoreApplication.translate
        issueStudent.setWindowTitle(_translate("issueStudent", "Issue Component"))
        self.closeButton.setText(_translate("issueStudent", "Close"))
        self.closeButton.setShortcut(_translate("issueStudent", "Esc"))
        self.label.setText(_translate("issueStudent", "Name of Student:"))
        self.searchName.setPlaceholderText(_translate("issueStudent", "Name"))
        self.label_3.setText(_translate("issueStudent", "Double Click on the Student\'s name to issue the Component."))
    def searchStudent(self):
        
        import db
        self.listStud.clear()
        self.listStud.addItems(db.searchStudentDB(self.searchName.text()))
        
    def setLab(self, text):
        global lab
        lab=text
        
    def issueComponent(self, issueStudent):
        import db
        x=db.fetchStudentReg(self.listStud.currentItem().text())
        s=db.getComponentStock(Cid,lab)
        y=db.getComponentsinLab(lab)
        print(lab)
        if(int(s)<=0):
            QtWidgets.QMessageBox.about(issueStudent, 'Error!', "Component out of stock!")
        elif(Cid not in y):
            QtWidgets.QMessageBox.about(issueStudent, 'Error!', "Component not in lab!")
        else:
            db.issueComponent(Cid, x, lab)
            QtWidgets.QMessageBox.about(issueStudent, 'Succesfully Issued!', "Component Successfully Issued!")    

    def setCid(self,text):
        global Cid
        Cid=text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issueStudent = QtWidgets.QWidget()
    ui = Ui_issueStudent()
    ui.setupUi(issueStudent)
    issueStudent.show()
    sys.exit(app.exec_())

