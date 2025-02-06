from PySide6.QtWidgets import QProgressBar, QWidget
from PySide6.QtCore import QTimer, Signal, Qt

class Timer(QProgressBar):
    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(u"progressBar")
        self.setAutoFillBackground(False)
        self.setStyleSheet(u"")
        self.setValue(100)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setTextVisible(False)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        
    def start(self):
        self.timer.start(2000)

    def update_progress(self):
        value = self.value() - 3
        if value <= 0:
            self.setValue(0)
            self.timer.stop()
            self.finished.emit()
        else:
            self.setValue(value)