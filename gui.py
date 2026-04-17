import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from BlurWindow.blurWindow import GlobalBlur


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.showMaximized()

        GlobalBlur(self.winId(), Dark=False, QWidget=self)

        self.setStyleSheet("""
            background-color: qradialgradient(
                cx: 0.5, cy: 0.5, radius: 0.5,
                fx: 0.5, fy: 0.5,
                stop: 0 rgba(0, 0, 0, 102),
                stop: 1 rgba(0, 0, 0, 190)
            );
        """)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())