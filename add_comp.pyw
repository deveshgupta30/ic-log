# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_comp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_comp(object):
    def setupUi(self, add_comp):
        add_comp.setObjectName("add_comp")
        add_comp.resize(650, 550)
        add_comp.setMinimumSize(QtCore.QSize(650, 550))
        add_comp.setMaximumSize(QtCore.QSize(650, 550))
        self.confirmButton = QtWidgets.QPushButton(add_comp)
        self.confirmButton.setEnabled(True)
        self.confirmButton.setGeometry(QtCore.QRect(450, 490, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_comp.setWindowIcon(icon)
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
"}")
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(add_comp)
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
        self.formLayoutWidget = QtWidgets.QWidget(add_comp)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 110, 631, 344))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
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
"}")
        self.enterName.setClearButtonEnabled(True)
        self.enterName.setObjectName("enterName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enterName)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.labelCid = QtWidgets.QLabel(self.formLayoutWidget)
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCid)
        self.enterCid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.enterCid.setMinimumSize(QtCore.QSize(430, 40))
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
"}\n"
"#enterCid:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enterCid:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.enterCid.setClearButtonEnabled(True)
        self.enterCid.setObjectName("enterCid")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.enterCid)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem2)
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
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelStock)
        self.spinStock = QtWidgets.QSpinBox(self.formLayoutWidget)
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
"}")
        self.spinStock.setMaximum(1000000)
        self.spinStock.setObjectName("spinStock")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinStock)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.LabelRole, spacerItem3)
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
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelLab)
        self.enterLab = QtWidgets.QLineEdit(self.formLayoutWidget)
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
"}")
        self.enterLab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enterLab.setClearButtonEnabled(True)
        self.enterLab.setObjectName("enterLab")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.enterLab)
        self.MAINLABEL = QtWidgets.QLabel(add_comp)
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
        self.label_2 = QtWidgets.QLabel(add_comp)
        self.label_2.setGeometry(QtCore.QRect(-30, 70, 731, 551))
        self.label_2.setStyleSheet("background-color:#ffffff")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()
        self.formLayoutWidget.raise_()
        self.MAINLABEL.raise_()
        self.confirmButton.clicked.connect(lambda: self.addComponent(add_comp))
        self.cancelButton.clicked.connect(add_comp.close)

        self.retranslateUi(add_comp)
        QtCore.QMetaObject.connectSlotsByName(add_comp)
    def addComponent(self, add_comp):
        import db
        if(self.spinStock.value()==0 or self.enterName.text()=='' or self.enterCid.text() == '' or self.enterLab.text()==''):
            QtWidgets.QMessageBox.about(add_comp, "Invalid Entry!", "Please Fill all the details!")
        else:
            db.addComponent([self.enterName.text(), self.enterCid.text(), self.spinStock.value(), self.enterLab.text()])
            QtWidgets.QMessageBox.about(add_comp, "Successfully Added!", self.enterName.text()+ " has been successfully added!")
    def retranslateUi(self, add_comp):
        _translate = QtCore.QCoreApplication.translate
        add_comp.setWindowTitle(_translate("add_comp", "Add Component"))
        self.confirmButton.setText(_translate("add_comp", "+   ADD"))
        self.confirmButton.setShortcut(_translate("add_comp", "Return"))
        self.cancelButton.setText(_translate("add_comp", "CANCEL"))
        self.cancelButton.setShortcut(_translate("add_comp", "Esc"))
        self.labelName.setText(_translate("add_comp", "Component Name"))
        self.enterName.setPlaceholderText(_translate("add_comp", "Component Name"))
        self.labelCid.setText(_translate("add_comp", "Component ID"))
        self.enterCid.setPlaceholderText(_translate("add_comp", "Component Product ID/Barcode No."))
        self.labelStock.setText(_translate("add_comp", "Stock"))
        self.labelLab.setText(_translate("add_comp", "Lab"))
        self.enterLab.setPlaceholderText(_translate("add_comp", "Lab to which it belongs"))
        self.MAINLABEL.setText(_translate("add_comp", "Add Component"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_comp = QtWidgets.QWidget()
    ui = Ui_add_comp()
    ui.setupUi(add_comp)
    add_comp.show()
    sys.exit(app.exec_())

