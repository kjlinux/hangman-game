from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal, QTimer
from .game_line_edit import GameLineEdit
from .letter_button import LetterButton
from .game_state_picture import GameStatePicture
from PySide6.QtGui import QKeyEvent
import unicodedata

class GameBox(QWidget):
    all_letters_filled = Signal()
    def __init__(self, hidden_word, index, game_state_picture, luck, parent=None):
        super().__init__(parent)
        self.setObjectName("widget_2")
        self.gameStatePicture = game_state_picture
        self.luck = luck
        self.hidden_word = self.format_word(hidden_word)
        
        self.setFocusPolicy(Qt.StrongFocus)
        
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
        self.verticalLayout.addWidget(self.gameStatePicture)
        
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.line_edits = []
        for _ in range(len(self.hidden_word)):
            line_edit = GameLineEdit(self)
            self.line_edits.append(line_edit)
            self.horizontalLayout_2.addWidget(line_edit)
        
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        for letter in "ABCDEFGHIJ":
            button = LetterButton(letter, self)
            button.letter_clicked.connect(self.on_letter_clicked)
            self.horizontalLayout_3.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        for letter in "KLMNOPQR":
            button = LetterButton(letter, self)
            button.letter_clicked.connect(self.on_letter_clicked)
            self.horizontalLayout_4.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        for letter in "STUVWXYZ":
            button = LetterButton(letter, self)
            button.letter_clicked.connect(self.on_letter_clicked)
            self.horizontalLayout_5.addWidget(button)
        
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        
        self.verticalLayout_3.addLayout(self.verticalLayout)
        
    def access_luck(self):
        luck = self.main_window.get_luck()
        return luck
    
    def access_level(self):
        main_window = self.parent().parent().parent().parent()
        luck = main_window.get_level()
        return luck
    
    def on_letter_clicked(self, letter):
        lower = self.format_word(letter)
        if lower in self.hidden_word:
            for index, char in enumerate(self.hidden_word):
                if char == lower:
                    self.line_edits[index].setText(letter)
            self.check_all_letters_filled()
        else:
            self.gameStatePicture.updateState()
            self.luck.lose()
            
    def check_all_letters_filled(self):
        if all(line_edit.text() for line_edit in self.line_edits):
            self.all_letters_filled.emit()
            
    def format_word(self, text):
        text = text.lower()
        text = unicodedata.normalize("NFD", text)
        text = "".join(char for char in text if unicodedata.category(char) != "Mn")
        return text
    
    def keyPressEvent(self, event: QKeyEvent):
        letter = event.text().upper()
        for layout in [self.horizontalLayout_3, self.horizontalLayout_4, self.horizontalLayout_5]:
            for i in range(layout.count()):
                button = layout.itemAt(i).widget()
                if button and button.letter == letter:
                    button.on_click()
                    return
                
    # def keyPressEvent(self, event: QKeyEvent):
    #     letter = event.text().upper()
    #     for layout in [self.horizontalLayout_3, self.horizontalLayout_4, self.horizontalLayout_5]:
    #         for i in range(layout.count()):
    #             button = layout.itemAt(i).widget()
    #             if button and button.letter == letter:
    #                 button.setDown(True)
    #                 button.on_click()
    #                 QTimer.singleShot(100, lambda: button.setDown(False))
    #                 return