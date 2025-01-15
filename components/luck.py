from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal

class Luck(QLabel):
    life_lost = Signal()
    def __init__(self, parent=None, initial_value=8):
        super().__init__(parent)
        self.setObjectName("luck")
        self.setFont(QFont("Tempus Sans ITC", 40))
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.initial_value = initial_value
        self.life = self.initial_value
        self.setText(f"{self.life} chances")
        
    def lose(self):
        if self.life > 0:
            self.life -= 1
            self.setText(f"{self.life} chances")
            if self.life == 0:
                self.life_lost.emit()
    
    def reset(self):
        self.life = self.initial_value
        self.setText(f"{self.life} chances")