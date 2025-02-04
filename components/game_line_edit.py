from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtGui import QFont, QCursor
from PySide6.QtCore import Qt

class GameLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        font2 = QFont()
        font2.setFamilies(["Tempus Sans ITC"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.setFont(font2)
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.setFixedWidth(10)
        self.setStyleSheet(
            "QLineEdit {\n"
            "    border: none;\n"
            "    border-bottom: 5px solid #DB5461; /* Épaissit la bordure en bas */\n"
            "    padding: 5px; /* Ajoute plus d'espace interne */\n"
            "    background-color: transparent;\n"
            "    color: white;\n"
            "    font-weight: bold; /* Rend le texte plus épais */\n"
            "}\n"
        )
        self.setMaxLength(1)
        self.setFrame(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setReadOnly(True)
        self.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)