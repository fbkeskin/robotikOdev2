#komut satırı
import sys
#ihtiyacımız olan libler
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
#pencere ikonu
from PyQt5.QtGui import QIcon, QFont


#QMainwindow'dan turetilen class
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Giriş Ekranı")
        #login penceresinin ekranı ortalayarak acılması
        self.setGeometry(700,300,500,300)
        #ikonun eklenmesi
        self.setWindowIcon(QIcon("user.png"))

        #initUI cagırlır
        self.initUI()

    def initUI(self):
        #kullanıcı bilgisi text
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(70,50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(70, 90)

        self.lbl_password =QtWidgets.QLabel(self)
        self.lbl_password.setText("Şifre: ")
        self.lbl_password.move(70, 130)

        #giris bilgisi yazdırma
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(200,40)
        self.lbl_result.move(70,220)
        self.lbl_result.setStyleSheet("background-color: white; border: 1px solid black; padding: 5px;")
        self.lbl_result.setAlignment(QtCore.Qt.AlignCenter)

        #kullanıcı text kutusu
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 50)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150, 90)

        self.txt_password = QtWidgets.QLineEdit(self)
        self.txt_password.move(150, 130)

        #onay islemi
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Giriş")
        self.btn_save.move(150, 170)
        self.btn_save.clicked.connect(self.login)

    def login(self):
        name = self.txt_name.text()
        surname = self.txt_surname.text()
        password = self.txt_password.text()

        if (name == "betul" and surname == "keskin" and password == "123"):
            self.lbl_result.setText("Hoş Geldin " + self.txt_name.text() + " " + self.txt_surname.text())
        else:
            self.lbl_result.setText("Hatalı giris")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    #uygulama calıstırılacak
    win.show()

    #uygulama son bulacak (carpı ikonuna tıkladıgımda)
    sys.exit(app.exec_())

window()
