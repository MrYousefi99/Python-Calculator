from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader


class Calculate(QMainWindow) :
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.my_ui = loader.load("cal.ui")
        self.my_ui.show()
        
             
app = QApplication([])
my_window = Calculate()      

app.exec()