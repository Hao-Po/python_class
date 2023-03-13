from PyQt5 import QtWidgets
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.WidgetComponents import LabelComponent

class MainWidget(QtWidgets.QWidget):
    def __init__(self, client):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(24, "Student Management System")
        add_stu_widget = AddStuWidget(client)

        layout.addWidget(header_label, stretch=20)
        layout.addWidget(add_stu_widget, stretch=80)
        
        self.setLayout(layout)
