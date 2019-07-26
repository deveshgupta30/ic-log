# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(450, 480)
        About.setMinimumSize(QtCore.QSize(450, 480))
        About.setMaximumSize(QtCore.QSize(450, 480))
        About.setStyleSheet("background-color: white")
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(60, 10, 121, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/others/APP ICON_EDIT.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 151, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/APP ICON_EDIT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.label_2.setStyleSheet("font: 22pt \"Slate For OnePlus Bk\";\n"
"color:#000051")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 451, 21))
        self.label_3.setStyleSheet("color:#001064")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(About)
        self.line.setGeometry(QtCore.QRect(20, 140, 411, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 381, 221))
        self.label_4.setStyleSheet("font: 25 8pt \"Slate For OnePlus Light\";")
        self.label_4.setObjectName("label_4")
        self.closeButton = QtWidgets.QPushButton(About)
        self.closeButton.setGeometry(QtCore.QRect(330, 410, 93, 51))
        self.closeButton.setStyleSheet("#closeButton{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 21px;\n"
"}\n"
"#closeButton:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#closeButton:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.closeButton.raise_()
        self.closeButton.clicked.connect(About.close)
        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label_2.setText(_translate("About", "ICLog"))
        self.label_3.setText(_translate("About", "v 2.1.1"))
        self.label_4.setText(_translate("About", "ICLog\n"
"Version 2.1.1 (Beta)\n"
"© 2018 Kugelblitz. All rights reserved.\n"
"\n"
"\n"
"Project made possible by:\n"
"G Sriram\n"
"Devesh Gupta\n"
"Anitha Rathnam KV\n"
"Sahana KV\n"
"Sufiya Tahseen\n"
"Kushal Gowda CP"))
        self.closeButton.setText(_translate("About", "CLOSE"))
        self.closeButton.setShortcut(_translate("About", "Esc"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

