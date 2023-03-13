from WorkWidgets.MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication
from SocketClient.SocketClient import SocketClient
import sys

app = QApplication([])
client = SocketClient()
main_window = MainWidget(client)

main_window.setFixedSize(600, 400)
main_window.show()

sys.exit(app.exec_())