# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_getAdmin(object):
    def setupUi(self, getAdmin):
        getAdmin.setObjectName("getAdmin")
        getAdmin.resize(650, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(getAdmin.sizePolicy().hasHeightForWidth())
        getAdmin.setSizePolicy(sizePolicy)
        getAdmin.setMinimumSize(QtCore.QSize(650, 650))
        getAdmin.setMaximumSize(QtCore.QSize(650, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        getAdmin.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(getAdmin)
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
        self.label = QtWidgets.QLabel(getAdmin)
        self.label.setGeometry(QtCore.QRect(10, 30, 251, 40))
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
        self.searchName = QtWidgets.QLineEdit(getAdmin)
        self.searchName.setGeometry(QtCore.QRect(150, 30, 491, 40))
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
        self.label_2 = QtWidgets.QLabel(getAdmin)
        self.label_2.setGeometry(QtCore.QRect(-60, -80, 821, 781))
        self.label_2.setStyleSheet("\n"
"background-color:qlineargradient(spread:pad, x1:0.492, y1:0, x2:0.501925, y2:0.796, stop:0 rgba(40, 53, 147, 255), stop:1 rgba(    131, 185, 255, 255))\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.listAdmin = QtWidgets.QListWidget(getAdmin)
        self.listAdmin.setGeometry(QtCore.QRect(10, 100, 631, 471))
        self.listAdmin.setStyleSheet("#listAdmin{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 1px solid #002171;\n"
"border-style: outset;\n"
"}\n"
"#listAdmin:hover{font: 57 9pt \"Slate For OnePlus Medium\";\n"
"border: 3px solid #002171;\n"
"}\n"
"")
        self.listAdmin.setObjectName("listAdmin")
        self.label_2.raise_()
        self.closeButton.raise_()
        self.label.raise_()
        self.searchName.raise_()
        self.listAdmin.raise_()
        self.searchName.textChanged.connect(lambda: self.searchAdmin())
        self.listAdmin.itemDoubleClicked.connect(lambda: self.doubleClick(getAdmin))
        self.closeButton.clicked.connect(lambda: self.openDeleteAdmin(getAdmin))

        self.retranslateUi(getAdmin)
        QtCore.QMetaObject.connectSlotsByName(getAdmin)
    def openDeleteAdmin(self,getAdmin):
        from view_admin import Ui_delete_admin
        self.window=QtWidgets.QWidget()
        self.ui1=Ui_delete_admin()
        self.ui1.setupUi(self.window)
        self.window.show()  
        getAdmin.close()   
        
    def doubleClick(self, getAdmin):
        from view_admin import Ui_delete_admin
        import db
        a=self.listAdmin.currentItem().text()
        b=db.fetchAdminE_ID(a)
        self.window=QtWidgets.QWidget()
        self.ui1=Ui_delete_admin()
        self.ui1.setupUi(self.window)
        self.ui1.changeText(b)
        self.window.show()  
        getAdmin.close()
        
    def searchAdmin(self):
        import db
        self.listAdmin.clear()
        self.listAdmin.addItems(db.searchAdminDB(self.searchName.text()))

    def retranslateUi(self, getAdmin):
        _translate = QtCore.QCoreApplication.translate
        getAdmin.setWindowTitle(_translate("getAdmin", "Get Admin Employee ID"))
        self.closeButton.setText(_translate("getAdmin", "×  Close"))
        self.closeButton.setShortcut(_translate("getAdmin", "Esc"))
        self.label.setText(_translate("getAdmin", "Name of Admin:"))
        self.searchName.setPlaceholderText(_translate("getAdmin", "Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getAdmin = QtWidgets.QWidget()
    ui = Ui_getAdmin()
    ui.setupUi(getAdmin)
    getAdmin.show()
    sys.exit(app.exec_())

