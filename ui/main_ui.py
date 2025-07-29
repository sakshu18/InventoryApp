from PySide6.QtWidgets import QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System")
        self.setMinimumSize(600, 400)

        self.label = QLabel("Welcome to the Inventory Dashboard", self)
        self.label.move(150, 180)
