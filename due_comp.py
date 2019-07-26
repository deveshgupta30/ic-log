# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'due_comp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_compDue(object):
    def setupUi(self, compDue):
        compDue.setObjectName("compDue")
        compDue.resize(650, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(compDue.sizePolicy().hasHeightForWidth())
        compDue.setSizePolicy(sizePolicy)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        compDue.setWindowIcon(icon)
        compDue.setMinimumSize(QtCore.QSize(650, 650))
        compDue.setMaximumSize(QtCore.QSize(650, 650))
        self.closeButton = QtWidgets.QPushButton(compDue)
        self.closeButton.setGeometry(QtCore.QRect(280, 600, 93, 41))
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
        self.label = QtWidgets.QLabel(compDue)
        self.label.setGeometry(QtCore.QRect(170, 20, 331, 40))
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Slate For OnePlus Medium\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(compDue)
        self.label_2.setGeometry(QtCore.QRect(-60, -80, 821, 781))
        self.label_2.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.nameList = QtWidgets.QListWidget(compDue)
        self.nameList.setGeometry(QtCore.QRect(10, 110, 310, 431))
        self.nameList.setStyleSheet("#nameList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 1px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#nameList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.nameList.setObjectName("nameList")
        self.dueList = QtWidgets.QListWidget(compDue)
        self.dueList.setGeometry(QtCore.QRect(330, 110, 310, 431))
        self.dueList.setStyleSheet("#dueList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 1px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#dueList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.dueList.setObjectName("dueList")
        self.label_3 = QtWidgets.QLabel(compDue)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 57 10pt \"Slate For OnePlus Medium\";\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(compDue)
        self.label_4.setGeometry(QtCore.QRect(330, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 57 10pt \"Slate For OnePlus Medium\";\n"
"color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(compDue)
        self.label_5.setGeometry(QtCore.QRect(10, 550, 251, 31))
        self.label_5.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(compDue)
        self.label_6.setGeometry(QtCore.QRect(330, 550, 311, 31))
        self.label_6.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.closeButton.raise_()
        self.label.raise_()
        self.nameList.raise_()
        self.dueList.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.nameList.itemClicked.connect(lambda: self.getBorrowList())
        self.dueList.itemDoubleClicked.connect(lambda: self.returnComponent(compDue))
        self.closeButton.clicked.connect(compDue.close)

        self.retranslateUi(compDue)
        QtCore.QMetaObject.connectSlotsByName(compDue)
    def returnComponent(self,compDue):
        import db
        x=db.fetchCompID(self.dueList.currentItem().text())
        reg_no=db.fetchStudentReg(self.nameList.currentItem().text())
        db.returnComponent(x, reg_no, lab)
        QtWidgets.QMessageBox.about(compDue, 'Succesfully Returned!', "Component Successfully Returned!")
        self.dueList.takeItem(self.dueList.currentRow())
        
    def setLab(self, text):
        global lab
        lab=text
    def setItems(self,a):
        self.nameList.addItems(a)
    def getBorrowList(self):
        import db
        self.dueList.clear()
        a=db.getBorrowedComponents(db.fetchStudentReg(self.nameList.currentItem().text()))
        self.dueList.addItems(a)
    def retranslateUi(self, compDue):
        _translate = QtCore.QCoreApplication.translate
        compDue.setWindowTitle(_translate("compDue", "Components Dues"))
        self.closeButton.setText(_translate("compDue", "×  Close"))
        self.closeButton.setShortcut(_translate("compDue", "Esc"))
        self.label.setText(_translate("compDue", "COMPONENT DUES"))
        self.label_3.setText(_translate("compDue", "Student Name"))
        self.label_4.setText(_translate("compDue", "Request List"))
        self.label_5.setText(_translate("compDue", "Click the student\'s name to check components borrowed."))
        self.label_6.setText(_translate("compDue", "Double Click the component names to define them as returned."))
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    compDue = QtWidgets.QWidget()
    ui = Ui_compDue()
    ui.setupUi(compDue)
    compDue.show()
    sys.exit(app.exec_())

