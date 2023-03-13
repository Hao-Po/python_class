from PyQt5 import QtWidgets, QtCore, QtGui

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignLeft)

        self.setFont(QtGui.QFont("微軟正黑體", font_size, QtGui.QFont.Bold))
        self.setText(content)

class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))

        self.setStyleSheet(
            """
                QLineEdit
                {
                    border-radius: 12px; 
                    border-style: outset;
                }
            """
        )

class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))

        self.setStyleSheet(
            """
                QPushButton
                {
                    background-color: rgb(54, 54, 54);
                    color: rgb(255, 255, 255);
                    font-size: 24px;
                    border-radius: 14px; 
                    border: 5px groove black;
                    border-style: outset;
                }

                QPushButton::hover
                {
                    background-color : red;
                    border-radius: 12px;
                    border: 7px groove white;
                    border-style: outset;
                }

                QPushButton::pressed
                {
                    background-color : rgb(106, 90, 205);
                }
            """
        )
            
           
