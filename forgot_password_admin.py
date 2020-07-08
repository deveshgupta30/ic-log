# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgot_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc
class Ui_forgotpassword(object):
    def setupUi(self, forgotpassword):
        forgotpassword.setObjectName("forgotpassword")
        forgotpassword.resize(400, 450)
        forgotpassword.setMinimumSize(QtCore.QSize(400, 450))
        forgotpassword.setMaximumSize(QtCore.QSize(400, 450))
        self.email_input = QtWidgets.QLineEdit(forgotpassword)
        self.email_input.setGeometry(QtCore.QRect(120, 80, 261, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/admin/admin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        forgotpassword.setWindowIcon(icon)
        self.email_input.setStyleSheet("#email_input{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#email_input:hover {\n"
"    border-style: inset;\n"
"}\n"
"#email_input:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}")
        self.email_input.setAlignment(QtCore.Qt.AlignCenter)
        self.email_input.setObjectName("email_input")
        self.enter_otp = QtWidgets.QLineEdit(forgotpassword)
        self.enter_otp.setEnabled(False)
        self.enter_otp.setGeometry(QtCore.QRect(100, 140, 200, 40))
        self.enter_otp.setStyleSheet("#enter_otp{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#enter_otp:hover {\n"
"    border-style: inset;\n"
"}\n"
"#enter_otp:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}\n"
"#enter_otp:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}")
        self.enter_otp.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_otp.setObjectName("enter_otp")
        self.send_otp = QtWidgets.QPushButton(forgotpassword)
        self.send_otp.setGeometry(QtCore.QRect(20, 140, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Slate For OnePlus Medium")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.send_otp.setFont(font)
        self.send_otp.setStyleSheet("#send_otp{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 12px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#send_otp:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#send_otp:pressed{\n"
"background-color:#1A237E;\n"
"}\n"
"#send_otp:disabled{\n"
"background-color:#bbdefb;\n"
"color: #eeffff;\n"
"}\n"
"")
        self.send_otp.setObjectName("send_otp")
        self.confirm_otp = QtWidgets.QPushButton(forgotpassword)
        self.confirm_otp.setEnabled(False)
        self.confirm_otp.setGeometry(QtCore.QRect(310, 140, 71, 40))
        self.confirm_otp.setStyleSheet("#confirm_otp{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 12px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#confirm_otp:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#confirm_otp:pressed{\n"
"background-color:#1A237E;\n"
"}\n"
"#confirm_otp:disabled{\n"
"background-color:#bbdefb;\n"
"color: #eeffff;\n"
"}\n"
"")
        self.confirm_otp.setObjectName("confirm_otp")
        self.password = QtWidgets.QLineEdit(forgotpassword)
        self.password.setEnabled(False)
        self.password.setGeometry(QtCore.QRect(40, 230, 321, 41))
        self.password.setStyleSheet("#password{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#password:hover {\n"
"    border-style: inset;\n"
"}\n"
"#password:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}\n"
"#password:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.confirm_password = QtWidgets.QLineEdit(forgotpassword)
        self.confirm_password.setEnabled(False)
        self.confirm_password.setGeometry(QtCore.QRect(40, 300, 321, 40))
        self.confirm_password.setStyleSheet("#confirm_password{\n"
"background-color: white;\n"
"border-color: #64B5F6;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"font: 57 10pt \"Slate For OnePlus\";\n"
"padding: 6px;\n"
"padding-left: 15px;\n"
"}\n"
"#confirm_password:hover {\n"
"    border-style: inset;\n"
"}\n"
"#confirm_password:focus {\n"
"    background-color: #E3F2FD;\n"
"    border-style: inset;\n"
"}\n"
"#confirm_password:disabled {\n"
"    background-color: #e0f2f1;\n"
"    border-style: inset;\n"
"}")
        self.confirm_password.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_password.setObjectName("confirm_password")
        self.line = QtWidgets.QFrame(forgotpassword)
        self.line.setGeometry(QtCore.QRect(40, 200, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.confirm_button = QtWidgets.QPushButton(forgotpassword)
        self.confirm_button.setEnabled(False)
        self.confirm_button.setGeometry(QtCore.QRect(170, 360, 93, 40))
        self.confirm_button.setStyleSheet("#confirm_button{\n"
"    font: 57 8pt \"Slate For OnePlus Medium\";\n"
"background-color:#0277BD;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 12px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#confirm_button:hover{\n"
"background-color:#01579B;\n"
"\n"
"}\n"
"#confirm_button:pressed{\n"
"background-color:#1A237E;\n"
"}\n"
"#confirm_button:disabled{\n"
"background-color:#bbdefb;\n"
"color: #eeffff;\n"
"}\n"
"")
        self.confirm_button.setObjectName("confirm_button")
        self.close_button = QtWidgets.QPushButton(forgotpassword)
        self.close_button.setGeometry(QtCore.QRect(290, 400, 93, 40))
        self.close_button.setStyleSheet("#close_button{\n"
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
"#close_button:hover{\n"
"background-color:#01579B;\n"
"    font: 87 8pt \"Roboto Black\";\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"border-radius: 5px;\n"
"}\n"
"#close_button:pressed{\n"
"background-color:#1A237E;\n"
"}")
        self.close_button.setObjectName("close_button")
        self.label_0 = QtWidgets.QLabel(forgotpassword)
        self.label_0.setGeometry(QtCore.QRect(40, 85, 71, 31))
        self.label_0.setStyleSheet("font: 8pt \"Slate For OnePlus\";")
        self.label_0.setTextFormat(QtCore.Qt.AutoText)
        self.label_0.setScaledContents(False)
        self.label_0.setWordWrap(True)
        self.label_0.setObjectName("label_0")
        self.label_3 = QtWidgets.QLabel(forgotpassword)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 401, 41))
        self.label_3.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color: transparent")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(forgotpassword)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 71))
        self.label.setStyleSheet("font: 57 22pt \"Slate For OnePlus Medium\";\n"
"color: #ffffff;\n"
"background-color:#01579B;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(forgotpassword)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 401, 431))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: inset;\n"
"border-color: white;\n"
"border-radius: 10px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.email_input.raise_()
        self.enter_otp.raise_()
        self.send_otp.raise_()
        self.confirm_otp.raise_()
        self.password.raise_()
        self.confirm_password.raise_()
        self.line.raise_()
        self.confirm_button.raise_()
        self.close_button.raise_()
        self.label_0.raise_()
        self.label_3.raise_()
        self.send_otp.clicked.connect(lambda: self.sendOTP(forgotpassword))
        self.confirm_otp.clicked.connect(lambda: self.confirmOTP(forgotpassword))
        self.confirm_button.clicked.connect(lambda: self.confirmPassword(forgotpassword))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(forgotpassword)
        self.close_button.clicked.connect(forgotpassword.close)
        QtCore.QMetaObject.connectSlotsByName(forgotpassword)
    def sendOTP(self, forgotpassword):
        import db
        import random
        ch=db.adminLogin(self.email_input.text(), 'test')
        if(ch!=True and ch!=False):
            QtWidgets.QMessageBox.about(forgotpassword, "E-Mail not Found", "Please enter a valid E-Mail Address!" )
        else:
            self.email_input.setEnabled(False)
            self.send_otp.setEnabled(False)
            global a
            a=random.randint(100000,999999)
            sendEmail(self.email_input.text(),a)
            QtWidgets.QMessageBox.about(forgotpassword, "OTP Sent!","An OTP has been sent to your E-Mail, please enter the OTP sent" )
            self.confirm_otp.setEnabled(True)
            self.enter_otp.setEnabled(True)
    def confirmOTP(self, forgotpassword):
        if(self.enter_otp.text()==str(a)):
            QtWidgets.QMessageBox.about(forgotpassword, "OTP Correct!","The OTP is correct! You may change your password now." )
            self.confirm_otp.setEnabled(False)
            self.enter_otp.setEnabled(False)
            self.password.setEnabled(True)
            self.confirm_password.setEnabled(True)
            self.confirm_button.setEnabled(True)
        else:
            QtWidgets.QMessageBox.about(forgotpassword, "OTP incorrect!","The OTP is incorrect! Please check your E-Mail." )
    def confirmPassword(self, forgotpassword):
        if(self.password.text()==self.confirm_password.text()):
            import db
            db.changePasswordAdmin(self.email_input.text(), self.password.text())
            QtWidgets.QMessageBox.about(forgotpassword, "Password Changed!","Your password has been changed successfully!" )
        else:
            QtWidgets.QMessageBox.about(forgotpassword, "Error!","Passwords don't match!" )

    def retranslateUi(self, forgotpassword):
        _translate = QtCore.QCoreApplication.translate
        forgotpassword.setWindowTitle(_translate("forgotpassword", "Forgot Password"))
        self.email_input.setPlaceholderText(_translate("forgotpassword", "Official E-Mail ID"))
        self.enter_otp.setPlaceholderText(_translate("forgotpassword", "Enter OTP"))
        self.send_otp.setText(_translate("forgotpassword", "Send OTP"))
        self.confirm_otp.setText(_translate("forgotpassword", "Confirm"))
        self.password.setPlaceholderText(_translate("forgotpassword", "Enter new Password"))
        self.confirm_password.setPlaceholderText(_translate("forgotpassword", "Confirm new Password"))
        self.confirm_button.setText(_translate("forgotpassword", "CONFIRM"))
        self.confirm_button.setShortcut(_translate("forgotpassword", "Return"))
        self.close_button.setText(_translate("forgotpassword", "Close"))
        self.close_button.setShortcut(_translate("forgotpassword", "Esc"))
        self.label_0.setText(_translate("forgotpassword", "Official   E-Mail:"))
        self.label_3.setText(_translate("forgotpassword", "Change Password"))

def sendEmail(eMail, OTP):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fromaddr = "EMAIL_ADDRESS_HERE"
    toaddr = eMail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "OTP for Resetting your password!"
    body = "Dear User, \n\n"+"You had recently requested to change your password/reset your password.\n"+ "\nThe OTP is: "+ str(OTP)+ "\nYou can now enter the OTP and change the password."+ "\nThank You." 
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD_HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    forgotpassword = QtWidgets.QWidget()
    ui = Ui_forgotpassword()
    ui.setupUi(forgotpassword)
    forgotpassword.show()
    sys.exit(app.exec_())

