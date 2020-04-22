# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 15:11
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : test.py
# @Software: PyCharm
# QListWidget 控件使用
from PyQt5 import QtCore, QtGui, QtWidgets


#
class CheckableComboBox(QtWidgets.QComboBox):

    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

    def getCheckItem(self):
        # getCheckItem可以获得选择的项目text
        checkedItems = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == QtCore.Qt.Checked:
                checkedItems.append(item.text())
        return checkedItems

    def checkedItems(self):
        checkedItems = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == QtCore.Qt.Checked:
                checkedItems.append(item)
        return checkedItems
