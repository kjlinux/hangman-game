
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from components.game_box import GameBox
from components.game_state_picture import GameStatePicture

if __name__ == "__main__":
    cube = {
    "level": None,
    'options': [],
    'number': None
    }
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    # Create GameBox widgets
    game_boxes = [
        GameBox(hidden_word="HANGMAN", index="Index 1", game_state_picture=GameStatePicture(image_path=":/images/hangman.png")),
        GameBox(hidden_word="PYTHON", index="Index 2", game_state_picture=GameStatePicture(image_path=":/images/hangman.png"))
    ]
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, game_boxes)
    MainWindow.show()
    sys.exit(app.exec())