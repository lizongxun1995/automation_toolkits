import ctypes
import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QMouseEvent, QPainter, QColor, QFont, QGuiApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0.45)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()
        self.start_position = ()
        self.end_position = ()
        app_width = QGuiApplication.primaryScreen().geometry().size().width()
        user32 = ctypes.windll.user32
        # 单显示器屏幕宽度和高度:
        screen_size0 = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        screen_width = screen_size0[0]

        self._rate = screen_width / app_width

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == 16777216:
            self.close()

    def mousePressEvent(self, event):
        position = event.position()
        self.start_position = int(position.x()), int(position.y())
        self.update()

    def mouseMoveEvent(self, event):
        position = event.position()
        self.end_position = int(position.x()), int(position.y())
        self.update()

    def mouseReleaseEvent(self, event):
        position = event.position()
        self.end_position = int(position.x()), int(position.y())
        self.close()

    def paintEvent(self, event):
        if self.start_position != () and self.end_position != ():
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(168, 34, 3))
            x1 = self.start_position[0]
            y1 = self.start_position[1]
            x2 = self.end_position[0]
            y2 = self.end_position[1]
            height = y2 - y1
            width = x2 - x1
            qp.drawRect(x1, y1, width, height)
            qp.drawText(x1, y1, f'{int(x1 * self._rate)},{int(y1 * self._rate)}')
            qp.drawText(x2, y2, f'{int(x2 * self._rate)},{int(y2 * self._rate)}')
            qp.end()
        if self.start_position != () and self.end_position == ():
            x1 = self.start_position[0]
            y1 = self.start_position[1]
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(168, 34, 3))
            qp.drawText(x1, y1, f'{int(x1 * self._rate)},{int(y1 * self._rate)}')

    def get_ori(self):
        (x1, y1), (x2, y2) = self.start_position, self.end_position
        return (int(x1 * self._rate), int(y1 * self._rate)), (int(x2 * self._rate), int(y2 * self._rate))


def get_ori():
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
    return w.get_ori()


if __name__ == '__main__':
    print(get_ori())
