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
                           "    background-color: #FFD9CE;"
                           "    border: 2px solid #DB5461;"
                           "    border-radius: 20px;"
                           "    min-width: 80px;"
                           "    min-height: 40px;"
                           "    color: #DB5461;"
                           "    font-weight: bold; "
                           "}"
                           "\n"
                           "QPushButton:checked {"
                           "    background-color: #DB5461;"
                           "    color: #FFD9CE;"
                           "}"
                           "")
        self.setCheckable(True)
        self.setChecked(False)
        self.text = text
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clicked.connect(self.on_click)
        
    def on_click(self):
        self.option_clicked.emit(self.text)