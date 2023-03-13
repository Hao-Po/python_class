from PyQt5 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent
from SocketClient.ServiceController import ExecuteCommand
import json

class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QVBoxLayout()
        
        header_label = LabelComponent(20, "Show Student")
        self.scroll_area = QtWidgets.QScrollArea()
        self.student_list = LabelComponent(12, "")

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.scroll_area, stretch=9)
        
        self.scroll_area.setWidget(self.student_list)
        self.scroll_area.setWidgetResizable(True)

        self.setLayout(layout)
    
    def load(self):
        print("    show widget")
        self.query_command = ExecuteCommand(command = "show", data = {})
        self.query_command.start()    
        self.query_command.retrun_signal.connect(self.process_result)

    def process_result(self, result):
        try:              
            result_string = ("==== student list ====\n")
            for data in json.loads(result)['parameters']:
                result_string += (f"Name: {data['name']}\n")
                for subject_name, subject_score in data['scores'].items():
                    result_string += (f"  subject: {subject_name}, score: {subject_score}\n")
                result_string += ("\n")
            result_string += ("================")
        
            self.student_list.setText(result_string)
        except:
            pass