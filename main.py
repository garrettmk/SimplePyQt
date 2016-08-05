import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QWidget()

    label = QLabel('Hello, World!', widget)

    button = QPushButton('Quit', widget)
    button.clicked.connect(app.quit)

    layout = QVBoxLayout(widget)
    layout.addChildWidget(label)
    layout.addChildWidget(button)

    widget.setLayout(layout)
    widget.show()

    app.exec_()
    app.exit()
