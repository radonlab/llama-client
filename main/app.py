import sys

from PyQt6.QtWidgets import QApplication


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

    def exec(self):
        super().exec()
