# # # # PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
# # # #
# # # #
# # # # class Note:
# # # #     def __init__(self, n, dl=False):
# # # #         self.n = n
# # # #         self.is_long = dl
# # # #
# # # #     def play(self):
# # # #         print(self.n)
# # # #
# # # #     def __str__(self):
# # # #         if not self.is_long:
# # # #             return self.n
# # # #         else:
# # # #             if self.n == 'до':
# # # #                 return 'до-о'
# # # #             if self.n == 'ре':
# # # #                 return 'ре-э'
# # # #             if self.n == 'ми':
# # # #                 return 'ми-и'
# # # #             if self.n == 'фа':
# # # #                 return 'фа-а'
# # # #             if self.n == 'соль':
# # # #                 return 'со-оль'
# # # #             if self.n == 'ля':
# # # #                 return 'ля-а'
# # # #             if self.n == 'си':
# # # #                 return 'си-и'
# # # #
# # # #
# # # # class LoudNote(Note):
# # # #     def __str__(self):
# # # #         if not self.is_long:
# # # #             return self.n.upper()
# # # #         else:
# # # #             if self.n == 'до':
# # # #                 return 'до-о'.upper()
# # # #             if self.n == 'ре':
# # # #                 return 'ре-э'.upper()
# # # #             if self.n == 'ми':
# # # #                 return 'ми-и'.upper()
# # # #             if self.n == 'фа':
# # # #                 return 'фа-а'.upper()
# # # #             if self.n == 'соль':
# # # #                 return 'со-оль'.upper()
# # # #             if self.n == 'ля':
# # # #                 return 'ля-а'.upper()
# # # #             if self.n == 'си':
# # # #                 return 'си-и'.upper()
# # # #
# # # #
# # # # class DefaultNote(Note):
# # # #     def __init__(self, n="до", is_long=False):
# # # #         self.n = n
# # # #         self.is_long = is_long
# # # #
# # # #
# # # # class NoteWithOctave(Note):
# # # #     def __init__(self, n, octava, is_long=False):
# # # #         self.n = n
# # # #         self.octava = octava
# # # #         self.is_long = is_long
# # # #
# # # #     def __str__(self):
# # # #         if not self.is_long:
# # # #             return f'{self.n} ({self.octava})'
# # # #         else:
# # # #             if self.n == 'до':
# # # #                 return f'до-о ({self.octava})'
# # # #             if self.n == 'ре':
# # # #                 return f'ре-э ({self.octava})'
# # # #             if self.n == 'ми':
# # # #                 return f'ми-и ({self.octava})'
# # # #             if self.n == 'фа':
# # # #                 return f'фа-а ({self.octava})'
# # # #             if self.n == 'соль':
# # # #                 return f'со-оль ({self.octava})'
# # # #             if self.n == 'ля':
# # # #                 return f'ля-а ({self.octava})'
# # # #             if self.n == 'си':
# # # #                 return f'си-и ({self.octava})'
# # #
# # #
# # # # class Point:
# # # #     def __init__(self, name, x, y):
# # # #         self.name = name
# # # #         self.x = x
# # # #         self.y = y
# # # #
# # # #     def get_x(self):
# # # #         return self.x
# # # #
# # # #     def get_y(self):
# # # #         return self.y
# # # #
# # # #     def get_coords(self):
# # # #         return self.x, self.y
# # # #
# # # #     def __invert__(self):
# # # #         return Point(self.name, self.y, self.x)
# # # #
# # # #     def __str__(self):
# # # #         return f'{self.name}({self.x, self.y})'
# # #
# # #
# # # N = 7
# # # PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
# # # LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
# # # INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
# # #
# # #
# # # class Note:
# # #     def __init__(self, n, is_long=False):
# # #         self.is_long = is_long
# # #         if self.is_long:
# # #             self.pit = LONG_PITCHES.copy()
# # #             self.n = LONG_PITCHES[PITCHES.index(n)]
# # #         else:
# # #             self.pit = PITCHES.copy()
# # #             self.n = n
# # #
# # #     def __eq__(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = note2.pit.index(note2.n)
# # #         if ind1 == ind2:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __lt__(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = note2.pit.index(note2.n)
# # #         if ind1 < ind2:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __ne__(self, note2):
# # #         if self.n != note2.n:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __gt__(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = note2.pit.index(note2.n)
# # #         if ind1 > ind2:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __le__(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = note2.pit.index(note2.n)
# # #         if ind1 <= ind2:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __ge__(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = note2.pit.index(note2.n)
# # #         if ind1 >= ind2:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def __lshift__(self, num):
# # #         k = self.pit.index(self.n)
# # #         m = self.pit[(k - num) % N]
# # #         return Note(PITCHES[self.pit.index(m)], self.is_long)
# # #
# # #     def __rshift__(self, num):
# # #         k = self.pit.index(self.n)
# # #         m = self.pit[(k + num) % N]
# # #         return Note(PITCHES[self.pit.index(m)], self.is_long)
# # #
# # #     def get_interval(self, note2):
# # #         ind1 = self.pit.index(self.n)
# # #         ind2 = PITCHES.index(note2.n)
# # #         return INTERVALS[ind1 - ind2]
# # #
# # #     def play(self):
# # #         print(self.n)
# # #
# # #     def __str__(self):
# # #         if not self.is_long:
# # #             return self.n
# # #         else:
# # #             if self.n == 'до':
# # #                 return 'до-о'
# # #             if self.n == 'ре':
# # #                 return 'ре-э'
# # #             if self.n == 'ми':
# # #                 return 'ми-и'
# # #             if self.n == 'фа':
# # #                 return 'фа-а'
# # #             if self.n == 'соль':
# # #                 return 'со-оль'
# # #             if self.n == 'ля':
# # #                 return 'ля-а'
# # #             if self.n == 'си':
# # #                 return 'си-и'
# # #
# # #
# # #
# # #
# # #
# # #
# # # # class LoudNote(Note):
# # # #     def __str__(self):
# # # #         if not self.is_long:
# # # #             return self.n.upper()
# # # #         else:
# # # #             if self.n == 'до':
# # # #                 return 'до-о'.upper()
# # # #             if self.n == 'ре':
# # # #                 return 'ре-э'.upper()
# # # #             if self.n == 'ми':
# # # #                 return 'ми-и'.upper()
# # # #             if self.n == 'фа':
# # # #                 return 'фа-а'.upper()
# # # #             if self.n == 'соль':
# # # #                 return 'со-оль'.upper()
# # # #             if self.n == 'ля':
# # # #                 return 'ля-а'.upper()
# # # #             if self.n == 'си':
# # # #                 return 'си-и'.upper()
# # # #
# # # #
# # # # class DefaultNote(Note):
# # # #     def __init__(self, n="до", is_long=False):
# # # #         self.n = n
# # # #         self.is_long = is_long
# # # #
# # # #
# # # # class NoteWithOctave(Note):
# # # #     def __init__(self, n, octava, is_long=False):
# # # #         self.n = n
# # # #         self.octava = octava
# # # #         self.is_long = is_long
# # # #
# # # #     def __str__(self):
# # # #         if not self.is_long:
# # # #             return f'{self.n} ({self.octava})'
# # # #         else:
# # # #             if self.n == 'до':
# # # #                 return f'до-о ({self.octava})'
# # # #             if self.n == 'ре':
# # # #                 return f'ре-э ({self.octava})'
# # # #             if self.n == 'ми':
# # # #                 return f'ми-и ({self.octava})'
# # # #             if self.n == 'фа':
# # # #                 return f'фа-а ({self.octava})'
# # # #             if self.n == 'соль':
# # # #                 return f'со-оль ({self.octava})'
# # # #             if self.n == 'ля':
# # # #                 return f'ля-а ({self.octava})'
# # # #             if self.n == 'си':
# # # #                 return f'си-и ({self.octava})'
# #
# #
# # import sys
# #
# # from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# # from PyQt6.QtWidgets import QLCDNumber, QLabel
# #
# # # import sys
# # #
# # # from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# # # from PyQt6.QtWidgets import QLabel, QLineEdit, QLCDNumber
# # #
# # #
# # # class MiniCalculator(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.initUI()
# # #
# # #     def initUI(self):
# # #         self.setGeometry(600, 300, 320, 250)
# # #         self.setWindowTitle('Миникалькулятор')
# # #         self.number_1 = QLineEdit(self)
# # #         self.number_1.move(10, 20)
# # #         self.number_2 = QLineEdit(self)
# # #         self.number_2.move(10, 80)
# # #         self.calculate_button = QPushButton("->", self)
# # #         self.calculate_button.resize(20, 20)
# # #         self.calculate_button.move(150, 50)
# # #         self.calculate_button.clicked.connect(self.run)
# # #
# # #         self.lab1 = QLabel(self)
# # #         self.lab1.setText("Первое чило(целое): ")
# # #         self.lab1.move(10, 3)
# # #         self.lab2 = QLabel(self)
# # #         self.lab2.setText("Второе число(целое): ")
# # #         self.lab2.move(10, 63)
# # #
# # #
# # #         self.result_sum = QLCDNumber(self)
# # #         self.result_sum.move(245,5)
# # #         self.res_lab = QLabel(self)
# # #         self.res_lab.setText("Сумма: ")
# # #         self.res_lab.move(200, 13)
# # #         self.result_sub = QLCDNumber(self)
# # #         self.result_sub.move(245, 35)
# # #         self.sub_lab = QLabel(self)
# # #         self.sub_lab.setText("Разность: ")
# # #         self.sub_lab.move(190, 42)
# # #         self.result_mul = QLCDNumber(self)
# # #         self.result_mul.move(245, 65)
# # #         self.mul_lab = QLabel(self)
# # #         self.mul_lab.setText("Произведение: ")
# # #         self.mul_lab.move(160, 71)
# # #         self.result_div = QLCDNumber(self)
# # #         self.result_div.move(245, 95)
# # #         self.div_lab = QLabel(self)
# # #         self.div_lab.setText("Частное: ")
# # #         self.div_lab.move(190, 95)
# # #
# # #
# # #     def run(self):
# # #         prim = self.first_value.text()
# # #         rez = eval(prim)
# # #         self.second_value.setText(str(rez))
# # #
# # #
# # # if __name__ == '__main__':
# # #     app = QApplication(sys.argv)
# # #     ex = MiniCalculator()
# # #     ex.show()
# # #     sys.exit(app.exec())
# #
# #
# # import sys
# #
# # from PyQt6 import uic  # Импортируем uic
# # from PyQt6.QtWidgets import QApplication, QMainWindow
# #
# #
# # class FlagMaker(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         uic.loadUi('untitled.ui', self)
# #         self.result.setText("")
# #         self.color_group_1.buttonClicked.connect(self.get1)
# #         self.color_group_2.buttonClicked.connect(self.get1)
# #         self.color_group_3.buttonClicked.connect(self.get1)
# #         self.make_flag.clicked.connect(self.run)
# #         self.data = {self.color_group_1: "Синий", self.color_group_2: "Синий", self.color_group_3: "Синий"}
# #
# #     def get1(self, button):
# #         self.data[self.sender()] = button.text()
# #
# #     def run(self):
# #         self.result.setText(str(self.data.values()))
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = FlagMaker()
# #     ex.show()
# #     sys.exit(app.exec())
#
# # def check():
# #     phone_number = input()
# #     phone_number = phone_number.replace(" ", "")
# #     phone_number = phone_number.replace("\t", "")
# #     phone_number = phone_number.replace("\n", "")
# #     if not (phone_number[0] == "8" or phone_number[0:2] == "+7"):
# #         print("error")
# #         return
# #     elif "--" in phone_number or phone_number[-1] == "-":
# #         print("error")
# #     else:
# #         phone_number = phone_number.replace("-", "")
# #
# #         if ")" in phone_number or "(" in phone_number:
# #             k = 0
# #             for i in phone_number:
# #                 if k == 0 and i == ")":
# #                     print("error")
# #                     return
# #                 elif "(" == i:
# #                     k += 1
# #                 elif ")" == i:
# #                     k -= 1
# #                 if k < 0:
# #                     print("error")
# #                     return
# #                 if k >= 2:
# #                     print("error")
# #                     return
# #             if k > 0:
# #                 print("error")
# #                 return
# #         phone_number = phone_number.replace("(", "")
# #         phone_number = phone_number.replace(")", "")
# #         if phone_number[0] == "8":
# #             phone_number = "+7" + phone_number[1:]
# #         if len(phone_number) != 12:
# #             print("error")
# #             return
# #         elif phone_number[1:].isdigit():
# #             print("error")
# #             return
# #         else:
# #             print(phone_number)
# #
# #
# # check()
#
# #
# # def abvgd():
# #     a = input()
# #     try:
# #         a = a.replace(' ', '')
# #         a = a.replace('\t', '')
# #         a = a.replace('\n', '')
# #         if not (a[0] == '8' or a[0:2] == '+7'):
# #             raise ValueError
# #         elif '--' in a or a[-1] == '-':
# #             raise ValueError
# #         else:
# #             if ')' in a or '(' in a:
# #                 k = 0
# #                 for i in a:
# #                     if k == 0 and i == ')':
# #                         raise ValueError
# #                     elif '(' == i:
# #                         k += 1
# #                     elif ')' == i:
# #                         k -= 1
# #                     if k < 0:
# #                         raise ValueError
# #                     if k >= 2:
# #                         raise ValueError
# #                 if k > 0:
# #                     raise ValueError
# #             a = a.replace('-', '')
# #             a = a.replace('(', '')
# #             a = a.replace(')', '')
# #
# #             if a[0] == '8':
# #                 a = '+7' + a[1:]
# #             if len(a) != 12:
# #                 raise ZeroDivisionError
# #             elif not a[1:].isdigit():
# #                 raise ValueError
# #             else:
# #                 print(a)
# #     except ValueError:
# #         print("неверный формат")
# #     except ZeroDivisionError:
# #         print("неверное количество цифр")
# #
# #
# # abvgd()
#
# # elif phone_number.count("(") != phone_number.count(")"):
# #     print("error")
#
#
# # import random as rnd
# #
# # f = open("lines.txt", mode="r+", encoding="utf-8")
# # text = f.readlines()
# # if text:
# #     rstring = rnd.choice(text)
# #     print(rstring)
# # f.close()
#
# # import random as rnd
# # import sys
# #
# # from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
# #
# #
# # class RandomString(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.setWindowTitle("Сучайная строка")
# #         self.setGeometry(400, 200, 600, 100)
# #         self.button = QPushButton("Получить", self)
# #         self.button.move(10, 35)
# #         self.text_field = QTextEdit(self)
# #         self.text_field.move(100, 10)
# #         self.text_field.resize(400, 70)
# #         self.button.clicked.connect(self.set_string)
# #
# #     def set_string(self):
# #         f = open("lines.txt", mode="r+", encoding="utf-8")
# #         text = f.readlines()
# #         if text:
# #             rstring = rnd.choice(text)
# #             self.text_field.setText(rstring)
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = RandomString()
# #     ex.show()
# #     sys.exit(app.exec())
#
#
#
#
# from PyQt6 import uic
# import random as rnd
# import sys
#
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
#
#
# from PyQt6 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(584, 496)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(50, 60, 161, 61))
#         font = QtGui.QFont()
#         font.setPointSize(13)
#         self.label.setFont(font)
#         self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label.setObjectName("label")
#         self.filenameEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.filenameEdit.setGeometry(QtCore.QRect(230, 80, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.filenameEdit.setFont(font)
#         self.filenameEdit.setObjectName("filenameEdit")
#         self.button = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.button.setGeometry(QtCore.QRect(410, 80, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.button.setFont(font)
#         self.button.setObjectName("button")
#         self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(50, 150, 291, 61))
#         font = QtGui.QFont()
#         font.setPointSize(13)
#         self.label_2.setFont(font)
#         self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label_2.setObjectName("label_2")
#         self.maxEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.maxEdit.setGeometry(QtCore.QRect(330, 170, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.maxEdit.setFont(font)
#         self.maxEdit.setObjectName("maxEdit")
#         self.minEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.minEdit.setGeometry(QtCore.QRect(330, 240, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.minEdit.setFont(font)
#         self.minEdit.setObjectName("minEdit")
#         self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(50, 220, 291, 61))
#         font = QtGui.QFont()
#         font.setPointSize(13)
#         self.label_3.setFont(font)
#         self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label_3.setObjectName("label_3")
#         self.avgEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.avgEdit.setGeometry(QtCore.QRect(330, 310, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.avgEdit.setFont(font)
#         self.avgEdit.setObjectName("avgEdit")
#         self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(50, 290, 291, 61))
#         font = QtGui.QFont()
#         font.setPointSize(13)
#         self.label_4.setFont(font)
#         self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label_4.setObjectName("label_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Имя файла"))
#         self.button.setText(_translate("MainWindow", "Рассчитать"))
#         self.label_2.setText(_translate("MainWindow", "Максимальное значение:"))
#         self.label_3.setText(_translate("MainWindow", "Минимальное значение:"))
#         self.label_4.setText(_translate("MainWindow", "Среднеее значение:"))
#
# class FileStat(QWidget, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('filestat.ui', self)
#         self.setupUi(self)
#
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = FileStat()
#     ex.show()
#     sys.exit(app.exec())


# import sys
#
# from PyQt6.QtGui import QPainter, QColor
# from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 200, 200)
#         self.setWindowTitle('PIL 2.0')
#         self.btn = QPushButton('Рисовать', self)
#         self.btn1 = QPushButton(self, "R")
#         self.btn2 = QPushButton(self, "G")
#         self.btn3 = QPushButton(self, "B")
#         self.btn4 = QPushButton(self, "ALL")
#         self.channelButtons.addButton(self.btn1, self.btn2, self.btn3, self.btn4)
#         self.curr_image = ""
#         self.btn1.clicked.connect(self.red)
#         self.btn1.clicked.connect(self.green)
#         self.btn1.clicked.connect(self.blue)
#         self.btn1.clicked.connect(self.all)
#
#     def red(self):
#         image = self.curr_image
#         for x in range(QImage.size(image).width()):
#             for y in range(QImage.size(image).height()):
#                 pixel = QImage.pixelColor(image, x, y)
#                 pixel.setBlue(0)
#                 pixel.setGreen(0)
#                 QImage.setPixelColor(image, x, y, pixel)
#         self.curr_image = image
#
#     def paintEvent(self, event):
#         if self.do_paint:
#             qp = QPainter()
#             qp.begin(self)
#             self.draw_flag(qp)
#             qp.end()
#         self.do_paint = False
#
#     def paint(self):
#         self.do_paint = True
#         self.update()
#
#     def draw_flag(self, qp):
#         qp.setBrush(QColor(255, 0, 0))
#         qp.drawRect(30, 30, 120, 30)
#         qp.setBrush(QColor(0, 255, 0))
#         qp.drawRect(30, 60, 120, 30)
#         qp.setBrush(QColor(0, 0, 255))
#         qp.drawRect(30, 90, 120, 30)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec())


"""1"""

# f = open("filename.txt", mode="r+", encoding="utf-8")
# text = f.readlines()
# for i in range(len(text)):
#     text[i] = text[i].replace('\n', '').split()
#     m = len(max(text[i], key=len))
#     text[i] = list(filter(lambda word: len(word) != m, text[i]))
#     text[i] = " ".join(text[i])
# text = "\n".join(text)
# new_f = open("qwer.txt", mode="w",encoding="utf-8")
# new_f.write(text)
# print(text)


"""2"""

# import sys
#
# files = list(map(str.strip, sys.stdin))
# files.sort()
# all_nums = [[], []]
# for file in files:
#     f = open(file, mode="r", encoding="utf-8")
#     nums = f.readlines()
#     for i in range(len(nums)):
#         nums[i] = nums[i].replace("\n", '')
#         nums[i] = nums[i].split()
#         nums[i] = list(map(int, nums[i]))
#
#         filt_n = list(filter(lambda n: int(n) % 2 != 0, nums[i]))
#         filt = list(filter(lambda n: int(n) % 2 == 0, nums[i]))
#         all_nums[0].append(filt)
#         all_nums[1].append(filt_n)
#     kol_nech = sum([len(i) for i in all_nums[1]])
#     kol_ch = sum([len(i) for i in all_nums[0]])
#     f = open("book.txt", mode="w", encoding="utf-8")
#     if kol_nech >= kol_ch:
#         for i in all_nums[1]:
#             i = list(map(str, i))
#             f.write(" ".join(i) + "\n")
#     f.close()


# f = open("filename.txt", mode="r+", encoding="utf-8")
# text = f.readlines()
# for i in range(len(text)):
#     text[i] = text[i].replace('\n', '').split()
#     m = len(max(text[i], key=len))
#     text[i] = list(filter(lambda word: len(word) != m, text[i]))
#     text[i] = " ".join(text[i])
# text = "\n".join(text)
# new_f = open("qwer.txt", mode="w", encoding="utf-8")
# new_f.write(text)
# print(text)
#
# f = open("filename.txt", mode="r+", encoding="utf-8")
# new_f = open("qwer.txt", mode="w", encoding="utf-8")
# text = f.readlines()
# for i in range(len(text)):
#     text[i] = text[i].replace('\n', '').split()
#     itog = []
#     for j in range(len(text[i])):
#         if text[i].count(text[i][j]) == 1:
#             itog.append(text[i][j])
#     itog[len(itog) - 1] = itog[len(itog) - 1] + '\n'
#     rez = " ".join(itog)
#     new_f.write(rez)
#
#
#
#
# import sys
#
# files = list(map(str.strip, sys.stdin))
# files.sort()
# all_nums = [[], []]
# for file in files:
#     f = open(file, mode="r", encoding="utf-8")
#     nums = f.readlines()
#     for i in range(len(nums)):
#         nums[i] = nums[i].replace("\n", '')
#         nums[i] = nums[i].split()
#         nums[i] = list(map(int, nums[i]))
#
#         filt_n = list(filter(lambda n: int(n) % 2 != 0, nums[i]))
#         filt = list(filter(lambda n: int(n) % 2 == 0, nums[i]))
#         all_nums[0].append(filt)
#         all_nums[1].append(filt_n)
#     kol_nech = sum([len(i) for i in all_nums[1]])
#     kol_ch = sum([len(i) for i in all_nums[0]])
#     f = open("book.txt", mode="w", encoding="utf-8")
#     if kol_nech >= kol_ch:
#         for i in all_nums[1]:
#             i = list(map(str, i))
#             f.write(" ".join(i) + "\n")
#     f.close()


# import sys
# import numpy as np
#
#
# def read_numbers_from_file(filename):
#     with open(filename, 'r') as f:
#         return [list(map(int, line.split())) for line in f]
#
#
# def calculate_median(numbers):
#     return np.median(numbers)
#
#
# def filter_numbers_below_median(lines, median):
#     result = []
#     for line in lines:
#         filtered = [str(num) for num in line if num < median]
#         result.append(' '.join(filtered))
#     return result
#
#
# def main():
#     filenames = sys.stdin.read().strip().split()
#     filenames.sort()
#
#     all_numbers = []
#     all_lines = []
#
#     for filename in filenames:
#         lines = read_numbers_from_file(filename)
#         all_lines.extend(lines)
#         for line in lines:
#             all_numbers.extend(line)
#
#     median = calculate_median(all_numbers)
#
#     output_lines = []
#     for filename in filenames:
#         lines = read_numbers_from_file(filename)
#         filtered_lines = filter_numbers_below_median(lines, median)
#         output_lines.extend(filtered_lines)
#
#     with open('face.txt', 'w') as f:
#         for line in output_lines:
#             f.write(line + '\n')
#
#
# if __name__ == "__main__":
#     main()


# f = open("input.bmp", "rb")
# bits = f.read()
# name = bits[:54]
# new_pallet = bytes([255 - d for d in bits[54:]])
# res = open("res.bmp", "wb")
# res.write(name + new_pallet)
# res.close()


# import csv

# f = open("wares.csv", mode="r", encoding="utf-8")
# reader = csv.reader(f, delimiter=";")
# reader = list(reader)
# summa = 1000
# data = [(r[0], int(r[1])) for r in reader]
# data.sort(key=lambda x: x[1])
# if data[0][1] > summa:
#     print("error")
# res = []
# while data != [] and summa >= data[0][1]:
#     count = summa // data[0][1]
#     if count > 10:
#         count = 10
#     summa -= count * data[0][1]
#     res = res + ([data[0][0]] * count)
#     del data[0]
# print(", ".join(res))

# import csv

# f = open("wares.csv", mode="r", encoding="utf-8")
# reader = csv.DictReader(f, delimiter=";")
# find_sale = filter(lambda row: int(row["New price"]) - int(row["Old price"]) < 0, reader)
# for i in find_sale:
#     print(i["Name"])


# import csv
# import sys
#
# from PyQt6 import uic
# from PyQt6.QtWidgets import (QApplication, QTableWidgetItem, QHeaderView, QWidget)
# from PyQt6 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 646)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(30, 10, 741, 511))
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(530, 550, 101, 31))
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         self.label.setFont(font)
#         self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
#         self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(630, 550, 113, 31))
#         font = QtGui.QFont()
#         font.setPointSize(11)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого:"))
#
#
# class InteractiveReceipt(QWidget, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.load_table("price.csv")
#         # self.tableWidget.itemChanged.connect(self.update_chek)
#
#     def load_table(self, file):
#         f = open(file, mode="r", encoding="utf-8")
#         reader = list(csv.reader(f, delimiter=";"))
#         title = reader[0]
#         self.tableWidget.setHorizontalHeaderLabels(title + ["Количество"])
#         self.tableWidget.setRowCount(0)
#         for i in range(len(reader[1:])):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             self.tableWidget.setItem(reader[i][0], reader[i][1])
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = InteractiveReceipt()
#     ex.show()
#     sys.exit(app.exec())

#
# import csv
# import sys
# from PyQt6.QtWidgets import (QApplication,
#                              QTableWidgetItem, QMainWindow)
# from PyQt6 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(816, 606)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(40, 20, 731, 491))
#         self.tableWidget.setLineWidth(1)
#         self.tableWidget.setAutoScrollMargin(16)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(490, 510, 81, 41))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(590, 520, 181, 31))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого"))
#
#
# class InteractiveReceipt(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setupUi(self)
#         self.load_table("price.csv")
#         self.tableWidget.itemChanged.connect(self.update_check)
#
#     def load_table(self, file):
#         f = open(file, mode='r', encoding="utf-8")
#
#         # # получаем данные
#         reader = list(csv.reader(f, delimiter=';'))
#         title = reader[0]
#
#         self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
#         # растянуть столбцы относительно таблицы
#         header = self.tableWidget.horizontalHeader()
#         header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
#
#         self.tableWidget.setRowCount(0)
#
#         for i in range(1, len(reader)):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             # указывает номер строки, столбца и сам элемент в ячейку
#             self.tableWidget.setItem(i - 1, 0, QTableWidgetItem(reader[i][0]))
#             self.tableWidget.setItem(i - 1, 1, QTableWidgetItem(reader[i][1]))
#             self.tableWidget.setItem(i - 1, 2, QTableWidgetItem('0'))
#
#     def update_check(self):
#         # получаем цену товаров, проходясь по 1 столбцу таблицы
#         price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
#         # получаем кол-во товара,  или 0, если ячейка не заполнена
#         count = [
#             int(self.tableWidget.item(i, 2).text())
#             if self.tableWidget.item(i, 2).text() != '' else 0
#             for i in
#             range(self.tableWidget.rowCount())]
#         # считаем итоговую сумму
#         sum_of = 0
#         for i in range(len(price)):
#             sum_of += price[i] * count[i]
#         self.total.setText(str(sum_of))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = InteractiveReceipt()
#     ex.show()
#     sys.exit(app.exec())


# import csv
# import sys
# import random
# from PyQt6.QtWidgets import (QApplication,
#                              QTableWidgetItem, QMainWindow)
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtGui import QColor
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(816, 606)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(40, 20, 731, 491))
#         self.tableWidget.setLineWidth(1)
#         self.tableWidget.setAutoScrollMargin(16)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(490, 510, 81, 41))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(590, 520, 181, 31))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         self.updateButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.updateButton.setGeometry(QtCore.QRect(20, 520, 93, 28))
#         self.updateButton.setObjectName("updateButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого"))
#         self.updateButton.setText(_translate("MainWindow", "Обновить"))
#
#
# class Expensive(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setupUi(self)
#         self.load_table("price.csv")
#         self.tableWidget.itemChanged.connect(self.update_check)
#         self.updateButton.clicked.connect(self.set_color)
#
#     def set_color(self):
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def load_table(self, file):
#         f = open(file, mode='r', encoding="utf-8")
#
#         # # получаем данные
#         reader = list(csv.reader(f, delimiter=';'))
#         title = reader[0]
#         reader = sorted(reader[1:], key=lambda x: -int(x[1]))
#         self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
#         # растянуть столбцы относительно таблицы
#         header = self.tableWidget.horizontalHeader()
#         header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
#
#         self.tableWidget.setRowCount(0)
#
#         for i in range(len(reader[1:])):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             # указывает номер строки, столбца и сам элемент в ячейку
#             self.tableWidget.setItem(i, 0, QTableWidgetItem(reader[i][0]))
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(reader[i][1]))
#             self.tableWidget.setItem(i, 2, QTableWidgetItem(''))
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def update_check(self):
#         # получаем цену товаров, проходясь по 1 столбцу таблицы
#         price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
#         # получаем кол-во товара,  или 0, если ячейка не заполнена
#         count = [
#             int(self.tableWidget.item(i, 2).text())
#             if self.tableWidget.item(i, 2).text() != '' else 0
#             for i in
#             range(self.tableWidget.rowCount())]
#         # считаем итоговую сумму
#         sum_of = 0
#         for i in range(len(price)):
#             sum_of += price[i] * count[i]
#         self.total.setText(str(sum_of))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Expensive()
#     ex.show()
#     sys.exit(app.exec())
#
#
#
#
#
# import csv
# import sys
# import random
# from PyQt6.QtWidgets import (QApplication,
#                              QTableWidgetItem, QMainWindow)
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtGui import QColor
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(816, 606)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(40, 20, 731, 491))
#         self.tableWidget.setLineWidth(1)
#         self.tableWidget.setAutoScrollMargin(16)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(490, 510, 81, 41))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(590, 520, 181, 31))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         self.updateButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.updateButton.setGeometry(QtCore.QRect(20, 520, 93, 28))
#         self.updateButton.setObjectName("updateButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого"))
#         self.updateButton.setText(_translate("MainWindow", "Обновить"))
#
#
# class Expensive(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setupUi(self)
#         self.load_table("price.csv")
#         self.tableWidget.itemChanged.connect(self.update_check)
#         self.updateButton.clicked.connect(self.set_color)
#
#     def set_color(self):
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def load_table(self, file):
#         f = open(file, mode='r', encoding="utf-8")
#
#         # # получаем данные
#         reader = list(csv.reader(f, delimiter=';'))
#         title = reader[0]
#         reader = sorted(reader[1:], key=lambda x: -int(x[1]))
#
#         self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
#         # растянуть столбцы относительно таблицы
#         header = self.tableWidget.horizontalHeader()
#         header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
#
#         self.tableWidget.setRowCount(0)
#
#         for i in range(len(reader)):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             # указывает номер строки, столбца и сам элемент в ячейку
#             self.tableWidget.setItem(i, 0, QTableWidgetItem(reader[i][0]))
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(reader[i][1]))
#             self.tableWidget.setItem(i, 2, QTableWidgetItem('0'))
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def update_check(self):
#         # получаем цену товаров, проходясь по 1 столбцу таблицы
#         price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
#         # получаем кол-во товара,  или 0, если ячейка не заполнена
#         count = [
#             int(self.tableWidget.item(i, 2).text())
#             if self.tableWidget.item(i, 2).text() != '' else 0
#             for i in
#             range(self.tableWidget.rowCount())]
#         # считаем итоговую сумму
#         sum_of = 0
#         for i in range(len(price)):
#             sum_of += price[i] * count[i]
#         self.total.setText(str(sum_of))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Expensive()
#     ex.show()
#     sys.exit(app.exec())


# import csv
# import sys
# import random
# from PyQt6.QtWidgets import (QApplication,
#                              QTableWidgetItem, QMainWindow)
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtGui import QColor
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(816, 606)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(40, 20, 731, 491))
#         self.tableWidget.setLineWidth(1)
#         self.tableWidget.setAutoScrollMargin(16)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(490, 510, 81, 41))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(590, 520, 181, 31))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         self.updateButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.updateButton.setGeometry(QtCore.QRect(20, 520, 93, 28))
#         self.updateButton.setObjectName("updateButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого"))
#         self.updateButton.setText(_translate("MainWindow", "Обновить"))
#
#
# class Expensive(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setupUi(self)
#         self.load_table("price.csv")
#         self.tableWidget.itemChanged.connect(self.update_check)
#         self.updateButton.clicked.connect(self.set_color)
#
#     def set_color(self):
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def load_table(self, file):
#         f = open(file, mode='r', encoding="utf-8")
#
#         # # получаем данные
#         reader = list(csv.reader(f, delimiter=';'))
#         title = reader[0]
#         reader = sorted(reader[1:], key=lambda x: -int(x[1]))
#
#         self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
#         # растянуть столбцы относительно таблицы
#         header = self.tableWidget.horizontalHeader()
#         header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
#
#         self.tableWidget.setRowCount(0)
#
#         for i in range(len(reader)):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             # указывает номер строки, столбца и сам элемент в ячейку
#             self.tableWidget.setItem(i, 0, QTableWidgetItem(reader[i][0]))
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(reader[i][1]))
#             self.tableWidget.setItem(i, 2, QTableWidgetItem('0'))
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def update_check(self):
#         # получаем цену товаров, проходясь по 1 столбцу таблицы
#         price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
#         # получаем кол-во товара,  или 0, если ячейка не заполнена
#         count = [
#             int(self.tableWidget.item(i, 2).text())
#             if self.tableWidget.item(i, 2).text() != '' else 0
#             for i in
#             range(self.tableWidget.rowCount())]
#         # считаем итоговую сумму
#         sum_of = 0
#         for i in range(len(price)):
#             sum_of += price[i] * count[i]
#         self.total.setText(str(sum_of))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Expensive()
#     ex.show()
#     sys.exit(app.exec())


# import random
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QMessageBox
# )
# from PyQt6.QtGui import QIcon
# from PyQt6.QtCore import Qt, QSize
#
#
# class MinesweeperGame(QMainWindow):
#     def __init__(self, rows=10, cols=10, mines=10):
#         super().__init__()
#         self.rows = rows
#         self.cols = cols
#         self.mines = mines
#         self.game_over = False
#         self.setup_ui()
#         self.init_game()
#
#     def setup_ui(self):
#         self.setWindowTitle("Minesweeper")
#         self.setWindowIcon(QIcon("icon.png"))
#         self.setFixedSize(QSize(50 * self.cols, 50 * self.rows + 50))
#
#         central_widget = QWidget()
#         grid_layout = QGridLayout()
#         central_widget.setLayout(grid_layout)
#         self.setCentralWidget(central_widget)
#
#         self.buttons = []
#         for row in range(self.rows):
#             row_buttons = []
#             for col in range(self.cols):
#                 button = QPushButton()
#                 button.setFixedSize(QSize(50, 50))
#                 button.clicked.connect(lambda checked, row=row, col=col: self.on_button_clicked(row, col))
#                 grid_layout.addWidget(button, row, col)
#                 row_buttons.append(button)
#             self.buttons.append(row_buttons)
#
#         self.status_label = QLabel()
#         grid_layout.addWidget(self.status_label, self.rows, 0, 1, self.cols)
#
#     def init_game(self):
#         self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#         self.revealed_cells = set()
#         self.place_mines()
#         self.update_board()
#
#     def place_mines(self):
#         mines_placed = 0
#         while mines_placed < self.mines:
#             row = random.randint(0, self.rows - 1)
#             col = random.randint(0, self.cols - 1)
#             if self.board[row][col] != -1:
#                 self.board[row][col] = -1
#                 mines_placed += 1
#
#     def update_board(self):
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 if (row, col) in self.revealed_cells:
#                     if self.board[row][col] == -1:
#                         self.buttons[row][col].setText("💣")
#                     else:
#                         count = self.count_adjacent_mines(row, col)
#                         if count > 0:
#                             self.buttons[row][col].setText(str(count))
#                         else:
#                             self.buttons[row][col].setText("")
#                 else:
#                     self.buttons[row][col].setText("")
#
#         if self.game_over:
#             self.status_label.setText("Game Over!")
#         else:
#             self.status_label.setText(f"Mines left: {self.mines - len(self.revealed_cells)}")
#
#     def count_adjacent_mines(self, row, col):
#         count = 0
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 new_row, new_col = row + dr, col + dc
#                 if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board[new_row][new_col] == -1:
#                     count += 1
#         return count
#
#     def on_button_clicked(self, row, col):
#         if self.game_over or (row, col) in self.revealed_cells:
#             return
#
#         if self.board[row][col] == -1:
#             self.game_over = True
#             self.reveal_all_mines()
#             QMessageBox.critical(self, "Game Over", "You hit a mine!")
#         else:
#             self.reveal_cell(row, col)
#             if self.check_win():
#                 QMessageBox.information(self, "Congratulations!", "You win!")
#                 self.game_over = True
#
#         self.update_board()
#
#     def reveal_cell(self, row, col):
#         self.revealed_cells.add((row, col))
#         if self.count_adjacent_mines(row, col) == 0:
#             for dr in [-1, 0, 1]:
#                 for dc in [-1, 0, 1]:
#                     new_row, new_col = row + dr, col + dc
#                     if 0 <= new_row < self.rows and 0 <= new_col < self.cols and (
#                     new_row, new_col) not in self.revealed_cells:
#                         self.reveal_cell(new_row, new_col)
#
#     def reveal_all_mines(self):
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 if self.board[row][col] == -1:
#                     self.revealed_cells.add((row, col))
#
#     def check_win(self):
#         return len(self.revealed_cells) == self.rows * self.cols - self.mines
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#     game = MinesweeperGame()
#     game.show()
#     app.exec()

#
# import sys
# import random
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMainWindow, QLabel
#
#
# class MineSweeper(QWidget):
#     def __init__(self, rows, cols, num_mines):
#         super().__init__()
#         self.rows = rows
#         self.cols = cols
#         self.num_mines = num_mines
#         self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
#         self.buttons = []
#         self.initUI()
#
#     def initUI(self):
#         layout = QGridLayout()
#
#         for i in range(self.rows):
#             row = []
#             for j in range(self.cols):
#                 button = QPushButton('')
#                 button.setFixedSize(40, 40)
#                 button.clicked.connect(lambda checked, i=i, j=j: self.on_click(i, j))
#                 layout.addWidget(button, i, j)
#                 row.append(button)
#             self.buttons.append(row)
#
#         self.generate_mines()
#
#         self.setLayout(layout)
#         self.setWindowTitle('MineSweeper')
#         self.show()
#
#     def generate_mines(self):
#         mines = 0
#         while mines < self.num_mines:
#             x = random.randint(0, self.rows - 1)
#             y = random.randint(0, self.cols - 1)
#             if self.grid[x][y] == 0:
#                 self.grid[x][y] = -1
#                 mines += 1
#                 for i in range(x - 1, x + 2):
#                     for j in range(y - 1, y + 2):
#                         if 0 <= i < self.rows and 0 <= j < self.cols and self.grid[i][j] != -1:
#                             self.grid[i][j] += 1
#
#     def on_click(self, x, y):
#         if self.grid[x][y] == -1:
#             self.buttons[x][y].setText('💣')
#             self.game_over()
#         else:
#             self.reveal_cell(x, y)
#
#     def reveal_cell(self, x, y):
#         if 0 <= x < self.rows and 0 <= y < self.cols and self.buttons[x][y].text() == '':
#             self.buttons[x][y].setText(str(self.grid[x][y]))
#             if self.grid[x][y] == 0:
#                 for i in range(x - 1, x + 2):
#                     for j in range(y - 1, y + 2):
#                         self.reveal_cell(i, j)
#
#     def game_over(self):
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if self.grid[i][j] == -1:
#                     self.buttons[i][j].setText('💣')
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(100, 100, 400, 400)
#         self.setWindowTitle('MineSweeper')
#
#         self.mine_sweeper = MineSweeper(10, 10, 10)
#         self.setCentralWidget(self.mine_sweeper)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

#
# import sqlite3
#
# name = input()
# con = sqlite3.connect(name)
# cur = con.cursor()
# result = cur.execute("""SELECT title FROM films
#     WHERE year >= 1995 AND year <= 2000 AND denre =(
#         SELECT id FROM genres
#         WHERE title = 'детектив') """).fetchall()
#
# for elem in result:
#     print(elem[0])
# con.close()

# import sqlite3
#
#
# def get_result(name):
#     con = sqlite3.connect(name)
#     cur = con.cursor()
#     cur.execute("""DELETE FROM films
#     WHERE duration >= 90 AND genre = (
#     SELECT id FROM genres
#     WHERE title = 'боевик') """).fetchall()
#     con.commit()
#     con.close()


# import sys
# from math import sin, cos, pi
# from random import randint
#
# from PyQt6.QtCore import Qt, QRectF, QPointF
# from PyQt6.QtGui import QPainter, QColor, QPolygonF
# from PyQt6.QtWidgets import QWidget, QApplication
#
#
# class Supermatism(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUi()
#         self.setMouseTracking(True)
#         self.coords = []
#
#         self.qp = QPainter()
#
#     def mousePressEvent(self, event):
#         self.coords = [event.pos().x(), event.pos().y()]
#         if (event.button() == Qt.MouseButton.LeftButton):
#             R = randint(20, 100)
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawEllipse(QPointF(self.coords[0], self.coords[0]), R, R)
#         elif (event.button() == Qt.MouseButton.RightButton):
#             A = randint(20, 100)
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawEllipse(QRectF(self.coords[0] - A / 2, self.coords[0] - A / 2, A, A))
#
#     def mouseMoveEventEvent(self, event):
#         self.coords = [event.pos().x(), event.pos().y()]
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Spase:
#             x, y = self.coords
#             A = randint(2, 100)
#             coords = QPolygonF([QPointF(x, y - A), QPointF(x + cos(7 * pi / 6) * A, y - sin(7 * pi / 6) * A),
#                                 QPointF(x + cos(7 * pi / 6) * A, y - sin(7 * pi / 6) * A)])
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawPolygon(coords)
#
#     def initUi(self):
#         self.setGeometry(300, 300, 1000, 1000)
#         self.setWindowTitle('Супрематизм')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Supermatism()
#     ex.show()
#     sys.exit(app.exec())


# import sys
# from math import sin, cos, pi
# from random import randint
#
# from PyQt6.QtCore import Qt, QRectF, QPointF
# from PyQt6.QtGui import QPainter, QColor, QPolygonF
# from PyQt6.QtWidgets import QWidget, QApplication
#
#
# class Suprematism(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.setMouseTracking(True)
#         self.coords_ = []
#         self.qp = QPainter()
#         self.flag = False
#         self.status = None
#
#     def drawf(self):
#         self.flag = True
#         self.update()
#
#     def paintEvent(self, event):
#         if self.flag:
#             self.qp = QPainter()
#             self.qp.begin(self)
#             self.draw(self.status)
#             self.qp.end()
#
#     def draw(self, status):
#         if status == 1:
#             R = randint(20, 100)
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawEllipse(QPointF(self.coords_[0],
#                                         self.coords_[1]), R, R)
#         elif status == 2:
#             A = randint(20, 100)
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawRect(QRectF(self.coords_[0] - A / 2,
#                                     self.coords_[1] - A / 2, A, A))
#         elif status == 3:
#             x, y = self.coords_
#             A = randint(20, 100)
#
#             coords = QPolygonF([QPointF(x, y - A),
#                                 QPointF(x + cos(7 * pi / 6) * A,
#                                         y - sin(7 * pi / 6) * A),
#                                 QPointF(x + cos(11 * pi / 6) * A,
#                                         y - sin(11 * pi / 6) * A)])
#             self.qp.setBrush(QColor(*[randint(0, 255) for _ in range(3)]))
#             self.qp.drawPolygon(coords)
#
#     def initUI(self):
#         self.setGeometry(300, 300, 1000, 1000)
#         self.setWindowTitle('Суперматизм')
#
#     def mousePressEvent(self, event):
#         self.coords = [event.pos().x(), event.pos().y()]
#         if (event.button() == Qt.MouseButton.LeftButton):
#             self.status = 1
#         elif (event.button() == Qt.MouseButton.RightButton):
#             self.status = 2
#         self.drawf()
#
#     def mouseMoveEvent(self, event):
#         self.coords_ = [event.pos().x(), event.pos().y()]
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Space:
#             self.status = 3
#             self.drawf()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Suprematism()
#     ex.show()
#     sys.exit(app.exec())


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(816, 606)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(40, 20, 731, 491))
#         self.tableWidget.setLineWidth(1)
#         self.tableWidget.setAutoScrollMargin(16)
#         self.tableWidget.setAlternatingRowColors(False)
#         self.tableWidget.setColumnCount(3)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setRowCount(0)
#         self.label = QtWidgets.QLabel(parent=self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(490, 510, 81, 41))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.total = QtWidgets.QLineEdit(parent=self.centralwidget)
#         self.total.setGeometry(QtCore.QRect(590, 520, 181, 31))
#         font = QtGui.QFont()
#         font.setPointSize(17)
#         self.total.setFont(font)
#         self.total.setObjectName("total")
#         self.updateButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.updateButton.setGeometry(QtCore.QRect(20, 520, 93, 28))
#         self.updateButton.setObjectName("updateButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Итого"))
#         self.updateButton.setText(_translate("MainWindow", "Обновить"))
#
#
# class Expensive(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setupUi(self)
#         self.load_table("price.csv")
#         self.tableWidget.itemChanged.connect(self.update_check)
#         self.updateButton.clicked.connect(self.set_color)
#
#     def set_color(self):
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def load_table(self, file):
#         f = open(file, mode='r', encoding="utf-8")
#
#         # # получаем данные
#         reader = list(csv.reader(f, delimiter=';'))
#         title = reader[0]
#         reader = sorted(reader[1:], key=lambda x: -int(x[1]))
#
#         self.tableWidget.setHorizontalHeaderLabels(title + ['Количество'])
#         # растянуть столбцы относительно таблицы
#         header = self.tableWidget.horizontalHeader()
#         header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
#
#         self.tableWidget.setRowCount(0)
#
#         for i in range(len(reader)):
#             self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
#             # указывает номер строки, столбца и сам элемент в ячейку
#             self.tableWidget.setItem(i, 0, QTableWidgetItem(reader[i][0]))
#             self.tableWidget.setItem(i, 1, QTableWidgetItem(reader[i][1]))
#             self.tableWidget.setItem(i, 2, QTableWidgetItem('0'))
#         for i in range(5):
#             color = [random.randrange(255) for _ in range(3)]
#             self.tableWidget.item(i, 0).setBackground(QColor(*color))
#             self.tableWidget.item(i, 1).setBackground(QColor(*color))
#             self.tableWidget.item(i, 2).setBackground(QColor(*color))
#
#     def update_check(self):
#         # получаем цену товаров, проходясь по 1 столбцу таблицы
#         price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
#         # получаем кол-во товара,  или 0, если ячейка не заполнена
#         count = [
#             int(self.tableWidget.item(i, 2).text())
#             if self.tableWidget.item(i, 2).text() != '' else 0
#             for i in
#             range(self.tableWidget.rowCount())]
#         # считаем итоговую сумму
#         sum_of = 0
#         for i in range(len(price)):
#             sum_of += price[i] * count[i]
#         self.total.setText(str(sum_of))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Expensive()
#     ex.show()
#     sys.exit(app.exec())


# import csv
#
# creatures = {}
#
# with open('fairytale.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['no', 'creature', 'habitat', 'stealth', 'power'])
#
#     count = 1
#     while True:
#         try:
#             info = input().split('; ')
#             creature = info[0]
#             habitat = info[1]
#             stealth = int(info[2])
#
#             if creature not in creatures:
#                 power = len(habitat) * (stealth // 2)
#                 creatures[creature] = (habitat, stealth, power)
#                 writer.writerow([count, creature, habitat, stealth, power])
#                 count += 1
#         except EOFError:
#             break


# import sqlite3
#
# sud = int(input())
# pl = input()
#
# con = sqlite3.connect("forest.db")
# cur = con.cursor()
# result = cur.execute(f"""SELECT name, looks_like FROM Events WHERE suddenness >= {sud}
# AND place = '{pl}'""").fetchall()
#
# rn = []
# for el in result:
#     rn.append(el[0] + ", ")
#     rn = list(set(rn))
#     rn.sort()
# rez1 = ''
# for elm in rn:
#     rez1 += elm
# rez1 = rez1[:len(rez1) - 2]
# ro = []
# for el in result:
#     ro.append(el[1] + ", ")
#     ro = list(set(ro))
#     ro.sort()
# rez2 = ''
# for elm in ro:
#     rez2 += elm
# rez2 = rez2[:len(rez2) - 2]
#
# print(rez1)
# print(rez2)
# con.close()

# def magic_eye(*tools):
#     import sqlite3
#     conn = sqlite3.connect("eye.db")
#     cur = conn.cursor()
#
#     query = f"""
#         SELECT Events.witness, Magicians.magician, Places.place
#         FROM Events
#         JOIN Magicians ON Events.magician_id = Magicians.id
#         JOIN Places ON Events.place_id = Places.id
#         WHERE Events.outcome < 0 AND Magicians.tool IN ({','.join(['?'] * len(tools))})
#     """
#     cur.execute(query, tools)
#     result = cur.fetchall()
#
#     result.sort(key=lambda x: (x[0], -ord(x[1][0]), x[2]), reverse=True)
#
#     conn.close()
#
#     return result
#
#
# tools = ['wand', 'beard', 'eye']
# print(*magic_eye('eye.db', *tools), sep='\n')


import sys
from random import randint
from PyQt6 import uic

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        print(456)
        self.pushButton.clicked.connect(self.run)
        print(56)
        self.qp = QPainter()
        self.flag = False

    def run(self):
        self.drawf()

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = randint(20, 100)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(QPointF(randint(20, 700),
                                    randint(20, 500)), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
