# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_comp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view_comp(object):
    def setupUi(self, view_comp):
        view_comp.setObjectName("view_comp")
        view_comp.resize(650, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        view_comp.setWindowIcon(icon)
        view_comp.setMinimumSize(QtCore.QSize(650, 550))
        view_comp.setMaximumSize(QtCore.QSize(650, 550))
        self.cancelButton = QtWidgets.QPushButton(view_comp)
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
        self.formLayoutWidget = QtWidgets.QWidget(view_comp)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 290, 591, 171))
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
        self.labelStock = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelStock.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelStock.setFont(font)
        self.labelStock.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelStock.setObjectName("labelStock")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelStock)
        self.showStock = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showStock.setFont(font)
        self.showStock.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showStock.setObjectName("showStock")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.showStock)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelLab)
        self.showLab = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.showLab.setFont(font)
        self.showLab.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";\n"
" padding: 5px;")
        self.showLab.setObjectName("showLab")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.showLab)
        self.MAINLABEL = QtWidgets.QLabel(view_comp)
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
        self.MAINLABEL.setText("")
        self.MAINLABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.MAINLABEL.setObjectName("MAINLABEL")
        self.label_2 = QtWidgets.QLabel(view_comp)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 651, 551))
        self.label_2.setStyleSheet("background-color:#ffffff;\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.searchButton = QtWidgets.QPushButton(view_comp)
        self.searchButton.setGeometry(QtCore.QRect(470, 180, 171, 51))
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
        self.enterCid = QtWidgets.QLineEdit(view_comp)
        self.enterCid.setGeometry(QtCore.QRect(170, 130, 471, 40))
        self.enterCid.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterCid.setFont(font)
        self.enterCid.setStyleSheet("#enterCid{\n"
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
"#enterCid:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterCid:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterCid.setClearButtonEnabled(False)
        self.enterCid.setObjectName("enterCid")
        self.labelCid = QtWidgets.QLabel(view_comp)
        self.labelCid.setGeometry(QtCore.QRect(10, 130, 141, 40))
        self.labelCid.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus BK")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelCid.setFont(font)
        self.labelCid.setStyleSheet("font: 57 12pt \"Slate For OnePlus BK\";")
        self.labelCid.setObjectName("labelCid")
        self.line = QtWidgets.QFrame(view_comp)
        self.line.setGeometry(QtCore.QRect(22, 250, 611, 4))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.searchCid = QtWidgets.QPushButton(view_comp)
        self.searchCid.setGeometry(QtCore.QRect(560, 130, 81, 40))
        self.searchCid.setMinimumSize(QtCore.QSize(0, 40))
        self.searchCid.setStyleSheet("#searchCid{background-color: transparent;\n"
"border-color: transparent;\n"
"font: 57 10pt \"Slate For OnePlus Medium\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"color:#8aacc8;\n"
"}\n"
"#searchCid:hover{\n"
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
"#searchCid:pressed {\n"
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
        self.searchCid.setObjectName("searchCid")
        self.addComponent = QtWidgets.QPushButton(view_comp)
        self.addComponent.setGeometry(QtCore.QRect(320, 180, 151, 51))
        self.addComponent.setStyleSheet("#addComponent{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    text-decoration: underline;\n"
"color:rgb(65, 131, 197);\n"
"background-color: transparent;\n"
"border-color: transparent;\n"
"selection-color: transparent;\n"
"selection-background-color:transparent;\n"
"gridline-color: transparent;\n"
"}\n"
"#addComponent:hover{\n"
"color:rgb(0, 0, 127);\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    text-decoration: underline;\n"
"}\n"
"#addComponent:pressed{\n"
"color:purple;\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    text-decoration: underline;\n"
"}")
        self.addComponent.setObjectName("addComponent")
        self.issueComponent = QtWidgets.QPushButton(view_comp)
        self.issueComponent.setGeometry(QtCore.QRect(410, 470, 60, 60))
        self.issueComponent.setStyleSheet("#issueComponent {\n"
"background-color:transparent;\n"
"    border-image: url(:/admin/cart.png);\n"
"border-color:transparent;\n"
"border-style:outset;\n"
"border-radius:30px;\n"
"}\n"
"\n"
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
        self.modifyComponent = QtWidgets.QPushButton(view_comp)
        self.modifyComponent.setGeometry(QtCore.QRect(250, 470, 60, 60))
        self.modifyComponent.setStyleSheet("#modifyComponent {\n"
"background-color:transparent;\n"
"    border-image: url(:/others/modify.png);\n"
"border-color:#4D4D4C;\n"
"border-style:outset;\n"
"border-radius:30px;\n"
"}\n"
"\n"
"#modifyComponent:hover {\n"
"    border-color:transparent;\n"
"    border-radius:30px;\n"
"    border-image: url(:/others/modify2.png);\n"
"    background-color: rgb(25, 118, 210);\n"
"}\n"
"\n"
"#modifyComponent:pressed {\n"
"    background-color:#01579B;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.modifyComponent.setText("")
        self.modifyComponent.setIconSize(QtCore.QSize(50, 50))
        self.modifyComponent.setObjectName("modifyComponent")
        self.label = QtWidgets.QLabel(view_comp)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 71))
        self.label.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.deleteComponent = QtWidgets.QPushButton(view_comp)
        self.deleteComponent.setGeometry(QtCore.QRect(110, 470, 60, 60))
        self.deleteComponent.setStyleSheet("#deleteComponent {\n"
"background-color: transparent;\n"
"\n"
"border-style: inset;\n"
"border-radius:30px;\n"
"border-image:url(:/others/lel_delete.png);\n"
"}\n"
"#deleteComponent:hover {\n"
"    background-color: #DC3333;\n"
"    \n"
"    border-radius:30px;\n"
"    border-style:outset;\n"
"    border-image: url(:/others/lel_delete2.png);\n"
"}\n"
"\n"
"#deleteComponent:pressed {\n"
"    background-color: #b80000;\n"
"    border-color:#b80000;\n"
"    border-radius:25px;\n"
"    border-style:inset;\n"
"}")
        self.deleteComponent.setText("")
        self.deleteComponent.setIconSize(QtCore.QSize(50, 50))
        self.deleteComponent.setObjectName("deleteComponent")
        self.MAINLABEL.raise_()
        self.label_2.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.searchButton.raise_()
        self.enterCid.raise_()
        self.labelCid.raise_()
        self.line.raise_()
        self.searchCid.raise_()
        self.addComponent.raise_()
        self.issueComponent.raise_()
        self.modifyComponent.raise_()
        self.label.raise_()
        self.deleteComponent.raise_()
        self.searchButton.clicked.connect(lambda: self.searchComponent(view_comp))
        self.deleteComponent.clicked.connect(lambda: self.delete_Component(view_comp))
        self.searchCid.clicked.connect(lambda: self.openSearch(view_comp))   
        self.modifyComponent.clicked.connect(lambda:self.openModifyComponent(view_comp))
        self.issueComponent.clicked.connect(lambda:self.openIssueComponent(view_comp))
        self.addComponent.clicked.connect(self.openAddComponent)
        self.cancelButton.clicked.connect(view_comp.close)

        self.retranslateUi(view_comp)
        QtCore.QMetaObject.connectSlotsByName(view_comp)

    def openAddComponent(self):
        from add_comp import Ui_add_comp
        self.window5=QtWidgets.QWidget()
        self.ui5=Ui_add_comp()
        self.ui5.setupUi(self.window5)
        self.window5.show()    
                 
    def openIssueComponent(self, view_student):
        
        from issue_student import Ui_issueStudent
        self.window=QtWidgets.QWidget()
        self.ui=Ui_issueStudent()
        self.ui.setupUi(self.window)
        self.ui.setCid(self.enterCid.text())
        self.ui.setLab(self.showLab.text())
        self.window.show()
        
    def openModifyComponent(self, view_component):
        from modify_comp import Ui_modify_comp
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_modify_comp()
        self.ui6.setupUi(self.window6)
        self.ui6.setDetails([self.enterCid.text(), self.showName.text(), self.showStock.text(), self.showLab.text()])
        self.window6.show()     
        
    def changeText(self, a):
        self.enterCid.setText(a)
        
    def openSearch(self,delete_comp):
        from get_comp1 import Ui_getComp
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getComp()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        delete_comp.close()
        
    def delete_Component(self, delete_comp):
        from warning_dialogue_component import Ui_Dialog
        self.window7=QtWidgets.QDialog()
        self.ui7=Ui_Dialog()
        self.ui7.setupUi(self.window7)
        self.ui7.setCid(self.enterCid.text())
        self.window7.show()
        
    def searchComponent(self,delete_comp):
        import db
        a=db.fetchComponentDetails(self.enterCid.text())
        if(a==None):
            QtWidgets.QMessageBox.about(delete_comp, "Error!", "Component not found!")
        else:
            self.enterCid.setEnabled(False)
            self.showName.setText(a[1])
            self.showStock.setText(str(a[2]))
            self.showLab.setText(a[3])
            self.searchCid.setEnabled(False)
            self.deleteComponent.setEnabled(True)
            self.issueComponent.setEnabled(True)
            self.modifyComponent.setEnabled(True)



    def retranslateUi(self, view_comp):
        _translate = QtCore.QCoreApplication.translate
        view_comp.setWindowTitle(_translate("view_comp", "Component Details"))
        self.cancelButton.setText(_translate("view_comp", "CANCEL"))
        self.cancelButton.setShortcut(_translate("view_comp", "Esc"))
        self.labelName.setText(_translate("view_comp", "Component Name:"))
        self.showName.setText(_translate("view_comp", "Please enter Component ID"))
        self.labelStock.setText(_translate("view_comp", "Stock:"))
        self.showStock.setText(_translate("view_comp", "Please enter Component ID"))
        self.labelLab.setText(_translate("view_comp", "Lab:"))
        self.showLab.setText(_translate("view_comp", "Please enter Component ID"))
        self.searchButton.setText(_translate("view_comp", "SEARCH"))
        self.enterCid.setPlaceholderText(_translate("view_comp", "Component Product ID/Barcode No."))
        self.labelCid.setText(_translate("view_comp", "Component ID:"))
        self.searchCid.setText(_translate("view_comp", "GET ID"))
        self.addComponent.setText(_translate("view_comp", "Add New Component?"))
        self.issueComponent.setToolTip(_translate("view_comp", "<html><head/><body><p>Issue Component</p></body></html>"))
        self.modifyComponent.setToolTip(_translate("view_comp", "<html><head/><body><p>Modify Component</p></body></html>"))
        self.modifyComponent.setWhatsThis(_translate("view_comp", "<html><head/><body><p>Modify Component</p></body></html>"))
        self.label.setText(_translate("view_comp", "Component Details"))
        self.deleteComponent.setWhatsThis(_translate("view_comp", "<html><head/><body><p>Delete Component</p></body></html>"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_comp = QtWidgets.QWidget()
    ui = Ui_view_comp()
    ui.setupUi(view_comp)
    view_comp.show()
    sys.exit(app.exec_())

