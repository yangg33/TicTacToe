import os
import random
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


def getbutton(num):
    if num == 1:
        return form.pushButton_1
    elif num == 2:
        return form.pushButton_2
    elif num == 3:
        return form.pushButton_3
    elif num == 4:
        return form.pushButton_4
    elif num == 5:
        return form.pushButton_5
    elif num == 6:
        return form.pushButton_6
    elif num == 7:
        return form.pushButton_7
    elif num == 8:
        return form.pushButton_8
    elif num == 9:
        return form.pushButton_9


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def computerturn():
    while True:
        r = random.randint(1, 9)
        button = getbutton(r)
        if button.text() == "":
            break
    button.setText("O")
    button.setEnabled(False)

    a = check()
    if a == 1:
        form.label.setText('Вы проиграли!')
        form.pushButton.setEnabled(True)
        for ss in range(1, 10):
            getbutton(ss).setEnabled(False)
    elif a == 0:
        form.label.setText('Ничья')
        form.pushButton.setEnabled(True)
        for ss in range(1, 10):
            getbutton(ss).setEnabled(False)



def start():
    for i in range(1, 10):
        button = getbutton(i)
        button.setText('')
        button.setEnabled(True)
    form.pushButton.setEnabled(False)
    form.label.setText('')
    r = random.randint(1, 2)
    if r == 1:
        computerturn()


def check():
    # 1 2 3
    # 4 5 6
    # 7 8 9
    for i in range(0, 7, 3):  # i = 0,3,6
        if getbutton(i + 1).text() == getbutton(i + 2).text() == getbutton(i + 3).text() != '':
            return 1
    for g in range(0, 3, 1):
        if getbutton(g + 1).text() == getbutton(g + 4).text() == getbutton(g + 7).text() != '':
            return 1
    if getbutton(1).text() == getbutton(5).text() == getbutton(9).text() != '':
        return 1
    if getbutton(3).text() == getbutton(5).text() == getbutton(7).text() != '':
        return 1
    for x in range(1, 10):
        if getbutton(x).text() == '':
            return -1
    return 0


def userturn(s):
    button = getbutton(s)
    button.setText('X')
    button.setEnabled(False)

    a = check()
    if a == 1:
        form.label.setText('Вы победили!')
        form.pushButton.setEnabled(True)
        for ss in range(1, 10):
            getbutton(ss).setEnabled(False)
    elif a == 0:
        form.label.setText('Ничья')
        form.pushButton.setEnabled(True)
        for ss in range(1, 10):
            getbutton(ss).setEnabled(False)
    else:
        computerturn()




# def f(x):
#     return y
# lambda a,  x = a: y(a)

Form, Windows = uic.loadUiType(resource_path('qt.ui'))
win = QApplication([])
windows = Windows()
form = Form()
form.setupUi(windows)

form.pushButton.clicked.connect(start)

form.pushButton_1.clicked.connect(lambda: userturn(1))
form.pushButton_2.clicked.connect(lambda: userturn(2))
form.pushButton_3.clicked.connect(lambda: userturn(3))
form.pushButton_4.clicked.connect(lambda: userturn(4))
form.pushButton_5.clicked.connect(lambda: userturn(5))
form.pushButton_6.clicked.connect(lambda: userturn(6))
form.pushButton_7.clicked.connect(lambda: userturn(7))
form.pushButton_8.clicked.connect(lambda: userturn(8))
form.pushButton_9.clicked.connect(lambda: userturn(9))

windows.show()
win.exec()
