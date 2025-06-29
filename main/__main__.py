import sys

from .app import App
from .main_window import MainWindow


def main():
    app = App()
    main_win = MainWindow()
    main_win.show()
    ret_code = app.exec()
    sys.exit(ret_code)


if __name__ == "__main__":
    main()
