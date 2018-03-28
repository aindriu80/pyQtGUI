import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        # label = QLabel("Hi there I am a label. Wooh.")
        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")
        #
        # horizontal = QHBoxLayout()
        # horizontal.addStretch()
        #
        # horizontal.addWidget(okButton)
        # horizontal.addWidget(cancelButton)
        #
        # vertical = QVBoxLayout()
        # vertical.addWidget(label)
        # vertical.addStretch(1)
        # vertical.addLayout(horizontal)
        #
        # self.setLayout(vertical)

        label = QLabel("Name: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked:")
        self.button.pressed.connect(self.pressButton)
        self.button.clicked.connect(self.clickedButton)

        h = QHBoxLayout()
        # h.addStretch(1)
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        # v.addStretch(1)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)



        self.setWindowTitle("Horizontal Layout")
        self.show()

    def clickedButton(self):
        print("this button has been clicked - released")

    def pressButton(self):
        print("Button has been pressed")
        self.counter += 1
        self.button.setText("Clicked:"+  str(self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())