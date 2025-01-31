# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, Signal, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
class DialogLose(QDialog):
    return_to_main_menu = Signal()
    
    def __init__(self, parent=None, on_return_to_main_menu=None):
        super().__init__(parent)
        self.on_return_to_main_menu = on_return_to_main_menu
        self.setupUi(self)
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 420)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.label_3 = QLabel(Dialog)
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(Dialog)
        self.label.setPixmap(QPixmap(u":/images/lose.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(31)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(Dialog)
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(14)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.on_next_button_clicked)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"HANGMAN GAME", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"YOU ARE HANGED", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        
    def on_next_button_clicked(self):
        if self.on_return_to_main_menu:
            self.on_return_to_main_menu()
        self.close()
