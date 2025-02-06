from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from .game_mode import GameMode
from providers.game_mode_provider import GameModeProvider

class MainMenu(object):
    def __init__(self, cube):
        self.cube = cube
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

        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")
        font2 = QFont()
        font2.setFamilies([u"Tempus Sans ITC"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.playButton.setFont(font2)
        self.playButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButton.setStyleSheet(u"")
        self.playButton.setFlat(False)

        self.verticalLayout.addWidget(self.playButton)

        self.playButtonWelcomePage_2 = QPushButton(self.centralwidget)
        self.playButtonWelcomePage_2.setObjectName(u"playButtonWelcomePage_2")
        self.playButtonWelcomePage_2.setFont(font2)
        self.playButtonWelcomePage_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButtonWelcomePage_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.playButtonWelcomePage_2)

        WelcomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(WelcomePage)

        self.playButton.setDefault(False)

        QMetaObject.connectSlotsByName(WelcomePage)
        
        self.playButton.clicked.connect(self.on_play_button_clicked)
    # setupUi

    def retranslateUi(self, WelcomePage):
        WelcomePage.setWindowTitle(QCoreApplication.translate("WelcomePage", u"MainWindow", None))
        self.titleWelcomePage.setText(QCoreApplication.translate("WelcomePage", u"HANGMAN GAME", None))
        self.playButton.setText(QCoreApplication.translate("WelcomePage", u"PLAY", None))
        self.playButtonWelcomePage_2.setText(QCoreApplication.translate("WelcomePage", u"SCORES", None))
        
    def on_play_button_clicked(self):
        main_window = QApplication.activeWindow()
        current_size = main_window.size()

        self.game_mode = GameMode(self.cube)
        GameModeProvider.set_instance(self.game_mode, main_window)

        self.game_mode.setupUi(main_window)
        main_window.resize(current_size)


