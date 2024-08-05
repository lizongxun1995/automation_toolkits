import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QMouseEvent, QPainter, QColor, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowOpacity(0.45)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()
        self.start_position = ()
        self.end_position = ()
        self._draw = False

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
            qp.drawText(x1, y1, f'{x1},{y1}')
            qp.drawText(x2, y2, f'{x2},{y2}')
            qp.end()
        if self.start_position != () and self.end_position == ():
            x1 = self.start_position[0]
            y1 = self.start_position[1]
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(168, 34, 3))
            qp.drawText(x1, y1, f'{x1},{y1}')

    def get_ori(self):

        return self.start_position, self.end_position


def get_ori():
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
    return w.get_ori()


if __name__ == '__main__':
    print(get_ori())
