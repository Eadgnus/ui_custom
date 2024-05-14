from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtCore import Qt, QRect

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.start_point = None
        self.end_point = None
        self.moving_point = None
        self.setWindowTitle("Drag to draw a rectangle")
        self.setGeometry(100, 100, 800, 600)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_point = event.globalPosition().toPoint()
            self.end_point = None  # Reset end point on new press
            self.update()  # Trigger paint event

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.start_point:
            self.moving_point = event.globalPosition().toPoint()
            self.update()  # Trigger paint event

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self.start_point:
            self.end_point = event.globalPosition().toPoint()
            print(f"클릭함: {self.start_point} - 뗌: {self.end_point}")
            self.update()  # Trigger final paint event

    def paintEvent(self, event):
        if self.start_point and self.moving_point:
            rect = QRect(self.start_point, self.moving_point)
            painter = QPainter(self)
            painter.drawRect(rect)

if __name__ == '__main__':
    app = QApplication([])
    viewer = ImageViewer()
    viewer.show()
    app.exec()
