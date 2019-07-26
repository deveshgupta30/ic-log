# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_portal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_student_portal(object):
    def setupUi(self, student_portal):
        student_portal.setObjectName("student_portal")
        student_portal.resize(1000, 700)
        student_portal.setMinimumSize(QtCore.QSize(1000, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        student_portal.setWindowIcon(icon)
        student_portal.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(student_portal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 1001, 661))
        self.label.setStyleSheet("background-color: #e3f2fd;\n"
"border-style: inset;\n"
"border-radius: 10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.signOut = QtWidgets.QPushButton(self.centralwidget)
        self.signOut.setGeometry(QtCore.QRect(890, 10, 101, 31))
        self.signOut.setStyleSheet("#signOut{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"font: 11pt \"Slate For OnePlus Bk\";\n"
"}\n"
"#signOut:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #73e8ff;\n"
"    font: 11pt \"Slate For OnePlus Bk\";\n"
"    text-decoration: underline;\n"
"}\n"
"#signOut:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 11pt \"Slate For OnePlus Bk\";\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/alert_box/signout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signOut.setIcon(icon)
        self.signOut.setObjectName("signOut")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1001, 71))
        self.label_4.setStyleSheet("background-color: #1a237e;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/alert_box/admin2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.adminButton = QtWidgets.QPushButton(self.centralwidget)
        self.adminButton.setGeometry(QtCore.QRect(320, 170, 150, 150))
        self.adminButton.setStyleSheet("#adminButton{\n"
"border-image: url(:/admin/admin1.png);\n"
"background: transparent;}\n"
"#adminButton:hover{\n"
"border-image: url(:/alert_box/admin2.png);\n"
"background: #1976D2;\n"
"border-radius: 20px;\n"
"}\n"
"#adminButton:pressed{\n"
"border-image: url(:/alert_box/admin2.png);\n"
"background: #1a237e;\n"
"border-radius: 20px;\n"
"}")
        self.adminButton.setText("")
        self.adminButton.setIconSize(QtCore.QSize(150, 150))
        self.adminButton.setObjectName("adminButton")
        self.studentButton = QtWidgets.QPushButton(self.centralwidget)
        self.studentButton.setGeometry(QtCore.QRect(580, 170, 150, 150))
        self.studentButton.setStyleSheet("#studentButton{\n"
"border-image:url(:/student/Student1.png);\n"
"background: transparent;\n"
"\n"
"}\n"
"#studentButton:hover{\n"
"border-image: url(:/alert_box/Student2.png);\n"
"background: #1976D2;\n"
"border-radius: 20px;\n"
"\n"
"}\n"
"#studentButton:pressed{\n"
"border-image: url(:/alert_box/Student2.png);\n"
"background: #1a237e;\n"
"border-radius: 20px;\n"
"}")
        self.studentButton.setText("")
        self.studentButton.setIconSize(QtCore.QSize(130, 130))
        self.studentButton.setObjectName("studentButton")
        self.componentButton = QtWidgets.QPushButton(self.centralwidget)
        self.componentButton.setGeometry(QtCore.QRect(810, 170, 150, 150))
        self.componentButton.setStyleSheet("#componentButton{\n"
"border-image: url(:/others/Components2.png);\n"
"background: transparent;}\n"
"#componentButton:hover{\n"
"border-image: url(:/alert_box/Components.png);\n"
"background: #1976D2;\n"
"border-radius: 20px;\n"
"}\n"
"#componentButton:pressed{\n"
"border-image: url(:/alert_box/Components.png);\n"
"background: #1a237e;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.componentButton.setText("")
        self.componentButton.setIconSize(QtCore.QSize(150, 150))
        self.componentButton.setObjectName("componentButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 231, 581))
        self.label_2.setStyleSheet("border-color: #002171;\n"
"background-color: white;\n"
"border-style: inset;\n"
"border-radius: 30px;\n"
"border-color:white")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 231, 31))
        self.label_3.setStyleSheet("color: black;\n"
"font: 57 15pt \"Slate For OnePlus Medium\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 190, 101, 31))
        self.label_7.setStyleSheet("font: 57 9pt \"Slate For OnePlus Medium\";\n"
"color: #000063;")
        self.label_7.setObjectName("label_7")
        self.approveButton = QtWidgets.QPushButton(self.centralwidget)
        self.approveButton.setGeometry(QtCore.QRect(440, 420, 150, 150))
        self.approveButton.setStyleSheet("#approveButton{\n"
"border-image: url(:/others/approve comp2.png);\n"
"background: transparent;}\n"
"#approveButton:hover{\n"
"border-image:url(:/others/approve comp3.png);\n"
"background: #1976D2;\n"
"border-radius: 20px;\n"
"}\n"
"#approveButton:pressed{\n"
"border-image: url(:/others/approve comp3.png);\n"
"background: #1a237e;\n"
"border-radius: 20px;\n"
"}")
        self.approveButton.setText("")
        self.approveButton.setIconSize(QtCore.QSize(130, 130))
        self.approveButton.setObjectName("approveButton")
        self.dueButton = QtWidgets.QPushButton(self.centralwidget)
        self.dueButton.setGeometry(QtCore.QRect(710, 420, 150, 150))
        self.dueButton.setStyleSheet("#dueButton{\n"
"border-image: url(:/others/due2.png);\n"
"background: transparent;}\n"
"#dueButton:hover{\n"
"border-image: url(:/others/due3.png);\n"
"background: #1976D2;\n"
"border-radius: 20px;\n"
"}\n"
"#dueButton:pressed{\n"
"border-image:url(:/others/due3.png);\n"
"background: #1a237e;\n"
"border-radius: 20px;\n"
"}")
        self.dueButton.setText("")
        self.dueButton.setIconSize(QtCore.QSize(130, 130))
        self.dueButton.setObjectName("dueButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 160, 211, 20))
        self.line.setStyleSheet("color: rgb(190, 190, 190);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.adminProfile = QtWidgets.QPushButton(self.centralwidget)
        self.adminProfile.setGeometry(QtCore.QRect(60, 0, 791, 51))
        self.adminProfile.setStyleSheet("#adminProfile{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: white;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"#adminProfile:hover{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #73e8ff;\n"
"    font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"\n"
"}\n"
"#adminProfile:pressed{\n"
"background-color: transparent;\n"
"border-color:transparent;\n"
"color: #29b6f6;\n"
"font: 17pt \"Slate For OnePlus Bk\";\n"
"text-align: left;\n"
"}\n"
"")
        self.adminProfile.setObjectName("adminProfile")
        self.lcdRequested = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdRequested.setGeometry(QtCore.QRect(70, 220, 171, 101))
        self.lcdRequested.setStyleSheet("color: blue;\n"
"")
        self.lcdRequested.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdRequested.setLineWidth(0)
        self.lcdRequested.setDigitCount(5)
        self.lcdRequested.setObjectName("lcdRequested")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 330, 211, 31))
        self.label_8.setStyleSheet("font: 57 9pt \"Slate For OnePlus Medium\";\n"
"color: #000063;")
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 480, 211, 31))
        self.label_13.setStyleSheet("font: 57 9pt \"Slate For OnePlus Medium\";\n"
"color: #000063;")
        self.label_13.setObjectName("label_13")
        self.lcdRequested_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdRequested_2.setGeometry(QtCore.QRect(70, 370, 171, 101))
        self.lcdRequested_2.setStyleSheet("color: #64dd17;\n"
"")
        self.lcdRequested_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdRequested_2.setLineWidth(0)
        self.lcdRequested_2.setDigitCount(5)
        self.lcdRequested_2.setObjectName("lcdRequested_2")
        self.lcdBorrowed = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdBorrowed.setGeometry(QtCore.QRect(70, 520, 171, 101))
        self.lcdBorrowed.setStyleSheet("color: red;")
        self.lcdBorrowed.setLineWidth(0)
        self.lcdBorrowed.setObjectName("lcdBorrowed")
        self.label_4.raise_()
        self.label.raise_()
        self.signOut.raise_()
        self.label_5.raise_()
        self.adminButton.raise_()
        self.studentButton.raise_()
        self.componentButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.approveButton.raise_()
        self.dueButton.raise_()
        self.line.raise_()
        self.adminProfile.raise_()
        self.lcdRequested.raise_()
        self.label_8.raise_()
        self.label_13.raise_()
        self.lcdRequested_2.raise_()
        self.lcdBorrowed.raise_()
        student_portal.setCentralWidget(self.centralwidget)
        self.adminButton.clicked.connect(self.openViewAdmin)
        self.adminProfile.clicked.connect(self.openViewProfile)
        self.componentButton.clicked.connect(self.openViewComponent)
        self.signOut.clicked.connect(lambda: self.openIndex(student_portal))
        self.studentButton.clicked.connect(self.openViewStudent)
        self.approveButton.clicked.connect(self.openApproveComponent)
        self.dueButton.clicked.connect(self.openComponentDues)
        self.retranslateUi(student_portal)

        QtCore.QMetaObject.connectSlotsByName(student_portal)
    def openIndex(self, student_portal):
        
        from admin_login import Ui_Form
        self.window4=QtWidgets.QWidget()
        self.ui4=Ui_Form()
        self.ui4.setupUi(self.window4)
        self.window4.show()
        student_portal.close()
        
    def setDashDetails(self, lab, borrowed, requested):
        self.lcdRequested.display(lab)
        self.lcdRequested_2.display(requested)
        self.lcdBorrowed.display(borrowed)
        
    def openComponentDues(self):
        import db
        from due_comp import Ui_compDue
        self.window10=QtWidgets.QWidget()
        self.ui10=Ui_compDue()
        a=db.getBorrowStudentList(db.getAdminLabNumber(e_id))

        self.ui10.setupUi(self.window10)
        self.ui10.setLab(db.getAdminLabNumber(e_id))
        self.ui10.setItems(a)
        self.window10.show()       
        
    def openApproveComponent(self):
        import db
        from approve_comp import Ui_approveComp
        a=db.getReqStudentList(db.getAdminLabNumber(e_id))
        
        self.window11=QtWidgets.QWidget()
        self.ui11=Ui_approveComp()
        self.ui11.setupUi(self.window11)
        self.ui11.setLab(db.getAdminLabNumber(e_id))
        self.ui11.setList(a)
        self.window11.show() 
        
    def openViewComponent(self):
        from view_comp import Ui_view_comp
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_view_comp()
        self.ui6.setupUi(self.window6)
        self.window6.show()    
                
    def openViewAdmin(self):
        from view_admin import Ui_delete_admin
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_delete_admin()
        self.ui6.setupUi(self.window6)
        self.window6.show()
        
    def openViewStudent(self):
        from view_student import Ui_view_student
        self.window6=QtWidgets.QWidget()
        self.ui6=Ui_view_student()
        self.ui6.setupUi(self.window6)
        self.window6.show()    
        
    def openViewProfile(self):
        from admin_profile import Ui_admin_profile
        import db
        self.window1=QtWidgets.QWidget()
        self.ui1=Ui_admin_profile()
        self.ui1.setupUi(self.window1)
        self.ui1.setDetails(list(db.fetchAdminDetails(e_id)))
        self.window1.show()     
        
    def setMame(self, text, student_portal):
        self.adminProfile.setText(text)
    def setTitle(self,text, student_portal):
        student_portal.setWindowTitle(text)     
        
    def setEID(self, text):
        global e_id
        e_id=text
        
    def retranslateUi(self, student_portal):
        _translate = QtCore.QCoreApplication.translate
        student_portal.setWindowTitle(_translate("stude2nt_portal", "Admin Portal"))
        self.signOut.setText(_translate("student_portal", "Sign Out"))
        self.adminButton.setToolTip(_translate("student_portal", "<html><head/><body><p>Admin</p></body></html>"))
        self.studentButton.setToolTip(_translate("student_portal", "<html><head/><body><p>Student</p></body></html>"))
        self.componentButton.setToolTip(_translate("student_portal", "<html><head/><body><p>Components</p></body></html>"))
        self.label_3.setText(_translate("student_portal", "DASHBOARD"))
        self.label_7.setText(_translate("student_portal", "Lab Number"))
        self.approveButton.setToolTip(_translate("student_portal", "<html><head/><body><p>Approve Components</p></body></html>"))
        self.dueButton.setToolTip(_translate("student_portal", "<html><head/><body><p>Component Dues</p></body></html>"))
        self.adminProfile.setText(_translate("student_portal", "Admin"))
        self.label_8.setText(_translate("student_portal", "Total Requested Components"))
        self.label_13.setText(_translate("student_portal", "Total Component Dues"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_portal = QtWidgets.QMainWindow()
    ui = Ui_student_portal()
    ui.setupUi(student_portal)
    student_portal.show()
    sys.exit(app.exec_())

