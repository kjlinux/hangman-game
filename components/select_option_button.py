from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import Qt, Signal

class SelectOptionButton(QPushButton):
    option_clicked = Signal(str)
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont("Tempus Sans ITC", 14, QFont.Bold))
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setStyleSheet(u"QPushButton {\n"
                           "    background-color: #FFD9CE; /* Fond par défaut */\n"
                           "    border: 2px solid #DB5461; /* Bordure */\n"
                           "    border-radius: 20px; /* Forme ovale */\n"
                           "    min-width: 80px;\n"
                           "    min-height: 40px;\n"
                           "    color: #DB5461; /* Couleur du texte par défaut */\n"
                           "    font-weight: bold; /* Rendre le texte plus lisible */\n"
                           "}\n"
                           "\n"
                           "QPushButton:checked {\n"
                           "    background-color: #DB5461; /* Fond quand coché */\n"
                           "    color: #FFD9CE; /* Texte quand coché */\n"
                           "}\n"
                           "")
        self.setCheckable(True)
        self.setChecked(False)
        self.text = text
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.on_click)
        
    def on_click(self):
        self.option_clicked.emit(self.text)