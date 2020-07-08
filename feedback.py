# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_feedback(object):
    def setupUi(self, feedback):
        feedback.setObjectName("feedback")
        feedback.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(feedback.sizePolicy().hasHeightForWidth())
        feedback.setSizePolicy(sizePolicy)
        feedback.setMinimumSize(QtCore.QSize(400, 300))
        feedback.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICLog icons/ICLog_png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        feedback.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(feedback)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 61))
        self.label.setStyleSheet("background-color:#01579B;\n"
"font: 22pt \"Slate For OnePlus Bk\";\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(feedback)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 401, 311))
        self.label_2.setStyleSheet("background-color: white;\n"
"border-color: white;\n"
"border-style: inset;\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(feedback)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 400, 16))
        self.label_3.setStyleSheet("font: 8pt \"Slate For OnePlus\";")
        self.label_3.setObjectName("label_3")
        self.feedbackText = QtWidgets.QTextEdit(feedback)
        self.feedbackText.setGeometry(QtCore.QRect(10, 110, 381, 121))
        self.feedbackText.setObjectName("feedbackText")
        self.confirmButton = QtWidgets.QPushButton(feedback)
        self.confirmButton.setGeometry(QtCore.QRect(252, 250, 71, 41))
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
        self.cancelButton = QtWidgets.QPushButton(feedback)
        self.cancelButton.setGeometry(QtCore.QRect(322, 250, 71, 41))
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
        self.cancelButton.clicked.connect(feedback.close)
        self.retranslateUi(feedback)
        self.confirmButton.clicked.connect(lambda: self.sendFeedback(feedback))
        QtCore.QMetaObject.connectSlotsByName(feedback)

    def retranslateUi(self, feedback):
        _translate = QtCore.QCoreApplication.translate
        feedback.setWindowTitle(_translate("feedback", "Feedback - ICLog"))
        self.label.setText(_translate("feedback", "Feedback"))
        self.label_3.setText(_translate("feedback", "Please feel free to write a feedback as an anonymous. :)"))
        self.feedbackText.setPlaceholderText(_translate("feedback", "Feedback Please..."))
        self.confirmButton.setText(_translate("feedback", "SEND"))
        self.cancelButton.setText(_translate("feedback", "CLOSE"))
        self.cancelButton.setShortcut(_translate("feedback", "Esc"))
    def sendFeedback(self, feedback):
        try:
            mytext = self.feedbackText.toPlainText()
            sendEmail(mytext)
            QtWidgets.QMessageBox.about(feedback, "Feedback", "Thank You!\nYour feedback has been recieved.\nFeedback submitted for ICLog v2.1.8." )
            feedback.close()
        except:
            QtWidgets.QMessageBox.about(feedback, "Feedback", "We are facing some technical issues. Please try again later." )
            

def sendEmail(fb):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fromaddr = "EMAIL_ID"
    toaddr = "EMAIL_ID"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Feedback"
    body = "Feedback:\n"+fb
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    feedback = QtWidgets.QWidget()
    ui = Ui_feedback()
    ui.setupUi(feedback)
    feedback.show()
    sys.exit(app.exec_())

