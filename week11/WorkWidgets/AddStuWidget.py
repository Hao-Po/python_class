from tkinter.tix import Tree
from PyQt5 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")
        self.student_list = dict()

        layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(20, "Add Student")

        self.content_label_name = LabelComponent(16, "Name: ")
        self.content_label_subject = LabelComponent(16, "Subject: ")
        self.content_label_score = LabelComponent(16, "Score: ")
        self.content_label_info = LabelComponent(12, " ")
        self.content_label_info.setStyleSheet("color: red;")
        
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.clear_editor_content_name
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_subject.setEnabled(False)
        self.editor_label_subject.mousePressEvent = self.clear_editor_content_subject
        self.editor_label_score = LineEditComponent("")
        self.editor_label_score.setValidator(QtGui.QIntValidator())
        self.editor_label_score.setEnabled(False)

        self.button_query = ButtonComponent("Query")
        self.button_query.setEnabled(False)
        self.button_query.clicked.connect(self.query_action)
        self.button_add = ButtonComponent("Add")
        self.button_add.setEnabled(False)
        self.button_add.clicked.connect(self.add_action)
        self.button_send = ButtonComponent("Send")
        self.button_send.clicked.connect(self.send_action)

        layout.addWidget(self.header_label, 0, 0, 1, 3)
        layout.addWidget(self.content_label_info, 0, 3, 7, 1)
        layout.addWidget(self.content_label_name, 1, 0, 1, 1)
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.content_label_subject, 2, 0, 1, 1)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)
        layout.addWidget(self.content_label_score, 3, 0, 1, 1)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)
        layout.addWidget(self.button_send, 7, 3, 1, 1)
        
        layout.setColumnStretch(0, 1.5)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 2.5)
        layout.setColumnStretch(3, 3)
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
        self.content_label_info.setText(f"Please enter subjects for student \'{self.editor_label_name.text()}\'")
        self.editor_label_subject.setEnabled(True)
        self.editor_label_score.setEnabled(True)

        self.student_list['name'] = self.editor_label_name.text()
        self.subject_list = dict()

    def add_action(self):
        if self.editor_label_subject.text() == "" or self.editor_label_score.text() == "":
            self.content_label_info.setText("Subject or score is empty.")
        elif int(self.editor_label_score.text()) > 100 or int(self.editor_label_score.text()) < 0:
            self.content_label_info.setText("Score needs to be 0 ~ 100.")
        else:
            self.content_label_info.setText(f"Student {self.editor_label_name.text()}'s subject \'{self.editor_label_subject.text()}\' with score \'{self.editor_label_score.text()}\' added.")
            
            self.subject_list[self.editor_label_subject.text()] = self.editor_label_score.text()
            self.student_list['scores'] = self.subject_list

    def send_action(self):
        if self.editor_label_name.text() == "Name":
            self.content_label_info.setText("Please input correct information.")
        else:
            self.content_label_info.setText(f"The information {self.student_list} is sent.")

        self.button_query.setEnabled(False)
        self.editor_label_subject.setEnabled(False)
        self.editor_label_score.setEnabled(False)
        self.button_add.setEnabled(False)
        self.editor_label_name.setText("Name")