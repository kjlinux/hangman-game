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
        self.setStyleSheet(
            "QLineEdit {\n"
            "    border: none; /* Supprime toutes les bordures */\n"
            "    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
            "    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
            "    background-color: transparent; /* Fond transparent (ou la couleur souhaitée) */\n"
            "    color:  white; /* Couleur du texte */\n"
            "}\n"
        )
        self.setMaxLength(1)
        self.setFrame(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setReadOnly(True)
        self.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)