from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from SocketClient.SocketClient import SocketClient
from SocketClient.ServiceController import ServiceController
import sys

app = QApplication([])
ServiceController.socket_client = SocketClient()
main_window = MainWidget()

# main_window.setFixedSize(900, 600)
main_window.show()

sys.exit(app.exec_())