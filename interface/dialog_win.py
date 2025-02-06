# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, Qt)
from PySide6.QtGui import (QFont,QPixmap,)
from PySide6.QtWidgets import (QLabel, QPushButton,QVBoxLayout)
from providers.game_mode_provider import GameModeProvider

class DialogWin(object):
    def __init__(self, main_window):
        self.main_window = main_window
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setWindowFlags(Dialog.windowFlags() & ~Qt.WindowCloseButtonHint)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"background-color: rgb(255, 217, 206);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(219, 84, 97);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/medal.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(31)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(219, 84, 97);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(14)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color: rgb(219, 84, 97);")
        self.pushButton.clicked.connect(self.on_accept)

        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"HANGMAN GAME", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"YOU WIN", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    
    def on_accept(self):
        self.game_mode = GameModeProvider.get_instance()
        current_size = self.main_window.size()
        self.game_mode.setupUi(self.main_window)
        self.main_window.resize(current_size)
        self.main_window.show()
        self.dialog.close()

