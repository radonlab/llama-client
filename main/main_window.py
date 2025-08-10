from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from QCefView import QCefSetting, QCefView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Llama")
        cef_setting = QCefSetting()
        cef_view = QCefView("https://www.baidu.com", cef_setting)
        self.setCentralWidget(cef_view)
