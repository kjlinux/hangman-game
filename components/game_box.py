from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from .game_line_edit import GameLineEdit
from .letter_button import LetterButton
from .game_state_picture import GameStatePicture

class GameBox(QWidget):
    def __init__(self, hidden_word, index, game_state_picture, parent=None):
        super().__init__(parent)
        self.setObjectName("widget_2")
        
        self.verticalLayout_3 = QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.description = QLabel(self)
        self.description.setObjectName("description")
        font1 = QFont()
        font1.setFamilies(["Tempus Sans ITC"])
        font1.setPointSize(29)
        self.description.setFont(font1)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setText(index)
        
        self.verticalLayout.addWidget(self.description)
        self.verticalLayout.addWidget(game_state_picture)
        
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.line_edits = []
        for _ in range(len(hidden_word)):
            line_edit = GameLineEdit(self)
            self.line_edits.append(line_edit)
            self.horizontalLayout_2.addWidget(line_edit)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        for letter in "ABCDEFGHIJ":
            button = LetterButton(letter, self)
            self.horizontalLayout_3.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        for letter in "KLMNOPQR":
            button = LetterButton(letter, self)
            self.horizontalLayout_4.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        for letter in "STUVWXYZ":
            button = LetterButton(letter, self)
            self.horizontalLayout_5.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        
        self.verticalLayout_3.addLayout(self.verticalLayout)