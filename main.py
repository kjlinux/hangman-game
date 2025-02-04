import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interface.main_menu import MainMenu
from providers.cube_provider import CubeProvider

cube = {
    "level": None,
    'options': [],
    'rounds': None
}

CubeProvider.set_instance(cube)

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainMenu(cube)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()