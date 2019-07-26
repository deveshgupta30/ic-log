# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_comp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_modify_comp(object):
    def setupUi(self, modify_comp):
        modify_comp.setObjectName("modify_comp")
        modify_comp.resize(650, 550)
        modify_comp.setMinimumSize(QtCore.QSize(650, 550))
        modify_comp.setMaximumSize(QtCore.QSize(650, 550))
        self.confirmButton = QtWidgets.QPushButton(modify_comp)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        modify_comp.setWindowIcon(icon)
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
        self.cancelButton = QtWidgets.QPushButton(modify_comp)
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
        self.formLayoutWidget = QtWidgets.QWidget(modify_comp)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 230, 631, 231))
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
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
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
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enterName)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelStock)
        self.spinStock = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinStock.setEnabled(False)
        self.spinStock.setMinimumSize(QtCore.QSize(0, 40))
        self.spinStock.setStyleSheet("#spinStock{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#spinStock:hover {\n"
"    border-style: inset;\n"
"}\n"
"#spinStock:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}\n"
"#spinStock:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}\n"
"")
        self.spinStock.setMaximum(1000000)
        self.spinStock.setObjectName("spinStock")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinStock)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
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
        self.enterLab = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterLab.setEnabled(False)
        self.enterLab.setMinimumSize(QtCore.QSize(430, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.enterLab.setFont(font)
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
        self.enterLab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterLab.setClearButtonEnabled(True)
        self.enterLab.setObjectName("enterLab")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.enterLab)
        self.MAINLABEL = QtWidgets.QLabel(modify_comp)
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
        self.label_2 = QtWidgets.QLabel(modify_comp)
        self.label_2.setGeometry(QtCore.QRect(-30, 82, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(modify_comp)
        self.line.setGeometry(QtCore.QRect(-30, 210, 731, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.searchCid = QtWidgets.QPushButton(modify_comp)
        self.searchCid.setGeometry(QtCore.QRect(560, 110, 81, 40))
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
        self.searchButton = QtWidgets.QPushButton(modify_comp)
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
        self.labelCid = QtWidgets.QLabel(modify_comp)
        self.labelCid.setGeometry(QtCore.QRect(10, 110, 141, 40))
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
        self.enterCid = QtWidgets.QLineEdit(modify_comp)
        self.enterCid.setGeometry(QtCore.QRect(170, 110, 471, 40))
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

        self.enterCid.setObjectName("enterCid")
        self.label_2.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.line.raise_()
        self.searchButton.raise_()
        self.labelCid.raise_()
        self.enterCid.raise_()
        self.searchCid.raise_()
        self.searchButton.clicked.connect(lambda: self.searchComponent(modify_comp))
        self.searchCid.clicked.connect(lambda:self.openSearch(modify_comp))
        self.confirmButton.clicked.connect(lambda: self.modifyComponent(modify_comp))
        self.cancelButton.clicked.connect(modify_comp.close)

        self.retranslateUi(modify_comp)
        QtCore.QMetaObject.connectSlotsByName(modify_comp)
    def openSearch(self,modify_comp):
        from get_comp import Ui_getComp
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_getComp()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        modify_comp.close()
        
    def setDetails(self,a):
        self.enterCid.setText(a[0])
        self.enterCid.setEnabled(False)
        self.enterName.setEnabled(True)
        self.enterName.setText(a[1])
        self.spinStock.setEnabled(True)
        self.spinStock.setValue(int(a[2]))
        self.enterLab.setEnabled(True)
        self.enterLab.setText(a[3])
        self.confirmButton.setEnabled(True)
        self.searchCid.setEnabled(False) 
         
    def changeText(self, a):
        self.enterCid.setText(a)
        
    def searchComponent(self,modify_comp):
        import db
        a=db.fetchComponentDetails(self.enterCid.text())
        if(a==None):
            QtWidgets.QMessageBox.about(modify_comp, "Error!", "Employee ID not found!")
        else:
            self.enterCid.setEnabled(False)
            self.enterName.setEnabled(True)
            self.enterName.setText(a[1])
            self.spinStock.setEnabled(True)
            self.spinStock.setValue(int(a[2]))
            self.enterLab.setEnabled(True)
            self.enterLab.setText(a[3])
            self.confirmButton.setEnabled(True)
            self.searchCid.setEnabled(False)
    def modifyComponent(self, modify_comp):
        import db
        if(self.spinStock.value()==0 or self.enterName.text()=='' or self.enterCid.text() == '' or self.enterLab.text()==''):
            QtWidgets.QMessageBox.about(modify_comp, "Invalid Entry!", "Please Fill all the details!")
        else:
            db.modifyComponent([self.enterName.text(), self.spinStock.value(), self.enterLab.text(), self.enterCid.text()])
            QtWidgets.QMessageBox.about(modify_comp, "Successfully Modified!", "Component Details Succesfully Modified!")
    def retranslateUi(self, modify_comp):
        _translate = QtCore.QCoreApplication.translate
        modify_comp.setWindowTitle(_translate("modify_comp", "Modify Component"))
        self.confirmButton.setText(_translate("modify_comp", "MODIFY"))
        self.cancelButton.setText(_translate("modify_comp", "CANCEL"))
        self.cancelButton.setShortcut(_translate("modify_comp", "Esc"))
        self.labelName.setText(_translate("modify_comp", "Component Name"))
        self.enterName.setPlaceholderText(_translate("modify_comp", "Component Name"))
        self.labelStock.setText(_translate("modify_comp", "Stock"))
        self.labelLab.setText(_translate("modify_comp", "Lab"))
        self.enterLab.setPlaceholderText(_translate("modify_comp", "Lab to which it belongs"))
        self.MAINLABEL.setText(_translate("modify_comp", "Modify Component"))
        self.searchCid.setText(_translate("modify_comp", "GET ID"))
        self.searchButton.setText(_translate("modify_comp", "Search"))
        self.searchButton.setShortcut(_translate("modify_comp", "Return"))
        self.labelCid.setText(_translate("modify_comp", "Component ID"))
        self.enterCid.setPlaceholderText(_translate("modify_comp", "Component Product ID/Barcode No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modify_comp = QtWidgets.QWidget()
    ui = Ui_modify_comp()
    ui.setupUi(modify_comp)
    modify_comp.show()
    sys.exit(app.exec_())

