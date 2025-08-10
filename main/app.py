import sys

from PyQt6.QtWidgets import QApplication
from QCefView import QCefConfig, QCefContext


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.cef_config = QCefConfig()
        self.cef_context = QCefContext(self, sys.argv, self.cef_config)

    def exec(self):
        super().exec()
