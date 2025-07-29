from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class ProductMaster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Product form coming soon"))
        self.setLayout(layout)