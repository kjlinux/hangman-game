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
            "    background-color: #FFD9CE;"
            "    border: 2px solid #DB5461;"
            "    border-radius: 25px;"
            "    width: 50px;"
            "    height: 50px;"
            "    color: #DB5461;"
            "    font-weight: bold;"
            "}"
            ""
            "QPushButton:pressed {"
            "    background-color: #DB5461;"
            "    color: #FFD9CE;"
            "}"
        )
        self.setCheckable(False)
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.letter_clicked.emit(self.letter)