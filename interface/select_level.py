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
from .select_option import SelectOption

class SelectLevel(object):
    def __init__(self, cube):
        self.cube = cube
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
        self.easyLevelButton = QPushButton(self.widget)
        self.easyLevelButton.setObjectName(u"easyLevelButton")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(14)
        font1.setBold(True)
        
        self.easyLevelButton.setFont(font1)
        self.easyLevelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.easyLevelButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.easyLevelButton.setStyleSheet(u"QPushButton {\n"
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
        self.easyLevelButton.setCheckable(True)
        self.easyLevelButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.easyLevelButton)

        self.mediumLevelButton = QPushButton(self.widget)
        self.mediumLevelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mediumLevelButton.setFont(font1)
        self.mediumLevelButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.mediumLevelButton.setStyleSheet(u"QPushButton {\n"
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
        self.mediumLevelButton.setCheckable(True)
        self.mediumLevelButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.mediumLevelButton)

        self.hardLevelButton = QPushButton(self.widget)
        self.hardLevelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hardLevelButton.setFont(font1)
        self.hardLevelButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.hardLevelButton.setStyleSheet(u"QPushButton {\n"
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
        self.hardLevelButton.setCheckable(True)
        self.hardLevelButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.hardLevelButton)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, -1, 300, -1)
        
        self.nextButton = QPushButton(self.widget_2)
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        self.nextButton.setFont(font2)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.hide()

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
        self.nextButton.clicked.connect(self.on_next_button_clicked)
        
        self.easyLevelButton.clicked.connect(lambda: self.on_level_button_clicked(self.easyLevelButton, 0))
        self.mediumLevelButton.clicked.connect(lambda: self.on_level_button_clicked(self.mediumLevelButton, 1))
        self.hardLevelButton.clicked.connect(lambda: self.on_level_button_clicked(self.hardLevelButton, 2))
    # setupUi
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.easyLevelButton.setText(QCoreApplication.translate("MainWindow", u"EASY", None))
        self.mediumLevelButton.setText(QCoreApplication.translate("MainWindow", u"MEDIUM", None))
        self.hardLevelButton.setText(QCoreApplication.translate("MainWindow", u"HARD", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi
    
    def on_level_button_clicked(self, clicked_button, level):
        if (self.nextButton.isHidden()):
            self.nextButton.show()
        self.easyLevelButton.setChecked(False)
        self.mediumLevelButton.setChecked(False)
        self.hardLevelButton.setChecked(False)

        clicked_button.setChecked(True)
        self.cube["level"] = level

    def on_next_button_clicked(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.select_option = SelectOption(self.cube)
        self.select_option.setupUi(main_window)

        main_window.resize(current_size)
