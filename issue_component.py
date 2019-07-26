# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'issue_component.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_issueComp(object):
    def setupUi(self, issueComp):
        issueComp.setObjectName("issueComp")
        issueComp.resize(650, 680)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        issueComp.setWindowIcon(icon)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(issueComp.sizePolicy().hasHeightForWidth())
        issueComp.setSizePolicy(sizePolicy)
        issueComp.setMinimumSize(QtCore.QSize(650, 680))
        issueComp.setMaximumSize(QtCore.QSize(650, 680))
        self.closeButton = QtWidgets.QPushButton(issueComp)
        self.closeButton.setGeometry(QtCore.QRect(340, 630, 101, 41))
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
        self.label = QtWidgets.QLabel(issueComp)
        self.label.setGeometry(QtCore.QRect(150, 20, 371, 40))
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
        self.searchComp = QtWidgets.QLineEdit(issueComp)
        self.searchComp.setGeometry(QtCore.QRect(140, 90, 401, 40))
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
        self.label_2 = QtWidgets.QLabel(issueComp)
        self.label_2.setGeometry(QtCore.QRect(-60, -80, 821, 781))
        self.label_2.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.sugList = QtWidgets.QListWidget(issueComp)
        self.sugList.setGeometry(QtCore.QRect(10, 220, 310, 341))
        self.sugList.setStyleSheet("#sugList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 1px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#sugList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.sugList.setObjectName("sugList")
        self.submitButton = QtWidgets.QPushButton(issueComp)
        self.submitButton.setGeometry(QtCore.QRect(210, 630, 101, 41))
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
        self.reqList = QtWidgets.QListWidget(issueComp)
        self.reqList.setGeometry(QtCore.QRect(330, 220, 310, 341))
        self.reqList.setStyleSheet("#reqList{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 2px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#reqList:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.reqList.setObjectName("reqList")
        self.label_3 = QtWidgets.QLabel(issueComp)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 241, 16))
        self.label_3.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(issueComp)
        self.label_4.setGeometry(QtCore.QRect(330, 200, 101, 16))
        self.label_4.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_4.setObjectName("label_4")
        self.registerLab = QtWidgets.QLineEdit(issueComp)
        self.registerLab.setGeometry(QtCore.QRect(140, 140, 401, 40))
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
        self.label_6 = QtWidgets.QLabel(issueComp)
        self.label_6.setGeometry(QtCore.QRect(330, 570, 311, 41))
        self.label_6.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(issueComp)
        self.label_5.setGeometry(QtCore.QRect(10, 570, 251, 41))
        self.label_5.setStyleSheet("\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"\n"
"    color: white;\n"
"")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_2.raise_()
        self.closeButton.raise_()
        self.label.raise_()
        self.searchComp.raise_()
        self.sugList.raise_()
        self.submitButton.raise_()
        self.reqList.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.registerLab.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.searchComp.textChanged.connect(self.searchDB)
        self.sugList.clicked.connect(self.addItem)
        self.reqList.doubleClicked.connect(self.clearItem)
        self.submitButton.clicked.connect(lambda: self.reqComp(issueComp))
        self.closeButton.clicked.connect(issueComp.close)
        self.retranslateUi(issueComp)
        QtCore.QMetaObject.connectSlotsByName(issueComp)
    def reqComp(self,requestComp):
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
                elif(db.getComponentStock(item.text(), self.registerLab.text())<=0):
                    QtWidgets.QMessageBox.about(requestComp, 'Error!', "Component ID "  + item.text() +  " out of stock!")  
                else:
                    db.issueComponent(item.text(),reg_no, self.registerLab.text())
                    QtWidgets.QMessageBox.about(requestComp, 'Components Issued!', "Component ID "  + item.text() +  " succesfully issued!")
            
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
        
    def setTitle(self,s,requestComp):
        requestComp.setWindowTitle(s)
        
    def setRegNo(self,r):
        global reg_no
        reg_no=r
        
    def retranslateUi(self, issueComp):
        _translate = QtCore.QCoreApplication.translate
        issueComp.setWindowTitle(_translate("issueComp", "Issue Components"))
        self.closeButton.setText(_translate("issueComp", "×  CLOSE"))
        self.closeButton.setShortcut(_translate("issueComp", "Esc"))
        self.label.setText(_translate("issueComp", "Issue Components"))
        self.searchComp.setPlaceholderText(_translate("issueComp", "Name of Component"))
        self.submitButton.setText(_translate("issueComp", "✔  SUBMIT"))
        self.label_3.setText(_translate("issueComp", "Component Name Suggestions"))
        self.label_4.setText(_translate("issueComp", "Request List"))
        self.registerLab.setPlaceholderText(_translate("issueComp", "Lab No."))
        self.label_6.setText(_translate("issueComp", "Double click the Component ID to remove the component from the issue list."))
        self.label_5.setText(_translate("issueComp", "Click the Component name to add it to the issue list."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issueComp = QtWidgets.QWidget()
    ui = Ui_issueComp()
    ui.setupUi(issueComp)
    issueComp.show()
    sys.exit(app.exec_())

