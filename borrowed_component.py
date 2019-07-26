# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borrowed_component.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_requestComp(object):
    def setupUi(self, requestComp):
        requestComp.setObjectName("requestComp")
        requestComp.resize(650, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(requestComp.sizePolicy().hasHeightForWidth())
        requestComp.setSizePolicy(sizePolicy)
        requestComp.setMinimumSize(QtCore.QSize(650, 660))
        requestComp.setMaximumSize(QtCore.QSize(650, 660))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/student/Student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        requestComp.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(requestComp)
        self.closeButton.setGeometry(QtCore.QRect(280, 610, 93, 41))
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
        self.label = QtWidgets.QLabel(requestComp)
        self.label.setGeometry(QtCore.QRect(120, 20, 421, 40))
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
        self.label_2 = QtWidgets.QLabel(requestComp)
        self.label_2.setGeometry(QtCore.QRect(-30, -30, 821, 781))
        self.label_2.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.listBorrowed = QtWidgets.QListWidget(requestComp)
        self.listBorrowed.setGeometry(QtCore.QRect(10, 80, 631, 501))
        self.listBorrowed.setStyleSheet("#listBorrowed{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 2px solid #002171;\n"
"border-style: outset;\n"
"}")
        self.listBorrowed.setObjectName("listBorrowed")
        self.label_2.raise_()
        self.closeButton.raise_()
        self.label.raise_()
        self.listBorrowed.raise_()
        self.closeButton.clicked.connect(requestComp.close)
        self.retranslateUi(requestComp)
        QtCore.QMetaObject.connectSlotsByName(requestComp)
    def setDetails(self,a):
        self.listBorrowed.addItems(a)
    def retranslateUi(self, requestComp):
        _translate = QtCore.QCoreApplication.translate
        requestComp.setWindowTitle(_translate("requestComp", "Borrowed Components"))
        self.closeButton.setText(_translate("requestComp", "×  Close"))
        self.closeButton.setShortcut(_translate("requestComp", "Esc"))
        self.label.setText(_translate("requestComp", "BORROWED COMPONENTS"))
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    requestComp = QtWidgets.QWidget()
    ui = Ui_requestComp()
    ui.setupUi(requestComp)
    requestComp.show()
    sys.exit(app.exec_())

