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
        self.text_label = QLabel("There has not been no name entered, so i can't do anything yet")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked:")
        # self.button.pressed.connect(self.pressButton)
        # self.button.clicked.connect(self.clickedButton)

        self.button.setText("Set Name")
        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()
        # h.addStretch(1)
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        # v.addStretch(1)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)



        self.setWindowTitle("Nothing clicked yet")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        print(inputted_text)
        our_string = "You've entered " + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text + "'s Window")


    # def clickedButton(self):
    #     print("this button has been clicked - released")
    #
    # def pressButton(self):
    #     print("Button has been pressed")
    #     self.counter += 1
    #     self.button.setText("Clicked:"+  str(self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())