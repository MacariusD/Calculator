from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class AboutDialog(QDialog):
    """about info display"""
    def __init__(self):
        super().__init__()

        uic.loadUi("..\\UI\\About.ui", self)