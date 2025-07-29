from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to Inventory Dashboard"))
        self.setLayout(layout)


### ui/user_master_ui.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class UserMaster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Master")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("User management coming soon"))
        self.setLayout(layout)