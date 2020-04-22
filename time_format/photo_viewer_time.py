# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 11:42
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : photo_viewer_time.py
# @Software: PyCharm

from PyQt5.QtGui import QBrush, QPixmap, QColor
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFrame
from PyQt5.QtCore import QPoint, pyqtSignal, Qt, QRectF


class PhotoViewer(QGraphicsView):
    # 分别传递鼠标点击，移动，松开信号
    mouse_clicked = pyqtSignal(QPoint)
    mouse_moved = pyqtSignal(QPoint)
    mouse_released = pyqtSignal(QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self.init_UI()

    def init_UI(self):

        self._zoom = 0  # 定义图片的放大级别
        self._empty = True  # 定义是否含有图片（点击模式和拖动模式切换）
        self._contour = False  # 定义轮廓拖动模式 0
        self._ocr = False  # 定义文字识别模式

        self._scene = QGraphicsScene(self)  # 新建一个场景
        self._photo = QGraphicsPixmapItem()  # 新建一个图像图元
        self._scene.addItem(self._photo)  # 图像图元添加到场景中
        self.setScene(self._scene)  # 场景添加到视图中
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)  # 坐标转换时以鼠标所在位置为中心
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)  # 视图大小调整时该如何定位其中的场景
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 垂直滚动条关闭
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 平行滚动条关闭
        self.setBackgroundBrush(QBrush(QColor(30, 30, 30)))  # 背景色
        self.setFrameShape(QFrame.NoFrame)  # 设置QFrame在它的内容周围画一个框

    def hasPhoto(self):
        # 是否加载图片
        return not self._empty

    def fitInView(self, scale=True):
        # 图片自适应函数，缩放模式开启
        rect = QRectF(self._photo.pixmap().rect())  # 绘制图元大小的矩形
        if not rect.isNull():
            self.setSceneRect(rect)  # 这个矩形限定了场景的范围
            if self.hasPhoto():
                unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        # 加载和重新渲染图元
        # self._zoom = 0 # 重新渲染的时候保持放大比例，并不初始化为_zoom为0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QGraphicsView.NoDrag)
            self._photo.setPixmap(QPixmap())

        # 是否从新适应
        # self.fitInView()

    def wheelEvent(self, event):
        # 鼠标滚轮控制放大缩小
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        # 鼠标拖动和点击及切换函数
        if self._contour or self._ocr:
            self.setDragMode(QGraphicsView.NoDrag)
        else:
            if self.dragMode() == QGraphicsView.ScrollHandDrag:
                self.setDragMode(QGraphicsView.NoDrag)
            elif not self._photo.pixmap().isNull():
                self.setDragMode(QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        # 鼠标点击返回鼠标所在的图片坐标
        if self._photo.isUnderMouse():
            # 注意坐标系转换 详解http://blog.51cto.com/9291927/1879128
            p = self._photo.mapToItem(self._photo, self.mapToScene(event.pos()))
            self.mouse_clicked.emit(p.toPoint())
        super(PhotoViewer, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._ocr == True:  # 只有当文字识别的时候实时返回拖动的鼠标的坐标
            if self._photo.isUnderMouse():
                p = self._photo.mapToItem(self._photo, self.mapToScene(event.pos()))
                self.mouse_moved.emit(p.toPoint())
        super(PhotoViewer, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # 获取鼠标松开的坐标点
        if self._photo.isUnderMouse():
            p = self._photo.mapToItem(self._photo, self.mapToScene(event.pos()))
            self.mouse_released.emit(p.toPoint())
        super(PhotoViewer, self).mouseReleaseEvent(event)
