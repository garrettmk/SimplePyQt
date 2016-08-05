import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('Hello, World')
    label.show()

    app.exec_()
    app.exit()
