from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

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