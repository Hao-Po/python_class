import json
from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QHBoxLayout()
        self.add_stu_status_widget = AddStuStatusWidget()
        self.add_stu_control_widget = AddStuControlWidget(self.add_stu_status_widget)
        self.add_stu_status_widget.init_status()
        layout.addWidget(self.add_stu_status_widget, stretch=2)
        layout.addWidget(self.add_stu_control_widget, stretch=1)

        self.setLayout(layout)

    def load(self):
        self.add_stu_status_widget.init_status()
        print("    addWidget")

class AddStuStatusWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_status_widget")
        self.student_list = dict()

        layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(20, "Add Student")
        self.header_label.setAlignment(QtCore.Qt.AlignRight)
        
        self.content_label_info = LabelComponent(12, " ")
        self.content_label_info.setStyleSheet("color: red;")
        self.content_label_name = LabelComponent(16,  "Name: ")
        self.content_label_subject = LabelComponent(16, "Subject: ")
        self.content_label_score = LabelComponent(16, "Score: ")
        self.content_label_show = LabelComponent(12, " ")
        
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.clear_editor_content_name
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_subject.mousePressEvent = self.clear_editor_content_subject
        self.editor_label_score = LineEditComponent("")
        self.editor_label_score.setValidator(QtGui.QIntValidator())

        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.query_action)
        self.button_add = ButtonComponent("Add")
        self.button_add.clicked.connect(self.add_action)

        layout.addWidget(self.header_label, 0, 0, 1, 3)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.content_label_subject, 2, 0, 1, 1)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)
        layout.addWidget(self.content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)
        layout.addWidget(self.content_label_show, 4, 0, 1, 3)
        
        layout.setColumnStretch(0, 1.5)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2.5)
        layout.setRowStretch(0, 2)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 5)

        self.setLayout(layout)

    def clear_editor_content_name(self, event):
        self.editor_label_name.clear()
        self.button_query.setEnabled(True)

    def clear_editor_content_subject(self, event):
        self.editor_label_subject.clear()
        self.button_add.setEnabled(True)

    def query_action(self):    
        self.student_list = dict()
        self.student_list['name'] = self.editor_label_name.text()

        self.query_command = ExecuteCommand(command = "query", data = self.student_list)
        self.query_command.start()    

        self.query_command.return_signal.connect(self.process_result)

    def process_result(self, result):
        if json.loads(result)['status'] == 'Fail':
            self.content_label_info.setText(f"Please enter subjects for student \'{self.editor_label_name.text()}\'")
            self.editor_label_subject.setEnabled(True)
            self.editor_label_score.setEnabled(True)
            self.subject_list = dict()
        else:
            self.content_label_info.setText(f"The student \'{self.editor_label_name.text()}\' already exists in DB.")

    def add_action(self):
        if self.editor_label_subject.text() == "" or self.editor_label_score.text() == "":
            self.content_label_info.setText("Subject or score is empty.")
        elif int(self.editor_label_score.text()) > 100 or int(self.editor_label_score.text()) < 0:
            self.content_label_info.setText("Score needs to be 0 ~ 100.")
        else:
            self.content_label_info.setText(f"Student {self.editor_label_name.text()}'s subject \'{self.editor_label_subject.text()}\' with score \'{self.editor_label_score.text()}\' added.")
            
            self.subject_list[self.editor_label_subject.text()] = self.editor_label_score.text()
            self.student_list['scores'] = json.dumps(self.subject_list)

    def init_status(self, info_clean=True):
        self.button_query.setEnabled(False)
        self.editor_label_subject.setText("")
        self.editor_label_subject.setEnabled(False)
        self.editor_label_score.setText("")
        self.editor_label_score.setEnabled(False)
        self.button_add.setEnabled(False)
        self.editor_label_name.setText("Name")
        if info_clean:
            self.content_label_info.setText("")

class AddStuControlWidget(QtWidgets.QWidget):
    def __init__(self, add_stu_status_widget):
        super().__init__()
        self.setObjectName("add_control_widget")

        self.add_stu_status_widget = add_stu_status_widget
        self.content_label_info = self.add_stu_status_widget.content_label_info
        self.student_list = self.add_stu_status_widget.student_list

        layout = QtWidgets.QGridLayout()

        self.button_send = ButtonComponent("Send")
        self.button_send.clicked.connect(self.send_action)
        layout.addWidget(self.content_label_info, 0, 0, 4, 1)
        layout.addWidget(self.button_send, 4, 0, 1, 1)

        self.setLayout(layout)

    def send_action(self):
        self.send_command = ExecuteCommand(command = "add", data = self.add_stu_status_widget.student_list)
        self.send_command.start()

        if self.add_stu_status_widget.editor_label_name.text() == "Name":
            self.content_label_info.setText("Please input correct information.")
        else:
            self.content_label_info.setText(f"Add {self.add_stu_status_widget.student_list} successfully.")
        
        self.add_stu_status_widget.student_list = dict()
        self.add_stu_status_widget.init_status(False)