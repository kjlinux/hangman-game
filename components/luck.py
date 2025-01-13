from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Luck(QLabel):
    def __init__(self, parent=None, initial_value=8):
        super().__init__(parent)
        self.setObjectName("luck")
        self.setFont(QFont("Tempus Sans ITC", 40))
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.chances = initial_value
        self.setText(f"{self.chances} chances")
        
    def lose(self):
        if self.chances > 0:
            self.chances -= 1
            self.setText(f"{self.chances} chances")