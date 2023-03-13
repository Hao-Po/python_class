from PyQt5 import QtWidgets, QtGui
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from SocketClient.ServiceController import ExecuteCommand
import json

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")

        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Modify Student")
        self.modify_widget = ModifyWidget()
        self.query_widget = QueryWidget(self.modify_widget)

        self.modify_widget.query_widget = self.query_widget
        self.query_widget.init_status()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.query_widget, stretch=1)
        layout.addWidget(self.modify_widget, stretch=8)
        self.setLayout(layout)
    
    def load(self):
        self.modify_widget.modify_stu_status_widget.status_change(False)
        self.query_widget.init_status()
        print("    modifyWidget")

class ModifyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")
 
        layout = QtWidgets.QHBoxLayout()
        self.modify_stu_status_widget = ModifyStuStatusWidget()
        self.modify_stu_control_widget = ModifyStuControlWidget(self.modify_stu_status_widget)
        
        self.modify_stu_status_widget.status_change()

        layout.addWidget(self.modify_stu_status_widget, stretch=2)
        layout.addWidget(self.modify_stu_control_widget, stretch=1)   

        self.setLayout(layout)

class QueryWidget(QtWidgets.QWidget):
    def __init__(self, modify_widget):
        super().__init__()
        self.setObjectName("query_widget")
        self.student_list = dict()

        self.modify_widget = modify_widget
        self.combo_box = modify_widget.modify_stu_status_widget.combo_box_score

        layout = QtWidgets.QGridLayout()

        self.content_label_info = LabelComponent(12, " ")
        self.content_label_name = LabelComponent(16,  "Name: ")

        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.clear_editor_content_name
        
        self.button_query = ButtonComponent("Query")
        self.button_query.clicked.connect(self.query_action)

        layout.addWidget(self.content_label_info, 0, 0, 1, 5)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 2)
        layout.addWidget(self.button_query, 1, 3, 1, 2)

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
        self.modify_widget.modify_stu_control_widget.result_status = json.loads(result)['status']

        if json.loads(result)['status'] == 'OK':
            self.content_label_info.setText(f"Please enter subjects for student \'{self.editor_label_name.text()}\'")
            self.combo_box.clear()
            self.combo_box.addItems(json.loads(result)['scores'].keys())
            self.combo_box.currentIndexChanged.connect(self.modify_widget.modify_stu_status_widget.combo_box_select_changed)
            self.modify_widget.modify_stu_status_widget.editor_label_score_change.setText(f"{json.loads(result)['scores'][self.combo_box.currentText()]}")
            self.modify_widget.modify_stu_status_widget.scores = json.loads(result)['scores']
            self.modify_widget.modify_stu_status_widget.status_change(True)
            self.modify_widget.modify_stu_control_widget.student_name = self.editor_label_name.text()
        else:
            self.content_label_info.setText(f"The student \'{self.editor_label_name.text()}\' not exists in DB.")
    
    def init_status(self, info_clean=True):
        self.editor_label_name.setText("Name")
        self.button_query.setEnabled(False)
        if info_clean:
            self.content_label_info.setText("")

class ModifyStuStatusWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_status_widget")
        self.scores = None
        self.radio_status = False

        layout = QtWidgets.QGridLayout()
        
        self.radio_button_change = QtWidgets.QRadioButton('Change a current score:')
        self.radio_button_add = QtWidgets.QRadioButton('Add a new score:')

        self.radio_button_change.toggled.connect(self.radio_button_on_clicked)
        self.radio_button_add.toggled.connect(self.radio_button_on_clicked)

        self.combo_box_score = QtWidgets.QComboBox()
        
        self.content_label_subject = LabelComponent(16, "Subject: ")
        self.content_label_score = LabelComponent(16, "Score: ")

        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_subject.mousePressEvent = self.clear_editor_label_subject
        self.editor_label_score_change = LineEditComponent("")
        self.editor_label_score_change.mousePressEvent = self.clear_editor_label_score_change
        self.editor_label_score_change.setValidator(QtGui.QIntValidator())
        self.editor_label_score_add = LineEditComponent("")
        self.editor_label_score_add.setValidator(QtGui.QIntValidator())

        layout.addWidget(self.radio_button_change, 0, 0, 1, 3)
        layout.addWidget(self.combo_box_score, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_score_change, 1, 1, 1, 2)
        layout.addWidget(self.radio_button_add, 2 ,0, 1, 3)
        layout.addWidget(self.content_label_subject, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_subject, 3, 1, 1, 2)
        layout.addWidget(self.content_label_score, 4, 0, 1, 1)
        layout.addWidget(self.editor_label_score_add, 4, 1, 1, 2)
                
        self.setLayout(layout)
        
    def radio_button_on_clicked(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.radio_status = True

    def combo_box_select_changed(self, index):
        try:
            self.editor_label_score_change.setText(f"{self.scores[self.combo_box_score.currentText()]}")
        except:
            pass
        
    def clear_editor_label_subject(self, event):
        self.editor_label_subject.clear()

    def clear_editor_label_score_change(self, event):
        self.editor_label_score_change.clear()

    def status_change(self, boolen=False):
        self.combo_box_score.setEnabled(boolen)
        self.radio_button_change.setEnabled(boolen)
        self.radio_button_add.setEnabled(boolen)
        self.editor_label_subject.setEnabled(boolen)
        self.editor_label_score_change.setEnabled(boolen)
        self.editor_label_score_add.setEnabled(boolen)
        self.radio_status = False
        
class ModifyStuControlWidget(QtWidgets.QWidget):
    def __init__(self, modify_stu_status_widget):
        super().__init__()
        self.setObjectName("modify_control_widget")
        self.modify_stu_status_widget = modify_stu_status_widget
        self.student_name = ""
        self.result_status = None

        layout = QtWidgets.QGridLayout()

        self.content_label_info = LabelComponent(12, " ")
        self.content_label_info.setStyleSheet("color: red;")
        self.button_send = ButtonComponent("Confirm")
        self.button_send.clicked.connect(self.send_action)

        layout.addWidget(self.content_label_info, 0, 0, 4, 1)
        layout.addWidget(self.button_send, 4, 0, 1, 1)

        self.setLayout(layout)

    def send_action(self):
        if self.result_status == "OK":
            if self.modify_stu_status_widget.radio_status == False:
                self.content_label_info.setText("You should choose change or add button.")
            else:
                student_list = dict()
                student_list['name'] = self.student_name
                
                subject_dict = dict()
                if self.modify_stu_status_widget.radio_button_change.isChecked():
                    subject_dict[self.modify_stu_status_widget.combo_box_score.currentText()] = self.modify_stu_status_widget.editor_label_score_change.text()
                elif self.modify_stu_status_widget.radio_button_add.isChecked():
                    if self.modify_stu_status_widget.editor_label_subject.text() == "subject" or self.modify_stu_status_widget.editor_label_score_add.text() == "":
                        self.content_label_info.setText("Subject or score is empty.")
                        return 
                    else:
                        subject_dict[self.modify_stu_status_widget.editor_label_subject.text()] = self.modify_stu_status_widget.editor_label_score_add.text()

                student_list['scores_dict'] = subject_dict
                self.send_command = ExecuteCommand(command = "modify", data = student_list)
                self.send_command.start()
        else:
            self.content_label_info.setText("No this person can modify.")