# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from .select_level import SelectLevel
from interface.loading import Loading

class GameMode(object):
    def __init__(self, cube):
        self.cube = cube
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(0, 0)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 88)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.arcadeButton = QPushButton(self.centralwidget)
        self.arcadeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(18)
        self.arcadeButton.setFont(font1)

        self.verticalLayout.addWidget(self.arcadeButton)

        self.limitlessButton = QPushButton(self.centralwidget)
        self.limitlessButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.limitlessButton.setFont(font1)

        self.verticalLayout.addWidget(self.limitlessButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.arcadeButton.clicked.connect(self.on_arcade_button_clicked)
        self.limitlessButton.clicked.connect(self.on_limitless_button_clicked)
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"GAME MODE", None))
        self.arcadeButton.setText(QCoreApplication.translate("MainWindow", u"ARCADE", None))
        self.limitlessButton.setText(QCoreApplication.translate("MainWindow", u"LIMITLESS", None))
    
    def on_arcade_button_clicked(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.select_level = SelectLevel(self.cube)
        self.select_level.setupUi(main_window)

        main_window.resize(current_size)
        
    def on_limitless_button_clicked(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.loading = Loading('limitless')
        self.loading.setupUi(main_window)

        main_window.resize(current_size)

