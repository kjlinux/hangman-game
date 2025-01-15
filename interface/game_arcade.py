from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget, QStackedWidget, QDialog)
from components.chronometer import Chronometer
from components.step import Step
from components.luck import Luck
from interface.dialog_lose import DialogLose
from interface.dialog_win import DialogWin
from interface.dialog_back import DialogBack
import source_rc

class GameArcade(object):
    last_game_box_full = Signal()
    
    def setupUi(self, MainWindow, game_boxes):
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
        
        self.game_boxes = game_boxes
        
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")
        font = QFont()
        font.setFamilies([u"Tempus Sans ITC"])
        font.setPointSize(40)
        self.backButton.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentRevert))
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.clicked.connect(self.on_back_button_clicked)

        self.horizontalLayout.addWidget(self.backButton)

        self.chronometer = Chronometer(self.widget)
        self.chronometer.start()
        self.chronometer.setObjectName(u"chronometer")
        self.horizontalLayout.addWidget(self.chronometer)

        self.step = Step(self.widget)
        self.step.setObjectName(u"step")
        self.horizontalLayout.addWidget(self.step)

        self.luck = Luck(self.widget)
        self.luck.life_lost.connect(self.game_lose)
        self.luck.setObjectName(u"luck")
        self.horizontalLayout.addWidget(self.luck)

        self.verticalLayout_2.addWidget(self.widget)
        
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        for game_box in self.game_boxes:
            game_box.all_letters_filled.connect(self.next_game_box)
            self.stackedWidget.addWidget(game_box)
        
        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.last_game_box_full.connect(self.game_win)
    # setupUi
    def get_luck(self):
        return self.luck
    
    def get_step(self):
        return self.step
    
    def next_game_box(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)
        luck = self.get_luck()
        luck.reset()
        step = self.get_step()
        step.next()
        self.check_last_game_box_filled()
        
    def check_last_game_box_filled(self):
        last_game_box = self.stackedWidget.widget(self.stackedWidget.count() - 1)
        all_filled = all(line_edit.text() for line_edit in last_game_box.findChildren(QLineEdit))
        if all_filled:
            self.last_game_box_full.emit()

    def game_lose(self):
        dialog = QDialog()
        ui = DialogLose()
        ui.setupUi(dialog)
        dialog.exec()
        
    def game_win(self):
        dialog = QDialog()
        ui = DialogWin()
        ui.setupUi(dialog)
        dialog.exec()
        
    def on_back_button_clicked(self):
        dialog = QDialog()
        ui = DialogBack()
        ui.setupUi(dialog)
        dialog.exec()