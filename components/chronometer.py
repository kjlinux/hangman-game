from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtGui import QFont

class Chronometer(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("chronometer")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Tempus Sans ITC", 40))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
        self.time = QTime(0, 0, 0)
        self.setText(self.time.toString("mm:ss"))
        
    def start(self):
        self.timer.start(1000)  # Update every second
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.time = QTime(0, 0, 0)
        self.setText(self.time.toString("mm:ss"))
    
    def update_time(self):
        self.time = self.time.addSecs(1)
        self.setText(self.time.toString("mm:ss"))