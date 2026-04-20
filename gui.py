import sys
import os
from qtpy import QtWidgets
from qtpy.QtCore import Qt, Slot, QMetaObject, QEvent
from qtpy.QtGui import QFontDatabase, QAction, QIcon, QKeySequence, QShortcut

from BlurWindow.blurWindow import GlobalBlur
import core
from core_tools.keybinder import QtKeyBinder

def resource_path(relative: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relative)

def add_font(file_name):
    font_path = os.path.join("fonts", f"{file_name}.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)

    if font_id == -1:
        print("Шрифт не загружен! Проверьте путь:", font_path)
    else:
        families = QFontDatabase.applicationFontFamilies(font_id)
        print("Загружен шрифт:", families)

class TrayMenu(QtWidgets.QMenu):
    def __init__(self):
        super().__init__()
        show_action = QAction("Показать", self)
        show_action.triggered.connect(self.on_show_action_pressed)

        settings_action = QAction("Настройки", self)

        exit_action = QAction("Закрыть", self)
        exit_action.triggered.connect(self.on_exit_action_activate)

        self.addAction(show_action)
        self.addAction(settings_action)
        self.addAction(exit_action)

        open_shortcut = QShortcut(QKeySequence("Ctrl+Shift+Space"), self)
        open_shortcut.activated.connect(self.on_show_action_pressed)

    def on_exit_action_activate(self):
        sys.exit()

    def on_show_action_pressed(self):
        mw.show_window()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self._blur_applied = False

        self.setup_hotkey()

        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(resource_path("terminal.png")))

        tray_menu = TrayMenu()

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.tray_icon.show()


        self.setStyleSheet("""
            background-color: qradialgradient(
                cx: 0.5, cy: 0.5, radius: 0.5,
                fx: 0.5, fy: 0.5,
                stop: 0 rgba(0, 0, 0, 102),
                stop: 1 rgba(0, 0, 0, 190)
            );
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setFixedSize(960, 85)
        self.line_edit.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,
                                QtWidgets.QSizePolicy.Policy.Fixed)
        self.line_edit.setPlaceholderText("Type !help to get help")
        self.line_edit.setStyleSheet("""
            QLineEdit {
                background-color: rgb(56, 56, 56);
                border: 3px solid rgb(44, 44, 44);
                border-radius: 25px;
                padding-left: 25px;
                color: rgb(220, 220, 220);
                font-size: 24px;
                font-family: IBM Plex Mono;
            }
            QLineEdit:focus {
                border: 3px solid rgb(44, 44, 44);
            }
        """)
        self.line_edit.returnPressed.connect(self.on_enter_press)


        hello_label = QtWidgets.QLabel()
        hello_label_text = f"Hello {os.getlogin()}!"
        hello_label.setText(hello_label_text)
        hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hello_label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 0);
                color: rgb(255, 255, 255);
                font-size: 64px;
                font-family: IBM Plex Mono SemiBold;
            }
        """)

        compliment_label = QtWidgets.QLabel()
        compliment_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        compliment_label.setStyleSheet("""
                    QLabel {
                        background-color: rgba(0, 0, 0, 0);
                        color: rgb(190, 190, 190);
                        font-size: 40px;
                        font-family: IBM Plex Mono SemiBold;
                    }
                """)
        compliment_label.setText("It's good day for <span style='color:white;'>commit</span> your code")

        layout.addWidget(hello_label)
        layout.addWidget(compliment_label)
        layout.addWidget(self.line_edit, alignment=Qt.AlignmentFlag.AlignHCenter)

    def on_enter_press(self):
        text = self.line_edit.text()
        self.line_edit.clear()
        core.input_data(text)
        self.hide()

    def on_tray_icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show_window()

    def showEvent(self, event):
        super().showEvent(event)
        if not self._blur_applied:
            GlobalBlur(self.winId(), Dark=False, QWidget=self)
            self._blur_applied = True

    def setup_hotkey(self):
        self.key_binder = QtKeyBinder(win_id=None)
        self.key_binder.register_hotkey("Ctrl+Space", self._on_hotkey_triggered)

    def _on_hotkey_triggered(self):
        QMetaObject.invokeMethod(
            self,
            "show_window",
            Qt.ConnectionType.QueuedConnection
        )

    @Slot()
    def show_window(self):
        self.setWindowState(Qt.WindowState.WindowNoState)
        self.showMaximized()
        self.raise_()
        self.activateWindow()

    def event(self, event, /):
        if event.type() == QEvent.Type.WindowDeactivate:
            self.hide()

        return super().event(event)


    def closeEvent(self, event, /):
        self.hide()
        event.ignore()

def start() -> None:
    app = QtWidgets.QApplication(sys.argv)
    add_font("IBMPlexMono-Regular")
    add_font("IBMPlexMono-SemiBold")

    global mw
    mw = MainWindow()

    sys.exit(app.exec())