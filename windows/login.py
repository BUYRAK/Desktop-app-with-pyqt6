# Form implementation generated from reading ui file 'designs/login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import data.models as model


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(280, 336)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.email_line = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line.setGeometry(QtCore.QRect(40, 110, 200, 25))
        self.email_line.setMaximumSize(QtCore.QSize(200, 25))
        self.email_line.setInputMask("")
        self.email_line.setText("")
        self.email_line.setFrame(False)
        self.email_line.setObjectName("email_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(40, 170, 200, 25))
        self.password_line.setMaximumSize(QtCore.QSize(200, 25))
        self.password_line.setFrame(False)
        self.password_line.setObjectName("password_line")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(40, 220, 200, 41))
        self.login_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.login_button.setObjectName("login_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 60, 16))
        self.label_3.setObjectName("label_3")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.login_button.clicked.connect(self.login_op)



    def login_op(self):
        model.is_authenticated(str(self.email_line.text()), str(self.password_line.text))


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Ciao!"))
        self.login_button.setText(_translate("LoginWindow", "Login"))
        self.label_2.setText(_translate("LoginWindow", "Email"))
        self.label_3.setText(_translate("LoginWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
