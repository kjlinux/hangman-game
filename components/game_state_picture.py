from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class GameStatePicture(QLabel):
    def __init__(self, level, parent=None):
        super().__init__(parent)
        self.setObjectName("GameStatePicture")
        self.setPixmap(QPixmap("../images/hangman_alive.png"))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.level = level
        self.life = 0
        if self.level == "medium":
            self.life = 5
        elif self.level == "hard":
            self.life = 3
        else:
            self.life = 8
    
    def updateState(self, level):
        if self.level == "easy":
            if self.life == 7:
                self.setPixmap(QPixmap("../images/hangman_easy_7.png"))
                self.life -= 1
            elif self.life == 6:
                self.setPixmap(QPixmap("../images/hangman_easy_6.png"))
                self.life -= 1
            elif self.life == 5:
                self.setPixmap(QPixmap("../images/hangman_easy_5.png"))
                self.life -= 1
            elif self.life == 4:
                self.setPixmap(QPixmap("../images/hangman_easy_4.png"))
                self.life -= 1
            elif self.life == 3:
                self.setPixmap(QPixmap("../images/hangman_easy_3.png"))
                self.life -= 1
            elif self.life == 2:
                self.setPixmap(QPixmap("../images/hangman_easy_2.png"))
                self.life -= 1
            elif self.life == 1:
                self.setPixmap(QPixmap("../images/hangman_easy_1.png"))
                self.life -= 1
            elif self.life == 0:
                self.setPixmap(QPixmap("../images/hangman_easy_0.png"))
        elif self.level == "medium":
            if self.life == 5:
                self.setPixmap(QPixmap("../images/hangman_medium_5.png"))
                self.life -= 1
            elif self.life == 4:
                self.setPixmap(QPixmap("../images/hangman_medium_4.png"))
                self.life -= 1
            elif self.life == 3:
                self.setPixmap(QPixmap("../images/hangman_medium_3.png"))
                self.life -= 1
            elif self.life == 2:
                self.setPixmap(QPixmap("../images/hangman_medium_2.png"))
                self.life -= 1
            elif self.life == 1:
                self.setPixmap(QPixmap("../images/hangman_medium_1.png"))
                self.life -= 1
            elif self.life == 0:
                self.setPixmap(QPixmap("../images/hangman_medium_0.png"))
        elif self.level == "hard":
            if self.life == 3:
                self.setPixmap(QPixmap("../images/hangman_hard_3.png"))
                self.life -= 1
            elif self.life == 2:
                self.setPixmap(QPixmap("../images/hangman_hard_2.png"))
                self.life -= 1
            elif self.life == 1:
                self.setPixmap(QPixmap("../images/hangman_hard_1.png"))
                self.life -= 1
            elif self.life == 0:
                self.setPixmap(QPixmap("../images/hangman_hard_0.png"))
    
    def getLife(self):
        return self.life
              
    def transferLife(self, life):
        if self.level == "easy":
            if life == 7:
                self.setPixmap(QPixmap("../images/hangman_easy_7.png"))
                self.life -= 1
            elif life == 6:
                self.setPixmap(QPixmap("../images/hangman_easy_6.png"))
                self.life -= 1
            elif life == 5:
                self.setPixmap(QPixmap("../images/hangman_easy_5.png"))
                self.life -= 1
            elif life == 4:
                self.setPixmap(QPixmap("../images/hangman_easy_4.png"))
                self.life -= 1
            elif life == 3:
                self.setPixmap(QPixmap("../images/hangman_easy_3.png"))
                self.life -= 1
            elif life == 2:
                self.setPixmap(QPixmap("../images/hangman_easy_2.png"))
                self.life -= 1
            elif life == 1:
                self.setPixmap(QPixmap("../images/hangman_easy_1.png"))
                self.life -= 1
            elif life == 0:
                self.setPixmap(QPixmap("../images/hangman_easy_0.png"))
        elif self.level == "medium":
            if life == 5:
                self.setPixmap(QPixmap("../images/hangman_medium_5.png"))
                self.life -= 1
            elif life == 4:
                self.setPixmap(QPixmap("../images/hangman_medium_4.png"))
                self.life -= 1
            elif life == 3:
                self.setPixmap(QPixmap("../images/hangman_medium_3.png"))
                self.life -= 1
            elif life == 2:
                self.setPixmap(QPixmap("../images/hangman_medium_2.png"))
                self.life -= 1
            elif life == 1:
                self.setPixmap(QPixmap("../images/hangman_medium_1.png"))
                self.life -= 1
            elif life == 0:
                self.setPixmap(QPixmap("../images/hangman_medium_0.png"))
        elif self.level == "hard":
            if life == 3:
                self.setPixmap(QPixmap("../images/hangman_hard_3.png"))
                self.life -= 1
            elif life == 2:
                self.setPixmap(QPixmap("../images/hangman_hard_2.png"))
                self.life -= 1
            elif life == 1:
                self.setPixmap(QPixmap("../images/hangman_hard_1.png"))
                self.life -= 1
            elif life == 0:
                self.setPixmap(QPixmap("../images/hangman_hard_0.png"))