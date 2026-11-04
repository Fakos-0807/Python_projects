from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox
from random import randint

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.move(900, 100)
window.show()


text = QLabel("Натисни щоб дізнатись переможця")
win_number = QLabel("?")
number = randint(1,100)
btn = QPushButton("Згенерувати")

main_line = QVBoxLayout()
main_line.addWidget(text)
main_line.addWidget(win_number)
main_line.addWidget(btn)

window.setLayout(main_line)

def click():
    number = randint(1,100)
    win_number.setText(str(number))

btn.clicked.connect(click)

app.exec_()