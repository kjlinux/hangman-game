from PySide6.QtCore import QCoreApplication, QMetaObject, QObject, QSize, Qt, Signal
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QDialog, QProgressBar
from components.chronometer import Chronometer
from components.step import Step
from components.luck import Luck
from interface.dialog_lose import DialogLose
from interface.dialog_win import DialogWin
from interface.dialog_back import DialogBack
from components.game_state_picture import GameStatePicture
from components.game_box import GameBox
from components.timer import Timer
from database.query_builder import QueryBuilder

class GameLimitless(QObject):
    last_game_box_full = Signal()
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet(u"background-color: rgb(109, 114, 195);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.widget = QWidget(self.centralwidget)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.main_window = MainWindow
        
        words = QueryBuilder().get_sorted_elements_by_level()
        
        game_boxes = []
        
        self.backButton = QPushButton(self.widget)
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
        self.horizontalLayout.addWidget(self.chronometer)

        self.step = Step(self.widget)
        self.horizontalLayout.addWidget(self.step)

        self.luck = Luck(self.widget)
        self.luck.life_lost.connect(self.game_lose)
        self.horizontalLayout.addWidget(self.luck)
        
        for key, value in words.items():
            game_state_picture = GameStatePicture()
            game_boxes.append(
                GameBox(key, value, game_state_picture, self.luck, MainWindow)
            )

        self.verticalLayout_2.addWidget(self.widget)
        
        self.timer = Timer(self.centralwidget)
        self.timer.finished.connect(self.game_lose)
        
        self.stackedWidget = QStackedWidget(self.centralwidget)
        for game_box in game_boxes:
            game_box.all_letters_filled.connect(self.next_game_box)
            self.stackedWidget.addWidget(game_box)
        
        self.verticalLayout_2.addWidget(self.timer)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.timer.start()

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

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
        self.timer.setValue(self.timer.value() + 10)

        
    def check_last_game_box_filled(self):
        last_game_box = self.stackedWidget.widget(self.stackedWidget.count() - 1)
        all_filled = all(line_edit.text() for line_edit in last_game_box.findChildren(QLineEdit))
        if all_filled:
            self.last_game_box_full.emit()

    def game_lose(self):
        dialog = QDialog(self.main_window)
        ui = DialogLose(self.main_window)
        ui.setupUi(dialog)
        dialog.exec()
        
    def game_win(self):
        dialog = QDialog(self.main_window)
        ui = DialogWin(self.main_window)
        ui.setupUi(dialog)
        dialog.exec()
        
    def on_back_button_clicked(self):
        dialog = QDialog(self.main_window)
        back_ui = DialogBack(self.main_window)
        back_ui.setupUi(dialog)
        dialog.exec()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.chronometer.setText(QCoreApplication.translate("MainWindow", u"15:10", None))
        self.step.setText(QCoreApplication.translate("MainWindow", u"\u00e9tape 1", None))
        self.luck.setText(QCoreApplication.translate("MainWindow", u"8 chances", None))