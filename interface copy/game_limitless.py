# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_limitless.ui'
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
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import source_rc
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(723, 717)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.pushButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFormat(u"%p%")

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(29)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.image = QLabel(self.widget_2)
        self.image.setObjectName(u"image")
        self.image.setPixmap(QPixmap(u":/images/hangman/images/hangman.png"))
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.image)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 10, 50, 25)
        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: none; /* Supprime toutes les bordures */\n"
"    border-bottom: 2px solid #DB5461; /* Ajoute une bordure uniquement en bas */\n"
"    padding: 5px; /* Ajout d'un espace interne pour le texte */\n"
"    background-color: transparent; /* Fond transparent (ou la couleur souhait\u00e9e) */\n"
"    color:  white; /* Couleur du texte */\n"
"}\n"
"")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.A = QPushButton(self.widget_2)
        self.A.setObjectName(u"A")
        font3 = QFont()
        font3.setFamilies([u"Tempus Sans ITC"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.A.setFont(font3)
        self.A.setStyleSheet(u"QPushButton {\n"
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
        self.A.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.A)

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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00e9tape 9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Index: animal aquatique", None))
        self.image.setText("")
        self.A.setText(QCoreApplication.translate("MainWindow", u"A", None))
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

