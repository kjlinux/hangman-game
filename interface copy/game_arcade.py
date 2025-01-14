# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_arcade.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.backButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.backButton)

        self.pseudoTimer = QLabel(self.widget)
        self.pseudoTimer.setObjectName(u"pseudoTimer")
        self.pseudoTimer.setFont(font)
        self.pseudoTimer.setFrameShape(QFrame.Shape.NoFrame)
        self.pseudoTimer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.pseudoTimer)

        self.level = QLabel(self.widget)
        self.level.setObjectName(u"level")
        self.level.setFont(font)
        self.level.setFrameShape(QFrame.Shape.NoFrame)
        self.level.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.level)

        self.luck = QLabel(self.widget)
        self.luck.setObjectName(u"luck")
        self.luck.setFont(font)
        self.luck.setFrameShape(QFrame.Shape.NoFrame)
        self.luck.setFrameShadow(QFrame.Shadow.Sunken)
        self.luck.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.luck)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.description = QLabel(self.widget_2)
        self.description.setObjectName(u"description")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(29)
        self.description.setFont(font1)
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.description)

        self.errorStateImage = QLabel(self.widget_2)
        self.errorStateImage.setObjectName(u"errorStateImage")
        self.errorStateImage.setPixmap(QPixmap(u":../images/hangman.png"))
        self.errorStateImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.errorStateImage)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 10, 50, 25)
        
        self.case1 = QLineEdit(self.widget_2)
        self.case1.setObjectName(u"case1")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.case1.setFont(font2)
        self.case1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.case1.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.case1.setMaxLength(1)
        self.case1.setFrame(True)
        self.case1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case1.setReadOnly(True)
        self.case1.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.case1)

        self.case2 = QLineEdit(self.widget_2)
        self.case2.setObjectName(u"case2")
        self.case2.setFont(font2)
        self.case2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.case2.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.case2.setMaxLength(1)
        self.case2.setFrame(True)
        self.case2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case2.setReadOnly(True)
        self.case2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.case2)

        self.case3 = QLineEdit(self.widget_2)
        self.case3.setObjectName(u"case3")
        self.case3.setFont(font2)
        self.case3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.case3.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.case3.setMaxLength(1)
        self.case3.setFrame(True)
        self.case3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case3.setReadOnly(True)
        self.case3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.case3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.A_1 = QPushButton(self.widget_2)
        self.A_1.setObjectName(u"A_1")
        font3 = QFont()
        font3.setFamilies([u"Tempus Sans ITC"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.A_1.setFont(font3)
        self.A_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_1.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_1)

        self.A_2 = QPushButton(self.widget_2)
        self.A_2.setObjectName(u"A_2")
        self.A_2.setFont(font3)
        self.A_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_2.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_2)

        self.A_3 = QPushButton(self.widget_2)
        self.A_3.setObjectName(u"A_3")
        self.A_3.setFont(font3)
        self.A_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_3.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_3)

        self.A_4 = QPushButton(self.widget_2)
        self.A_4.setObjectName(u"A_4")
        self.A_4.setFont(font3)
        self.A_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_4.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_4)

        self.A_5 = QPushButton(self.widget_2)
        self.A_5.setObjectName(u"A_5")
        self.A_5.setFont(font3)
        self.A_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_5.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_5)

        self.A_6 = QPushButton(self.widget_2)
        self.A_6.setObjectName(u"A_6")
        self.A_6.setFont(font3)
        self.A_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_6.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_6)

        self.A_7 = QPushButton(self.widget_2)
        self.A_7.setObjectName(u"A_7")
        self.A_7.setFont(font3)
        self.A_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_7.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_7)

        self.A_8 = QPushButton(self.widget_2)
        self.A_8.setObjectName(u"A_8")
        self.A_8.setFont(font3)
        self.A_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_8.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_8)

        self.A_9 = QPushButton(self.widget_2)
        self.A_9.setObjectName(u"A_9")
        self.A_9.setFont(font3)
        self.A_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_9.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_9)

        self.A_10 = QPushButton(self.widget_2)
        self.A_10.setObjectName(u"A_10")
        self.A_10.setFont(font3)
        self.A_10.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_10.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.A_11 = QPushButton(self.widget_2)
        self.A_11.setObjectName(u"A_11")
        self.A_11.setFont(font3)
        self.A_11.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_11.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_11)

        self.A_12 = QPushButton(self.widget_2)
        self.A_12.setObjectName(u"A_12")
        self.A_12.setFont(font3)
        self.A_12.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_12.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_12)

        self.A_13 = QPushButton(self.widget_2)
        self.A_13.setObjectName(u"A_13")
        self.A_13.setFont(font3)
        self.A_13.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_13.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_13)

        self.A_18 = QPushButton(self.widget_2)
        self.A_18.setObjectName(u"A_18")
        self.A_18.setFont(font3)
        self.A_18.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_18.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_18)

        self.A_14 = QPushButton(self.widget_2)
        self.A_14.setObjectName(u"A_14")
        self.A_14.setFont(font3)
        self.A_14.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_14.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_14)

        self.A_15 = QPushButton(self.widget_2)
        self.A_15.setObjectName(u"A_15")
        self.A_15.setFont(font3)
        self.A_15.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_15.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_15)

        self.A_16 = QPushButton(self.widget_2)
        self.A_16.setObjectName(u"A_16")
        self.A_16.setFont(font3)
        self.A_16.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_16.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_16)

        self.A_17 = QPushButton(self.widget_2)
        self.A_17.setObjectName(u"A_17")
        self.A_17.setFont(font3)
        self.A_17.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_17.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.A_17)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.A_20 = QPushButton(self.widget_2)
        self.A_20.setObjectName(u"A_20")
        self.A_20.setFont(font3)
        self.A_20.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_20.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_20)

        self.A_21 = QPushButton(self.widget_2)
        self.A_21.setObjectName(u"A_21")
        self.A_21.setFont(font3)
        self.A_21.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_21.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_21)

        self.A_22 = QPushButton(self.widget_2)
        self.A_22.setObjectName(u"A_22")
        self.A_22.setFont(font3)
        self.A_22.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_22.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_22)

        self.A_23 = QPushButton(self.widget_2)
        self.A_23.setObjectName(u"A_23")
        self.A_23.setFont(font3)
        self.A_23.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_23.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_23)

        self.A_24 = QPushButton(self.widget_2)
        self.A_24.setObjectName(u"A_24")
        self.A_24.setFont(font3)
        self.A_24.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_24.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_24)

        self.A_25 = QPushButton(self.widget_2)
        self.A_25.setObjectName(u"A_25")
        self.A_25.setFont(font3)
        self.A_25.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_25.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_25)

        self.A_26 = QPushButton(self.widget_2)
        self.A_26.setObjectName(u"A_26")
        self.A_26.setFont(font3)
        self.A_26.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD9CE; /* Fond par d\u00e9faut */\n"
"    border: 2px solid #DB5461; /* Bordure */\n"
"    border-radius: 25px; /* Rayon (moiti\u00e9 du diam\u00e8tre) */\n"
"    width: 50px; /* Diam\u00e8tre du cercle */\n"
"    height: 50px; /* Diam\u00e8tre du cercle */\n"
"    color: #DB5461; /* Couleur du texte */\n"
"    font-weight: bold; /* Texte en gras */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DB5461; /* Fond quand coch\u00e9 */\n"
"    color: #FFD9CE; /* Texte quand coch\u00e9 */\n"
"}\n"
"")
        self.A_26.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.A_26)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pseudoTimer.setText(QCoreApplication.translate("MainWindow", u"15:10", None))
        self.level.setText(QCoreApplication.translate("MainWindow", u"\u00e9tape 9", None))
        self.luck.setText(QCoreApplication.translate("MainWindow", u"8 chances", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"Index: animal aquatique", None))
        self.errorStateImage.setText("")
        self.A_1.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.A_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.A_3.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.A_4.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.A_5.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.A_6.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.A_7.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.A_8.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.A_9.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.A_10.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.A_11.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.A_12.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.A_13.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.A_18.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.A_14.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.A_15.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.A_16.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.A_17.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.A_20.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.A_21.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.A_22.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.A_23.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.A_24.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.A_25.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.A_26.setText(QCoreApplication.translate("MainWindow", u"Z", None))
    # retranslateUi

