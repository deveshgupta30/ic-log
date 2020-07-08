# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import feedback

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(500, 500)
        About.setMinimumSize(QtCore.QSize(500, 500))
        About.setMaximumSize(QtCore.QSize(500, 500))
        About.setStyleSheet("background-color: white")
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 501))
        self.label.setStyleSheet("border-image: url(:/Wallpaper/about.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/others/APP ICON_EDIT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(About)
        self.closeButton.setGeometry(QtCore.QRect(200, 450, 93, 41))
        self.closeButton.setStyleSheet("#closeButton{\n"
"background-color:transparent;\n"
"color: white;\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"   \n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"border-radius: 15px;\n"
"}\n"
"#closeButton:hover{\n"
"background-color:white;\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"    color: #004BA0;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 15px;\n"
"}\n"
"#closeButton:pressed{\n"
"background-color:rgba(255, 255, 255, 220);\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.feedbackButton = QtWidgets.QPushButton(About)
        self.feedbackButton.setGeometry(QtCore.QRect(440, 450, 61, 51))
        self.feedbackButton.setAutoFillBackground(False)
        self.feedbackButton.setStyleSheet("background-color: transparent\n"
"")
        self.feedbackButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICLog icons/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.feedbackButton.setIcon(icon)
        self.feedbackButton.setIconSize(QtCore.QSize(30, 30))
        self.feedbackButton.setObjectName("feedbackButton")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 461, 131))
        self.label_2.setStyleSheet("border-color: white;\n"
"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 225)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 131, 131))
        self.label_3.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/ICLog icons/ICLog_png.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(220, 20, 241, 131))
        self.label_4.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"font: 25 36pt \"Slate For OnePlus\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(About)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 461, 271))
        self.label_5.setStyleSheet("border-color: white;\n"
"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 225)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(About)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 251, 61))
        self.label_7.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"font: 25 9pt \"Slate For OnePlus\";")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(About)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 231, 31))
        self.label_6.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"font: 25 9pt \"Slate For OnePlus\";"
"font-weight: bold")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(About)
        self.label_8.setGeometry(QtCore.QRect(140, 280, 220, 151))
        self.label_8.setStyleSheet("background-color: transparent;\n"
"border-color: transparent;\n"
"font: 25 9pt \"Slate For OnePlus\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.closeButton.clicked.connect(About.close)
        self.feedbackButton.clicked.connect(self.openfb)
        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)
    def openfb(self):
        self.window2=QtWidgets.QWidget()
        self.ui2=feedback.Ui_feedback()
        self.ui2.setupUi(self.window2)
        self.window2.show()
    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About ICLog"))
        self.closeButton.setText(_translate("About", "CLOSE"))
        self.closeButton.setShortcut(_translate("About", "Esc"))
        self.feedbackButton.setWhatsThis(_translate("About", "<html><head/><body><p>Feedback</p></body></html>"))
        self.label_4.setText(_translate("About", "ICLog"))
        self.label_7.setText(_translate("About", "ICLog\n"
"Version 2.1.8 (Beta)\n"
"© ICLog 2018."))
        self.label_6.setText(_translate("About", "Project made possible by:"))
        self.label_8.setText(_translate("About", "Team Kugelblitz,/nCMR University."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

