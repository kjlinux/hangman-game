from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal

class Luck(QLabel):
    life_lost = Signal()
    def __init__(self, parent=None, level=0, mode="arcade"):
        super().__init__(parent)
        self.setObjectName("luck")
        self.setFont(QFont("Tempus Sans ITC", 40))
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.initial_value = 8
        self.mode = mode
        
        if level == 1:
            self.initial_value = 5
        elif level == 2:
            self.initial_value = 3
            
        self.life = self.initial_value
        
        if self.mode == "aracde":
            self.setText(f"{self.life} chances")
        else:
            self.setText(f"\u221E chances")
        
    def lose(self):
        if self.mode != "arcade": pass
        elif self.life > 0:
            self.life -= 1
            self.setText(f"{self.life} chances")
            if self.life == 0:
                self.life_lost.emit()
    
    def reset(self):
        if self.mode != "arcade": pass
        else:
            self.life = self.initial_value
            self.setText(f"{self.life} chances")