import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QDialog

from about_dialog import AboutDialog

class CalcMainWindow(QWidget):
    """main calculator window"""
    def __init__(self):
        super().__init__()

        uic.loadUi("..\\UI\\CalcMainWidget.ui", self)

        self.button_about.clicked.connect(self.onclicked_about_button)
    
    def onclicked_about_button(self):
        """about info display"""
        aboutdialog = AboutDialog()
        aboutdialog.exec()


def main():
    app = QApplication(sys.argv)
    window = CalcMainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()