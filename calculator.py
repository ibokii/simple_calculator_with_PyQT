from PyQt6 import QtWidgets
from calc_ui import Ui_MainWindow


class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		# Digits.
		self.pushButton_0.clicked.connect(self.digit_pressed)
		self.pushButton_1.clicked.connect(self.digit_pressed)
		self.pushButton_2.clicked.connect(self.digit_pressed)
		self.pushButton_3.clicked.connect(self.digit_pressed)
		self.pushButton_4.clicked.connect(self.digit_pressed)
		self.pushButton_5.clicked.connect(self.digit_pressed)
		self.pushButton_6.clicked.connect(self.digit_pressed)
		self.pushButton_7.clicked.connect(self.digit_pressed)
		self.pushButton_8.clicked.connect(self.digit_pressed)
		self.pushButton_9.clicked.connect(self.digit_pressed)
		# C-button.
		self.pushButton_C.clicked.connect(self.clear)
		# Unary operations.
		self.pushButton_plus_minus.clicked.connect(self.unary_operation_pressed)
		self.pushButton_percent.clicked.connect(self.unary_operation_pressed)
		# Binary operations.
		self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
		self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
		self.pushButton_divide.clicked.connect(self.binary_operation_pressed)
		self.pushButton_mul.clicked.connect(self.binary_operation_pressed)
		# Equal operator.
		self.pushButton_equal.clicked.connect(self.equals_pressed)
		# Binary operator check.
		self.pushButton_plus.setCheckable(True)
		self.pushButton_minus.setCheckable(True)
		self.pushButton_divide.setCheckable(True)
		self.pushButton_mul.setCheckable(True)
		# Period buttom.
		self.pushButton_dot.clicked.connect(self.period_pressed)

	def digit_pressed(self):
		# button = self.sender()
		# self.label.setText(format(float(self.label.text() + button.text()), '.15g'))
		button = self.sender()
		if '.' in self.label.text() and button.text() == '0':
			label = format(self.label.text() + button.text(), '.15')
		else:
			label = format(float(self.label.text() + button.text()), '.15g')
		self.label.setText(label)

	def period_pressed(self):
		labeltext = self.label.text()
		self.label.setText(labeltext + '.')

	def clear(self):
		self.label.setText('')

	def unary_operation_pressed(self):
		label = float(self.label.text())
		button = self.sender()
		if button.text() == '+/-':
			label = label * (-1)
		if button.text() == '%':
			label = label * 0.01

		self.label.setText(format(float(label), '.15g'))

	def binary_operation_pressed(self):
		self.first_num = float(self.label.text())
		self.label.setText('')
		button = self.sender()
		button.setChecked(True)

	def equals_pressed(self):
		self.second_num = float(self.label.text())
		if self.pushButton_plus.isChecked():
			self.label.setText(format(self.first_num + self.second_num, '.15g'))
			self.pushButton_plus.setChecked(False)

		if self.pushButton_minus.isChecked():
			self.label.setText(format(self.first_num - self.second_num, '.15g'))
			self.pushButton_minus.setChecked(False)

		if self.pushButton_mul.isChecked():
			self.label.setText(format(self.first_num * self.second_num, '.15g'))
			self.pushButton_mul.setChecked(False)

		if self.pushButton_divide.isChecked():
			self.label.setText(format(self.first_num / self.second_num, '.15g'))
			self.pushButton_divide.setChecked(False)
