import sys
import datetime
from PyQt6 import uic, QtCore, QtGui, QtWidgets
import requests
from requests.exceptions import HTTPError
import json


class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "http://127.0.0.1:5000"
    MessageID = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('Client_QT.ui', self)
        self.pushButton1.clicked.connect(self.pushButton1_clicked)

    def pushButton1_clicked(self):
        self.SendMessage()

    def SendMessage(self):
        UserName = self.lineEdit_1.text()
        MessageText = self.lineEdit_2.text()
        TimeStamp = str(datetime.datetime.today())
        msg = f"{{\"UserName\": \"{UserName}\", \"MessageText\": \"{MessageText}\", \"TimeStamp\": \"{TimeStamp}\""

        print('Message send:' + msg)
        url = self.ServerAdress + "/api/Messanger"
        data = json.loads(msg)
        r = requests.post(url, json=data)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
