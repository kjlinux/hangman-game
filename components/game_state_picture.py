from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import resources.resources_rc

class GameStatePicture(QLabel):
    def __init__(self, level=0, mode="arcade", parent=None):
        super().__init__(parent)
        self.setObjectName("GameStatePicture")
        self.mode = mode
        pixmap = QPixmap(":/images/hangman_alive.png") if self.mode == "arcade" else QPixmap(":/images/hangman_dead.png")
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.level = level
        self.life = 0
        if self.level == 1:
            self.life = 5
        elif self.level == 2:
            self.life = 3
        else:
            self.life = 7
    
    def updateState(self):
        if self.mode == "arcade":
            if self.level == 0:
                if self.life == 7:
                    self.setPixmap(QPixmap(":/images/hangman_easy_7.png"))
                    self.life -= 1
                elif self.life == 6:
                    self.setPixmap(QPixmap(":/images/hangman_easy_6.png"))
                    self.life -= 1
                elif self.life == 5:
                    self.setPixmap(QPixmap(":/images/hangman_easy_5.png"))
                    self.life -= 1
                elif self.life == 4:
                    self.setPixmap(QPixmap(":/images/hangman_easy_4.png"))
                    self.life -= 1
                elif self.life == 3:
                    self.setPixmap(QPixmap(":/images/hangman_easy_3.png"))
                    self.life -= 1
                elif self.life == 2:
                    self.setPixmap(QPixmap(":/images/hangman_easy_2.png"))
                    self.life -= 1
                elif self.life == 1:
                    self.setPixmap(QPixmap(":/images/hangman_easy_1.png"))
                    self.life -= 1
                elif self.life == 0:
                    self.setPixmap(QPixmap(":/images/hangman_dead.png"))
            elif self.level == 1:
                if self.life == 5:
                    self.setPixmap(QPixmap(":/images/hangman_medium_5.png"))
                    self.life -= 1
                elif self.life == 4:
                    self.setPixmap(QPixmap(":/images/hangman_medium_4.png"))
                    self.life -= 1
                elif self.life == 3:
                    self.setPixmap(QPixmap(":/images/hangman_medium_3.png"))
                    self.life -= 1
                elif self.life == 2:
                    self.setPixmap(QPixmap(":/images/hangman_medium_2.png"))
                    self.life -= 1
                elif self.life == 1:
                    self.setPixmap(QPixmap(":/images/hangman_medium_1.png"))
                    self.life -= 1
                elif self.life == 0:
                    self.setPixmap(QPixmap(":/images/hangman_dead.png"))
            elif self.level == 2:
                if self.life == 3:
                    self.setPixmap(QPixmap(":/images/hangman_hard_3.png"))
                    self.life -= 1
                elif self.life == 2:
                    self.setPixmap(QPixmap(":/images/hangman_hard_2.png"))
                    self.life -= 1
                elif self.life == 1:
                    self.setPixmap(QPixmap(":/images/hangman_hard_1.png"))
                    self.life -= 1
                elif self.life == 0:
                    self.setPixmap(QPixmap(":/images/hangman_dead.png"))
        else:
            self.setPixmap(QPixmap(":/images/hangman_dead.png"))