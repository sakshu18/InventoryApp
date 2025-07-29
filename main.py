from PySide6.QtWidgets import QApplication
from ui.login_ui import LoginWindow
from ui.main_ui import MainWindow
import sys

app = QApplication(sys.argv)

login = LoginWindow()
if login.exec():  # login accepted
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # <- Keep the app running after login
