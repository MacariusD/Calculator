from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
import operator

from about_dialog import AboutDialog

# Calculator state.
READY = 0 # Ready for a new input.
INPUT = 1 # Inputting a number.

class CalcMainWindow(QWidget):
    """main calculator window"""
    def __init__(self):
        super().__init__()

        uic.loadUi("..\\UI\\CalcMainWidget.ui", self)

        self.button_about.clicked.connect(self.onclicked_about_button)

        # Setup numbers. Auto create a function for each number button and pass the value to input_number2.
        for n in range(0, 10):
            getattr(self, 'button_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        # Setup operations.
        self.button_addition.pressed.connect(lambda: self.operation(operator.add))
        self.button_subtraction.pressed.connect(lambda: self.operation(operator.sub))
        self.button_multiplication.pressed.connect(lambda: self.operation(operator.mul))
        self.button_division.pressed.connect(lambda: self.operation(operator.truediv))

        self.button_percent.pressed.connect(self.operation_percent)
        self.button_equal.pressed.connect(self.equal)

        # Setup actions
        self.button_all_clear.pressed.connect(self.reset)

        #Memory connections
        self.button_memory_store.pressed.connect(self.memory_store)
        self.button_memory_recall.pressed.connect(self.memory_recall)

        #Memory initialization
        self.memory = 0
        self.reset()

        #Trigger Main Interface display
        self.show()


    def onclicked_about_button(self):
        """about info display"""
        aboutdialog = AboutDialog()
        aboutdialog.exec()

    def display(self):
        """display the stack"""
        self.main_display.display(self.stack[-1])

    def reset(self):
        """reset the calculator"""
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()
    
    def input_number(self, v):
        """number capture"""
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def operation(self, op):
        """operation capture"""
        if self.current_op:  # Complete the current operation
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operation_percent(self):
        """percent operation"""
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()

    def equal(self):
        """equal operation"""
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.main_display.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()

    def memory_store(self):
        """memory store"""
        self.memory = self.main_display.value()

    def memory_recall(self):
        """memory recall: """
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()