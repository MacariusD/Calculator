import sys
from PyQt6.QtWidgets import QApplication

from core import CalcMainWindow

def main():
    app = QApplication(sys.argv)
    window = CalcMainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()