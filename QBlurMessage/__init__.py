import os
import sys

from qtpy import QtWidgets
from qtpy.QtCore import Qt
from qtpy.QtGui import QFontDatabase
from qtpy.QtWidgets import QWidget

from BlurWindow.blurWindow import GlobalBlur


def add_font(file_name):
    font_path = os.path.join("fonts", f"{file_name}.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)

    if font_id == -1:
        print("Шрифт не загружен! Проверьте путь:", font_path)
    else:
        families = QFontDatabase.applicationFontFamilies(font_id)
        print("Загружен шрифт:", families)


class QBlurMessage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    add_font("IBMPlexMono-Regular")
    add_font("IBMPlexMono-SemiBold")

    message = QBlurMessage()

    sys.exit(app.exec())