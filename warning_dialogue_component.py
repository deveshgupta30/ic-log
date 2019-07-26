# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 100)
        Dialog.setMinimumSize(QtCore.QSize(390, 100))
        Dialog.setMaximumSize(QtCore.QSize(390, 100))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/alert_box/Sign-Alert-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 201, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/alert_box/Sign-Alert-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(lambda: self.deleteComponent(Dialog))
        self.buttonBox.rejected.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warning!"))
        self.label_2.setText(_translate("Dialog", "Are you sure you want to delete?"))
        
    def deleteComponent(self, Dialog):
        import db
        db.delComp(Cid)
        QtWidgets.QMessageBox.about(Dialog, 'Successfully Deleted!', 'Component Successfully Deleted!')
        Dialog.close()
        
    def setCid(self,a):
        global Cid
        Cid=a

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

