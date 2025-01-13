from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Signal

class LetterButton(QPushButton):
    letter_clicked = Signal(str)

    def __init__(self, letter, parent=None):
        super().__init__(letter, parent)
        self.letter = letter
        self.setObjectName(f"button_{letter}")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.setFont(font)
        self.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #FFD9CE; /* Fond par défaut */\n"
            "    border: 2px solid #DB5461; /* Bordure */\n"
            "    border-radius: 25px; /* Rayon (moitié du diamètre) */\n"
            "    width: 50px; /* Diamètre du cercle */\n"
            "    height: 50px; /* Diamètre du cercle */\n"
            "    color: #DB5461; /* Couleur du texte */\n"
            "    font-weight: bold; /* Texte en gras */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #DB5461; /* Fond quand coché */\n"
            "    color: #FFD9CE; /* Texte quand coché */\n"
            "}\n"
        )
        self.setCheckable(False)
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.letter_clicked.emit(self.letter)