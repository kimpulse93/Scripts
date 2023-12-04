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
        self.infoFr.clicked.connect(self.infoFR)
        self.info2d = QtWidgets.QPushButton(self.centralwidget)
        self.info2d.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.info2d.setObjectName("info2d")
        self.info2d.clicked.connect(self.info2D)
        self.annulBon = QtWidgets.QPushButton(self.centralwidget)
        self.annulBon.setGeometry(QtCore.QRect(190, 70, 141, 41))
        self.annulBon.setObjectName("annulBoN")
        self.annulBon.clicked.connect(self.annulBoN)
        self.teach2d = QtWidgets.QPushButton(self.centralwidget)
        self.teach2d.setGeometry(QtCore.QRect(10, 120, 141, 21))
        self.teach2d.setStyleSheet("alternate-background-color: rgb(255, 170, 255);")
        self.teach2d.setObjectName("teach2d")
        self.teach2d.clicked.connect(self.teach2D)
        self.shtrihconsole = QtWidgets.QPushButton(self.centralwidget)
        self.shtrihconsole.setGeometry(QtCore.QRect(190, 120, 141, 41))
        self.shtrihconsole.setObjectName("shtrihconsole")
        self.shtrihconsole.clicked.connect(self.shtrihconsolE)
        self.FW2d = QtWidgets.QPushButton(self.centralwidget)
        self.FW2d.setGeometry(QtCore.QRect(10, 80, 141, 21))
        self.FW2d.setObjectName("FW2d")
        self.FW2d.clicked.connect(self.FW2D)
        self.FWscale = QtWidgets.QPushButton(self.centralwidget)
        self.FWscale.setGeometry(QtCore.QRect(10, 200, 141, 21))
        self.FWscale.setObjectName("FWscale")
        self.FWscale.clicked.connect(self.FWscalE)
        self.scalelearn = QtWidgets.QPushButton(self.centralwidget)
        self.scalelearn.setGeometry(QtCore.QRect(10, 240, 141, 21))
        self.scalelearn.setStyleSheet("")
        self.scalelearn.setObjectName("scalelearn")
        self.scalelearn.clicked.connect(self.scalelearN)
        self.scaleinfo = QtWidgets.QPushButton(self.centralwidget)
        self.scaleinfo.setGeometry(QtCore.QRect(10, 160, 141, 21))
        self.scaleinfo.setObjectName("scaleinfo")
        self.scaleinfo.clicked.connect(self.scaleinfO)
        self.consoleAtol = QtWidgets.QPushButton(self.centralwidget)
        self.consoleAtol.setGeometry(QtCore.QRect(190, 170, 141, 41))
        self.consoleAtol.setObjectName("consoleAtol")
        self.consoleAtol.clicked.connect(self.consoleAtoL)
        self.fwKB = QtWidgets.QPushButton(self.centralwidget)
        self.fwKB.setGeometry(QtCore.QRect(190, 380, 141, 31))
        self.fwKB.setObjectName("fwKB")
        self.fwKB.clicked.connect(self.fWKB)
        self.drop = QtWidgets.QPushButton(self.centralwidget)
        self.drop.setGeometry(QtCore.QRect(190, 310, 141, 21))
        self.drop.setObjectName("drop")
        self.drop.clicked.connect(self.droP)
        self.clearBD = QtWidgets.QPushButton(self.centralwidget)
        self.clearBD.setGeometry(QtCore.QRect(190, 490, 141, 21))
        self.clearBD.setObjectName("clearBD")
        self.clearBD.clicked.connect(self.cleaRBD)
        self.modelPos = QtWidgets.QPushButton(self.centralwidget)
        self.modelPos.setGeometry(QtCore.QRect(190, 250, 141, 21))
        self.modelPos.setObjectName("modelPos")
        self.modelPos.clicked.connect(self.modelPoS)
        self.enableVNC = QtWidgets.QPushButton(self.centralwidget)
        self.enableVNC.setGeometry(QtCore.QRect(190, 280, 141, 21))
        self.enableVNC.setObjectName("enableVNC")
        self.enableVNC.clicked.connect(self.enablEVNC)
        self.delGKBOn = QtWidgets.QPushButton(self.centralwidget)
        self.delGKBOn.setGeometry(QtCore.QRect(190, 420, 141, 31))
        self.delGKBOn.setObjectName("delGKBOn")
        self.delGKBOn.clicked.connect(self.delGKBON)
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
        text = r"cat / var / log / FR / info_FR_human"
        pyperclip.copy(text)

    def info2D(self):
        text = r"cat /var/log/info_HandScan"
        pyperclip.copy(text)

    def annulBoN(self):
        text = r"rm /usr/local/gkretail/pos/gk_bon"
        pyperclip.copy(text)
    def teach2D(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/scanners_update_firmware/process.sh -c"
        pyperclip.copy(text)

    def shtrihconsolE(self):
        text = r"/opt/shtrih/Console_util/test_shtrih.sh"
        pyperclip.copy(text)

    def FW2D(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/scanners_update_firmware/process.sh -f"
        pyperclip.copy(text)

    def FWscalE(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/ScannerScale_Updater/ScannerScale_updater.sh -f"
        pyperclip.copy(text)
    def scalelearN(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/ScannerScale_Updater/ScannerScale_updater.sh -c"
        pyperclip.copy(text)
    def scaleinfO(self):
        text = r"cat /var/log/info_ScaleScanner"
        pyperclip.copy(text)

    def consoleAtoL(self):
        text = r"/opt/atol/Console_util/test_atol.sh"
        pyperclip.copy(text)

    def fWKB(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/NCR_keyboard/bin/kbupdate.sh"
        pyperclip.copy(text)

    def droP(self):
        text = r"cat /var/log/messages | grep -ia -A 10 \"USB disconnect\" | grep -a Manufacturer:| grep -av \"cat /var/log/messages\"|awk '{print$1,$2,$3,$4,$10,$11,$12,$13}'"
        pyperclip.copy(text)

    def cleaRBD(self):
        text = r"cd /usr/local/gkretail/pos/data;if ! [ -d ./old ]; then sudo mkdir old; fi;sudo mv standard_beleg.gdb ./old; sudo mv standard_stamm* ./old; sudo rm -rf temp_standard_stamm.gdb.zip*; cd ./empty; sudo cp -p standard_beleg.gdb ../; sudo cp -p standard_stamm.gdb ../"
        pyperclip.copy(text)

    def modelPoS(self):
        text = r" echo -e '\n\nМодель кассы: ' $(sudo dmidecode -t1 | grep -E 'Manufacturer|Product' | cut -d: -f 2; )' SN: ' $(sudo dmidecode -t1 | grep Serial | cut -d: -f 2)'\n'	'Последняя перезагрузка: ' $(uptime --since)'\n''Дата установки системы: '$(ls --time-style=long-iso -clt / | tail -n1 | awk '{print $7, $6}' 2>/dev/null)'\n''Дата обновления GK: ' $(ls -lt  --time-style='+%Y-%m-%d %H:%M' /usr/local/apr_utils/|grep root|head -1|awk '{print$6,$7}')'\n''Версия GK: '$(sudo unzip -c /usr/local/gkretail/pos/lib/com.gk-software.xrg.pos/pos-release-info.jar release.info | grep version.complete= | cut -d= -f 2)'\n'$(df -h | grep sda | awk '{print\"Занято места на диске: \" $5}')'\n'	'Количество ядер, потоков: '$(cat /proc/cpuinfo|grep processor|wc -l)'\n''Неотправленные чеки в ОФД: '$(cat /var/log/FR/info_FR_human | grep 'неотправленных' | cut -d- -f 2)'\n''Модель ФР: ' $(fr0=$(cat /var/log/FR/info_FR_human 2>/dev/null| grep 'Модель ФР:' | cut -d- -f2,3,4); if [ -z $fr0 ]; then fr=$(lsusb |grep -oE \"4ee4|0005\"); if [ $fr == 0005 ]; then echo Атол; elif [ $fr == 4ee4 ]; then echo Ритейл 01Ф\\Штрих; fi  2>/dev/null; else echo $fr0; fi)'\n''2D сканер: ' $(cat /var/log/info_HandScan|head -4 2>/dev/null)'\n''Весы: ' $(cat /var/log/info_ScaleScanner|head -4 2>/dev/null)'\n''Стационарный сканер: ' $(cat /var/log/info_Scanner|head -4 2>/dev/null)'\n';echo -e 'Состояние HDD - SSD\n\t'$(smartctl -i /dev/sda |grep \"User\"|awk '{print \"Объем: \" $5$6}'|tr -d '[|]';echo '\n\tДней в работе: ' $(($( smartctl -A /dev/sda | grep Power_On_Hours | awk '{print$10}')/24));echo '\n\tТемпература :' $( smartctl -A /dev/sda | grep '194 Temperature_Celsius'| awk '{print$10}');smart=$( smartctl -d ata -H /dev/sda | grep result | awk -F ':' '{print$2}');if [[ \"$smart\" == \" PASSED\" ]]; then echo \"\n\tСостояние: Диск в порядке\"; else echo \"Состояние: $smart\"; fi; echo;echo '\n\tМодель:' $(smartctl -i /dev/sda | grep -E 'Device Model|Serial Number'| awk -F ':' '{print$2}');ssd_life=$(smartctl -A /dev/sda | grep -E 'SSD_Life_Left' | awk '{print$2,$10}');if [[ -n \"$ssd_life\" ]]; then echo '\n\tSSD остаток жизни:' $(echo $ssd_life | awk '{print$2\"%\"}' ); fi;ssd_lifetime=$(smartctl -A /dev/sda | grep Remaining_Lifetime| awk '{print$2,$10}');if [[ -n \"$ssd_lifetime\" ]]; then echo '\n\tSSD остаток жизни:' $(echo $ssd_lifetime | awk '{print$2\"%\"}' ); fi;echo '\n\t'$(smartctl -A /dev/sda | grep -E 'Reallocated_Sector_Ct' | awk '{print$2,$10}');echo '\n\t'$(smartctl -A /dev/sda |grep 'Current_Pending_Sector' | awk '{print$2,$10}');echo '\n\t'$(smartctl -A /dev/sda |grep 'Offline_Uncorrectable' | awk '{print$2,$10}'));echo;echo 'Перезагрузки: ';last -x reboot|head -4"
        pyperclip.copy(text)

    def enablEVNC(self):
        text = r"sudo sed -i 's/-viewonly/ /g'  /lib/systemd/system/x11vnc.service; sudo systemctl daemon-reload; sudo systemctl restart x11vnc"
        pyperclip.copy(text)

    def delGKBON(self):
        text = r"rm /usr/local/gkretail/pos/gk_bon"
        pyperclip.copy(text)



    def scaleinfO(self):
        text = r"cat /var/log/info_ScaleScanner"
        pyperclip.copy(text)

    def consoleAtoL(self):
        text = r"/opt/atol/Console_util/test_atol.sh"
        pyperclip.copy(text)

    def fWKB(self):
        text = r"rcgk stop; sudo /usr/local/X5_scripts/NCR_keyboard/bin/kbupdate.sh"
        pyperclip.copy(text)

    def droP(self):
        text = r"cat /var/log/messages | grep -ia -A 10 \"USB disconnect\" | grep -a Manufacturer:| grep -av \"cat /var/log/messages\"|awk '{print$1,$2,$3,$4,$10,$11,$12,$13}'"
        pyperclip.copy(text)

    def cleaRBD(self):
        text = r"cd /usr/local/gkretail/pos/data;if ! [ -d ./old ]; then sudo mkdir old; fi;sudo mv standard_beleg.gdb ./old; sudo mv standard_stamm* ./old; sudo rm -rf temp_standard_stamm.gdb.zip*; cd ./empty; sudo cp -p standard_beleg.gdb ../; sudo cp -p standard_stamm.gdb ../"
        pyperclip.copy(text)

    def modelPoS(self):
        text = r" echo -e '\n\nМодель кассы: ' $(sudo dmidecode -t1 | grep -E 'Manufacturer|Product' | cut -d: -f 2; )' SN: ' $(sudo dmidecode -t1 | grep Serial | cut -d: -f 2)'\n'	'Последняя перезагрузка: ' $(uptime --since)'\n''Дата установки системы: '$(ls --time-style=long-iso -clt / | tail -n1 | awk '{print $7, $6}' 2>/dev/null)'\n''Дата обновления GK: ' $(ls -lt  --time-style='+%Y-%m-%d %H:%M' /usr/local/apr_utils/|grep root|head -1|awk '{print$6,$7}')'\n''Версия GK: '$(sudo unzip -c /usr/local/gkretail/pos/lib/com.gk-software.xrg.pos/pos-release-info.jar release.info | grep version.complete= | cut -d= -f 2)'\n'$(df -h | grep sda | awk '{print\"Занято места на диске: \" $5}')'\n'	'Количество ядер, потоков: '$(cat /proc/cpuinfo|grep processor|wc -l)'\n''Неотправленные чеки в ОФД: '$(cat /var/log/FR/info_FR_human | grep 'неотправленных' | cut -d- -f 2)'\n''Модель ФР: ' $(fr0=$(cat /var/log/FR/info_FR_human 2>/dev/null| grep 'Модель ФР:' | cut -d- -f2,3,4); if [ -z $fr0 ]; then fr=$(lsusb |grep -oE \"4ee4|0005\"); if [ $fr == 0005 ]; then echo Атол; elif [ $fr == 4ee4 ]; then echo Ритейл 01Ф\\Штрих; fi  2>/dev/null; else echo $fr0; fi)'\n''2D сканер: ' $(cat /var/log/info_HandScan|head -4 2>/dev/null)'\n''Весы: ' $(cat /var/log/info_ScaleScanner|head -4 2>/dev/null)'\n''Стационарный сканер: ' $(cat /var/log/info_Scanner|head -4 2>/dev/null)'\n';echo -e 'Состояние HDD - SSD\n\t'$(smartctl -i /dev/sda |grep \"User\"|awk '{print \"Объем: \" $5$6}'|tr -d '[|]';echo '\n\tДней в работе: ' $(($( smartctl -A /dev/sda | grep Power_On_Hours | awk '{print$10}')/24));echo '\n\tТемпература :' $( smartctl -A /dev/sda | grep '194 Temperature_Celsius'| awk '{print$10}');smart=$( smartctl -d ata -H /dev/sda | grep result | awk -F ':' '{print$2}');if [[ \"$smart\" == \" PASSED\" ]]; then echo \"\n\tСостояние: Диск в порядке\"; else echo \"Состояние: $smart\"; fi; echo;echo '\n\tМодель:' $(smartctl -i /dev/sda | grep -E 'Device Model|Serial Number'| awk -F ':' '{print$2}');ssd_life=$(smartctl -A /dev/sda | grep -E 'SSD_Life_Left' | awk '{print$2,$10}');if [[ -n \"$ssd_life\" ]]; then echo '\n\tSSD остаток жизни:' $(echo $ssd_life | awk '{print$2\"%\"}' ); fi;ssd_lifetime=$(smartctl -A /dev/sda | grep Remaining_Lifetime| awk '{print$2,$10}');if [[ -n \"$ssd_lifetime\" ]]; then echo '\n\tSSD остаток жизни:' $(echo $ssd_lifetime | awk '{print$2\"%\"}' ); fi;echo '\n\t'$(smartctl -A /dev/sda | grep -E 'Reallocated_Sector_Ct' | awk '{print$2,$10}');echo '\n\t'$(smartctl -A /dev/sda |grep 'Current_Pending_Sector' | awk '{print$2,$10}');echo '\n\t'$(smartctl -A /dev/sda |grep 'Offline_Uncorrectable' | awk '{print$2,$10}'));echo;echo 'Перезагрузки: ';last -x reboot|head -4"
        pyperclip.copy(text)

    def enablEVNC(self):
        text = r"sudo sed -i 's/-viewonly/ /g'  /lib/systemd/system/x11vnc.service; sudo systemctl daemon-reload; sudo systemctl restart x11vnc"
        pyperclip.copy(text)

    def delGKBON(self):
        text = r"rm /usr/local/gkretail/pos/gk_bon"
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
