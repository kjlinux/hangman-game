import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interface.main_menu import MainMenu

cube = {
    "level": None,
    'options': [],
    'rounds': None
}

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainMenu(cube)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()