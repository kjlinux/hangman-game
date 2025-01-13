# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_option.ui'
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
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.selectButton = QPushButton(self.widget)
        self.selectButton.setObjectName(u"selectButton")
        font1 = QFont()
        font1.setFamilies([u"Tempus Sans ITC"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.selectButton.setFont(font1)
        self.selectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.selectButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton.setCheckable(True)
        self.selectButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton)

        self.selectButton_2 = QPushButton(self.widget)
        self.selectButton_2.setObjectName(u"selectButton_2")
        self.selectButton_2.setFont(font1)
        self.selectButton_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_2.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_2.setCheckable(True)
        self.selectButton_2.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_2)

        self.selectButton_3 = QPushButton(self.widget)
        self.selectButton_3.setObjectName(u"selectButton_3")
        self.selectButton_3.setFont(font1)
        self.selectButton_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_3.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_3.setCheckable(True)
        self.selectButton_3.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_3)

        self.selectButton_4 = QPushButton(self.widget)
        self.selectButton_4.setObjectName(u"selectButton_4")
        self.selectButton_4.setFont(font1)
        self.selectButton_4.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_4.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_4.setCheckable(True)
        self.selectButton_4.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_4)

        self.selectButton_12 = QPushButton(self.widget)
        self.selectButton_12.setObjectName(u"selectButton_12")
        self.selectButton_12.setFont(font1)
        self.selectButton_12.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_12.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_12.setCheckable(True)
        self.selectButton_12.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_12)

        self.selectButton_6 = QPushButton(self.widget)
        self.selectButton_6.setObjectName(u"selectButton_6")
        self.selectButton_6.setFont(font1)
        self.selectButton_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_6.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_6.setCheckable(True)
        self.selectButton_6.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_6)

        self.selectButton_5 = QPushButton(self.widget)
        self.selectButton_5.setObjectName(u"selectButton_5")
        self.selectButton_5.setFont(font1)
        self.selectButton_5.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.selectButton_5.setStyleSheet(u"QPushButton {\n"
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
        self.selectButton_5.setCheckable(True)
        self.selectButton_5.setChecked(False)

        self.horizontalLayout_3.addWidget(self.selectButton_5)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(300, -1, 300, -1)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selectLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Animals", None))
        self.selectButton_2.setText(QCoreApplication.translate("MainWindow", u"Fruits", None))
        self.selectButton_3.setText(QCoreApplication.translate("MainWindow", u"Countries", None))
        self.selectButton_4.setText(QCoreApplication.translate("MainWindow", u"Foods", None))
        self.selectButton_12.setText(QCoreApplication.translate("MainWindow", u"Foods", None))
        self.selectButton_6.setText(QCoreApplication.translate("MainWindow", u"Foods", None))
        self.selectButton_5.setText(QCoreApplication.translate("MainWindow", u"Foods", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

