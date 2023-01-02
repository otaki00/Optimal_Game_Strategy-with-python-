from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QValidator
import sys
import qtawesome as qta
import simulation

COIN_SET = []
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()


def validating():
    rule = QIntValidator(0, 99)
    print(rule.validate("adl", 12))


set_input = QtWidgets.QLineEdit(window)
set_input.move(370, 380)
set_input.setFixedWidth(300)
set_input.setFixedHeight(34)


def add_coin():
    if set_input.text().isnumeric():
        if int(set_input.text()) > 0 and int(set_input.text()) < 100 and len(COIN_SET) < 165:
            COIN_SET.append(int(set_input.text()))
            set_input.setText("")


window.setGeometry(400, 100, 900, 700)
window.setWindowTitle("Project 1")
window.setWindowIcon(QtGui.QIcon('project1_icon.png'))

# Start the First Screen
# the user must enter the array of coins fisrt
# then validate it, if correct go to next screen
# else error alert show
# begin
title_message = QtWidgets.QLabel("Optimal Strategy for a Game", window)
title_message.move(180, 80)
title_message.setStyleSheet(
    'font-family:system-ui;color:#137CD9; font-size:40px; font-weight:bold')


welcome_message_content = '''                        
                        Welcome to my system
       Here you will see every thing about my ALGORITHM
    to start please insert a valid Value Of Coin, value > 0, <100
    the set must be integers ONLY , and enter the first value
    then hit next button, and so on, the max number is 15
    
'''

welcome_message = QtWidgets.QLabel(welcome_message_content, window)
welcome_message.move(200, 180)
welcome_message.setStyleSheet(
    'font-family:system-ui;color:#D9137F; font-size:18px; font-weight:500; text-align:center')

set_label = QtWidgets.QLabel("Enter value Here :", window)
set_label.move(200, 380)
set_label.setStyleSheet(
    'font-family:system-ui;color:#6208A9; font-size:18px; font-weight:500')


def start_simu():
    if len(COIN_SET) > 3 :
        simulation.main(COIN_SET)
        sys.exit(app.exit())


next_btn = QtWidgets.QPushButton(qta.icon('ei.caret-right'), "Next", window)
next_btn.move(570, 450)
next_btn.clicked.connect(add_coin)
done_btn = QtWidgets.QPushButton(qta.icon('ei.hand-right'), "Done", window)
done_btn.move(750, 630)
done_btn.clicked.connect(start_simu)


window.show()
app.exec_()
