# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_level.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(693, 480)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, 0)
        self.selectLabel = QLabel(self.centralwidget)
        self.selectLabel.setObjectName(u"selectLabel")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(48)
        self.selectLabel.setFont(font)
        self.selectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.selectLabel)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, -1, 50, -1)
        self.easyLevel = QPushButton(self.widget)
        self.easyLevel.setObjectName(u"easyLevel")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.easyLevel.setFont(font1)
        self.easyLevel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.easyLevel.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.easyLevel.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 20px; /* Forme ovale */\n"
"    min-width: 80px;\n"
"    min-height: 40px;\n"
"    color: #DB5461; /* Couleur du texte par d\u00e9faut */\n"
"    font-weight: bold; /* Rendre le texte plus lisible */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.easyLevel.setCheckable(True)
        self.easyLevel.setChecked(False)

        self.horizontalLayout_3.addWidget(self.easyLevel)

        self.mediumLevel = QPushButton(self.widget)
        self.mediumLevel.setObjectName(u"mediumLevel")
        self.mediumLevel.setFont(font1)
        self.mediumLevel.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.mediumLevel.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 20px; /* Forme ovale */\n"
"    min-width: 80px;\n"
"    min-height: 40px;\n"
"    color: #DB5461; /* Couleur du texte par d\u00e9faut */\n"
"    font-weight: bold; /* Rendre le texte plus lisible */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.mediumLevel.setCheckable(True)
        self.mediumLevel.setChecked(False)

        self.horizontalLayout_3.addWidget(self.mediumLevel)

        self.hardLevel = QPushButton(self.widget)
        self.hardLevel.setObjectName(u"hardLevel")
        self.hardLevel.setFont(font1)
        self.hardLevel.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.hardLevel.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 20px; /* Forme ovale */\n"
"    min-width: 80px;\n"
"    min-height: 40px;\n"
"    color: #DB5461; /* Couleur du texte par d\u00e9faut */\n"
"    font-weight: bold; /* Rendre le texte plus lisible */\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.hardLevel.setCheckable(True)
        self.hardLevel.setChecked(False)

        self.horizontalLayout_3.addWidget(self.hardLevel)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, -1, 300, -1)
        
        self.nextButton = QPushButton(self.widget_2)
        self.nextButton.setObjectName(u"nextButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        self.nextButton.setFont(font2)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

