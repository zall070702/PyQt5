from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

class Mywindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.label=QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry (0,0,400,400)
        self.setWindowTitle("Belajar PyQt5")


app = QApplication([])
window = Mywindow()
window.show()
app.exec_()