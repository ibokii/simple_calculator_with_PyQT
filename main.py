import sys
from PyQt6.QtWidgets import QApplication
from calculator import CalculatorWindow

app = QApplication([])
calculator = CalculatorWindow()
sys.exit(app.exec())
