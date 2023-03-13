import json
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

class ServiceController():
    socket_client = None

    def command_sender(self, command, data):
        self.socket_client.send_command(command, data)
        result = self.socket_client.wait_response()

        return result

class ExecuteCommand(QtCore.QThread):
    retrun_signal = pyqtSignal(str)

    def __init__(self, command, data):
        super().__init__()
        self.command = command
        self.data = data

    def run(self):
        result = ServiceController().command_sender(self.command, self.data)
        self.retrun_signal.emit(json.dumps(result))