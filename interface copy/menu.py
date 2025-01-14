# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        if not WelcomePage.objectName():
            WelcomePage.setObjectName(u"WelcomePage")
        WelcomePage.resize(708, 537)
        font = QFont()
        font.setBold(False)
        WelcomePage.setFont(font)
        
        self.centralwidget = QWidget(WelcomePage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, -1, 88)
        
        self.titleWelcomePage = QLabel(self.centralwidget)
        self.titleWelcomePage.setObjectName(u"titleWelcomePage")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(48)
        font1.setBold(False)
        self.titleWelcomePage.setFont(font1)
        self.titleWelcomePage.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titleWelcomePage.setFrameShadow(QFrame.Shadow.Plain)
        self.titleWelcomePage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleWelcomePage.setMargin(-1)

        self.verticalLayout.addWidget(self.titleWelcomePage, 0, Qt.AlignmentFlag.AlignVCenter)

        self.playButtonWelcomePage = QPushButton(self.centralwidget)
        self.playButtonWelcomePage.setObjectName(u"playButtonWelcomePage")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.playButtonWelcomePage.setFont(font2)
        self.playButtonWelcomePage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButtonWelcomePage.setStyleSheet(u"")
        self.playButtonWelcomePage.setFlat(False)

        self.verticalLayout.addWidget(self.playButtonWelcomePage)

        self.playButtonWelcomePage_2 = QPushButton(self.centralwidget)
        self.playButtonWelcomePage_2.setObjectName(u"playButtonWelcomePage_2")
        self.playButtonWelcomePage_2.setFont(font2)
        self.playButtonWelcomePage_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButtonWelcomePage_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.playButtonWelcomePage_2)

        WelcomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomePage)

        self.playButtonWelcomePage.setDefault(False)


        QMetaObject.connectSlotsByName(WelcomePage)
    # setupUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())