import json
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal

class ExecuteQueryCommand(QtCore.QThread):
    retrun_signal = pyqtSignal(str)

    def __init__(self, client, student_name):
        super().__init__()
        self.client = client
        self.student_name = student_name

    def run(self):
        self.client.send_command("query", {'name' : self.student_name})
        self.retrun_signal.emit(json.dumps(self.client.wait_response()))
        
        
class ExecuteAddCommand(QtCore.QThread):
    retrun_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        ...

class ExecuteSendCommand(QtCore.QThread):
    return_signal = pyqtSignal(str)
    
    def __init__(self, client, student_list):
        super().__init__()
        self.client = client
        self.student_list = student_list

    def run(self):
        self.client.send_command("add", self.student_list)
        self.client.wait_response() 