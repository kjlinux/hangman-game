from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Level(QLabel):
    def __init__(self, parent=None, end_value=10):
        super().__init__(parent)
        self.setObjectName("level")
        self.setFont(QFont("Tempus Sans ITC", 40))
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.current_step = 1
        self.end_value = end_value
        self.setText(f"étape {self.current_step}")
        
    def next(self):
        if self.current_step < self.end_value:
            self.current_step += 1
            self.setText(f"étape {self.current_step}")