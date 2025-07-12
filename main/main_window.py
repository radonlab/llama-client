from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from QCefView import QCefView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Llama")
        layout = QVBoxLayout()
        cef_view = QCefView()
        layout.addWidget(cef_view)
        self.setLayout(layout)
