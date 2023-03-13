import json
from PyQt5 import QtWidgets, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand

class DelStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("del_stu_widget")

        layout = QtWidgets.QHBoxLayout()
        self.del_stu_status_widget = DelStuStatusWidget()
        self.del_stu_control_widget = DelStuControlWidget(self.del_stu_status_widget)
        self.del_stu_status_widget.init_status()
        layout.addWidget(self.del_stu_status_widget, stretch=2)
        layout.addWidget(self.del_stu_control_widget, stretch=1)

        self.setLayout(layout)

    def load(self):
        self.del_stu_status_widget.init_status()
        print("    delWidget")

class DelStuStatusWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("del_status_widget")
        self.student_list = dict()
        self.result_status = None

        layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(20, "Delete Student")
        self.header_label.setAlignment(QtCore.Qt.AlignRight)
        
        self.content_label_info = LabelComponent(12, " ")
        self.content_label_info.setStyleSheet("color: red;")
        self.content_label_name = LabelComponent(16,  "Name: ")
        self.content_label_space = LabelComponent(12, "")
        
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.clear_editor_content_name

        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.query_action)

        layout.addWidget(self.header_label, 0, 0, 1, 3)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.content_label_space, 2, 0, 3, 4)

        self.setLayout(layout)

    def clear_editor_content_name(self, event):
        self.editor_label_name.clear()
        self.button_query.setEnabled(True)

    def query_action(self):    
        self.student_list = dict()
        self.student_list['name'] = self.editor_label_name.text()

        self.query_command = ExecuteCommand(command = "query", data = self.student_list)
        self.query_command.start()    

        self.query_command.retrun_signal.connect(self.process_result)

    def process_result(self, result):
        self.result_status = json.loads(result)['status']

        if self.result_status == 'Fail':
            self.content_label_info.setText(f"The student \'{self.editor_label_name.text()}\' not exists in DB")
        else:
            self.content_label_info.setText(f"The student \'{self.editor_label_name.text()}\' already exists in DB.")

    def init_status(self, info_clean=True):
        self.button_query.setEnabled(False)
        self.editor_label_name.setText("Name")
        if info_clean:
            self.content_label_info.setText("")

class DelStuControlWidget(QtWidgets.QWidget):
    def __init__(self, del_stu_status_widget):
        super().__init__()
        self.setObjectName("del_control_widget")

        self.del_stu_status_widget = del_stu_status_widget
        self.content_label_info = self.del_stu_status_widget.content_label_info
        self.student_list = self.del_stu_status_widget.student_list

        layout = QtWidgets.QGridLayout()

        self.button_send = ButtonComponent("Confirm")
        self.button_send.clicked.connect(self.send_action)

        layout.addWidget(self.content_label_info, 0, 0, 4, 1)
        layout.addWidget(self.button_send, 4, 0, 1, 1)

        self.setLayout(layout)

    def send_action(self):
        if self.del_stu_status_widget.result_status == "Fail":
            self.content_label_info.setText(f"No this person can delete.")
        else:
            self.send_command = ExecuteCommand(command = "delete", data = self.del_stu_status_widget.student_list)
            self.send_command.start()

            if self.del_stu_status_widget.editor_label_name.text() == "Name":
                self.content_label_info.setText("Please input correct information.")
            else:
                self.content_label_info.setText(f"Del {self.del_stu_status_widget.student_list} successfully.")
            
            self.del_stu_status_widget.student_list = dict()
            self.del_stu_status_widget.init_status(False)