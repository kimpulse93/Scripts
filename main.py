import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyperclip


class Scripts (QMainWindow):
    def __init__(self):
        super(Scripts, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 645)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 10, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.infoFr = QtWidgets.QPushButton(self.centralwidget)
        self.infoFr.setGeometry(QtCore.QRect(190, 40, 141, 21))
        self.infoFr.setObjectName("infoFr")
        self.info2d = QtWidgets.QPushButton(self.centralwidget)
        self.info2d.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.info2d.setObjectName("info2d")
        self.annulBon = QtWidgets.QPushButton(self.centralwidget)
        self.annulBon.setGeometry(QtCore.QRect(190, 70, 141, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.annulBon.setFont(font)
        self.annulBon.setAutoRepeat(False)
        self.annulBon.setAutoRepeatDelay(8)
        self.annulBon.setAutoRepeatInterval(100)
        self.annulBon.setObjectName("annulBon")
        self.teach2d = QtWidgets.QPushButton(self.centralwidget)
        self.teach2d.setGeometry(QtCore.QRect(10, 120, 141, 21))
        self.teach2d.setStyleSheet("alternate-background-color: rgb(255, 170, 255);")
        self.teach2d.setObjectName("teach2d")
        self.shtrihconsole = QtWidgets.QPushButton(self.centralwidget)
        self.shtrihconsole.setGeometry(QtCore.QRect(190, 120, 141, 41))
        self.shtrihconsole.setObjectName("shtrihconsole")
        self.FW2d = QtWidgets.QPushButton(self.centralwidget)
        self.FW2d.setGeometry(QtCore.QRect(10, 80, 141, 21))
        self.FW2d.setObjectName("FW2d")
        self.FWscale = QtWidgets.QPushButton(self.centralwidget)
        self.FWscale.setGeometry(QtCore.QRect(10, 200, 141, 21))
        self.FWscale.setObjectName("FWscale")
        self.scalelearn = QtWidgets.QPushButton(self.centralwidget)
        self.scalelearn.setGeometry(QtCore.QRect(10, 240, 141, 21))
        self.scalelearn.setStyleSheet("")
        self.scalelearn.setObjectName("scalelearn")
        self.scaleinfo = QtWidgets.QPushButton(self.centralwidget)
        self.scaleinfo.setGeometry(QtCore.QRect(10, 160, 141, 21))
        self.scaleinfo.setObjectName("scaleinfo")
        self.consoleAtol = QtWidgets.QPushButton(self.centralwidget)
        self.consoleAtol.setGeometry(QtCore.QRect(190, 170, 141, 41))
        self.consoleAtol.setObjectName("consoleAtol")
        self.fwKB = QtWidgets.QPushButton(self.centralwidget)
        self.fwKB.setGeometry(QtCore.QRect(190, 380, 141, 31))
        self.fwKB.setObjectName("fwKB")
        self.drop = QtWidgets.QPushButton(self.centralwidget)
        self.drop.setGeometry(QtCore.QRect(190, 310, 141, 21))
        self.drop.setObjectName("drop")
        self.clearBD = QtWidgets.QPushButton(self.centralwidget)
        self.clearBD.setGeometry(QtCore.QRect(190, 490, 141, 21))
        self.clearBD.setObjectName("clearBD")
        self.modelPos = QtWidgets.QPushButton(self.centralwidget)
        self.modelPos.setGeometry(QtCore.QRect(190, 250, 141, 21))
        self.modelPos.setObjectName("modelPos")
        self.enableVNC = QtWidgets.QPushButton(self.centralwidget)
        self.enableVNC.setGeometry(QtCore.QRect(190, 280, 141, 21))
        self.enableVNC.setObjectName("enableVNC")
        self.delGKBOn = QtWidgets.QPushButton(self.centralwidget)
        self.delGKBOn.setGeometry(QtCore.QRect(190, 420, 141, 31))
        self.delGKBOn.setObjectName("delGKBOn")
        self.delBridge = QtWidgets.QPushButton(self.centralwidget)
        self.delBridge.setGeometry(QtCore.QRect(190, 460, 141, 21))
        self.delBridge.setStyleSheet("")
        self.delBridge.setObjectName("delBridge")
        self.DTSize = QtWidgets.QPushButton(self.centralwidget)
        self.DTSize.setGeometry(QtCore.QRect(190, 550, 141, 41))
        self.DTSize.setObjectName("DTSize")
        self.sizeBD = QtWidgets.QPushButton(self.centralwidget)
        self.sizeBD.setGeometry(QtCore.QRect(190, 520, 141, 21))
        self.sizeBD.setObjectName("sizeBD")
        self.logMistakes = QtWidgets.QPushButton(self.centralwidget)
        self.logMistakes.setGeometry(QtCore.QRect(190, 340, 141, 31))
        self.logMistakes.setObjectName("logMistakes")
        self.offHP = QtWidgets.QPushButton(self.centralwidget)
        self.offHP.setGeometry(QtCore.QRect(10, 380, 141, 21))
        self.offHP.setObjectName("offHP")
        self.offNCR = QtWidgets.QPushButton(self.centralwidget)
        self.offNCR.setGeometry(QtCore.QRect(10, 300, 141, 21))
        self.offNCR.setStyleSheet("gridline-color: rgb(255, 170, 255);")
        self.offNCR.setObjectName("offNCR")
        self.onNCR = QtWidgets.QPushButton(self.centralwidget)
        self.onNCR.setGeometry(QtCore.QRect(10, 340, 141, 21))
        self.onNCR.setObjectName("onNCR")
        self.onHP = QtWidgets.QPushButton(self.centralwidget)
        self.onHP.setGeometry(QtCore.QRect(10, 420, 141, 21))
        self.onHP.setObjectName("onHP")
        self.passTR = QtWidgets.QPushButton(self.centralwidget)
        self.passTR.setGeometry(QtCore.QRect(10, 540, 141, 21))
        self.passTR.setObjectName("passTR")
        self.passWK = QtWidgets.QPushButton(self.centralwidget)
        self.passWK.setGeometry(QtCore.QRect(10, 480, 141, 21))
        self.passWK.setObjectName("passWK")
        self.passPOS = QtWidgets.QPushButton(self.centralwidget)
        self.passPOS.setGeometry(QtCore.QRect(10, 510, 141, 21))
        self.passPOS.setObjectName("passPOS")
        self.passIPcam = QtWidgets.QPushButton(self.centralwidget)
        self.passIPcam.setGeometry(QtCore.QRect(10, 570, 141, 21))
        self.passIPcam.setObjectName("passIPcam")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def infoFR(self):
        text =  r"cat / var / log / FR / info_FR_human"
        pyperclip.copy(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Сканеры/Весы"))
        self.label_3.setText(_translate("MainWindow", "    ФР"))
        self.infoFr.setText(_translate("MainWindow", "Инфо о ФР"))
        self.info2d.setText(_translate("MainWindow", "2d Info"))
        self.annulBon.setText(_translate("MainWindow", "Аннулция чеков\n"
" за сегодняшний день"))
        self.teach2d.setText(_translate("MainWindow", "2d Обучить"))
        self.shtrihconsole.setText(_translate("MainWindow", "Консоль управления\n"
"ФР Штрих/Ритейл"))
        self.FW2d.setText(_translate("MainWindow", "2d Прошить"))
        self.FWscale.setText(_translate("MainWindow", "Весы Прошить"))
        self.scalelearn.setText(_translate("MainWindow", "Весы Обучить"))
        self.scaleinfo.setText(_translate("MainWindow", "Весы Info"))
        self.consoleAtol.setText(_translate("MainWindow", "Консоль управления\n"
"ФР Атол"))
        self.fwKB.setText(_translate("MainWindow", "Прошивка клавиатуры"))
        self.drop.setText(_translate("MainWindow", "Отвалы"))
        self.clearBD.setText(_translate("MainWindow", "Очистка БД"))
        self.modelPos.setText(_translate("MainWindow", "Модель Кассы"))
        self.enableVNC.setText(_translate("MainWindow", "Включить VNC"))
        self.delGKBOn.setText(_translate("MainWindow", "Удалить gk_bon"))
        self.delBridge.setText(_translate("MainWindow", "Удалить BridgeLock"))
        self.DTSize.setText(_translate("MainWindow", "Разрешение 800x600\n"
"на кассе"))
        self.sizeBD.setText(_translate("MainWindow", "Размер БД"))
        self.logMistakes.setText(_translate("MainWindow", "Логи ошибок GK"))
        self.offHP.setText(_translate("MainWindow", "OFF DEBOLD/HP"))
        self.offNCR.setText(_translate("MainWindow", "OFF NCR/IBM"))
        self.onNCR.setText(_translate("MainWindow", "ON NCR/IBM"))
        self.onHP.setText(_translate("MainWindow", "ON DEBOLD/HP"))
        self.passTR.setText(_translate("MainWindow", "Трассир"))
        self.passWK.setText(_translate("MainWindow", "ТК/Сервер"))
        self.passPOS.setText(_translate("MainWindow", "Касса"))
        self.passIPcam.setText(_translate("MainWindow", "IP Камера"))
        self.label.setText(_translate("MainWindow", "  Общие"))
        self.label_4.setText(_translate("MainWindow", "Питание USB"))
        self.label_5.setText(_translate("MainWindow", "Пароли VNC"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Scripts()
    window.show()

    sys.exit(app.exec())
