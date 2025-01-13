from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class GameStatePicture(QLabel):
    def __init__(self, parent=None, image_path=""):
        super().__init__(parent)
        self.setObjectName("errorStateImage")
        self.setPixmap(QPixmap(image_path))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)