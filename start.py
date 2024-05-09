from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from run import Main_program

app = QApplication(sys.argv)

window = Main_program()

window.show()
app.exec()
