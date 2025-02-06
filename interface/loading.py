# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QPropertyAnimation, QSequentialAnimationGroup)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)
from interface.game_arcade import GameArcade
from interface.game_limitless import GameLimitless

class Loading(object):
    
    def __init__(self, mode):
        self.mode = mode
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 100, 50, 150)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(13)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.animateProgressBar()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOADING", None))
    # retranslateUi
    
    def animateProgressBar(self):
        self.animation1 = QPropertyAnimation(self.progressBar, b"value")
        self.animation1.setDuration(500)
        self.animation1.setStartValue(0)
        self.animation1.setEndValue(30)

        self.animation2 = QPropertyAnimation(self.progressBar, b"value")
        self.animation2.setDuration(500)
        self.animation2.setStartValue(30)
        self.animation2.setEndValue(100)

        self.animGroup = QSequentialAnimationGroup()
        self.animGroup.addAnimation(self.animation1)
        self.animGroup.addAnimation(self.animation2)
        
        self.animGroup.finished.connect(self.processing_game)
                
        self.animGroup.start()
        
    def processing_game(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.game_mode = GameArcade() if self.mode == 'arcade' else GameLimitless()
        self.game_mode.setupUi(main_window) 

        main_window.resize(current_size)
        main_window.show()
        

