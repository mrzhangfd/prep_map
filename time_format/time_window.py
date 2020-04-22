# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 9:57
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : time_window.py
# @Software: PyCharm
from datetime import datetime
from math import atan2
from PIL import Image, ImageDraw, ImageFont
from pickle import loads
import numpy as np
import sxtwl
import re
import json
import cv2 as cv
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QPen
from PyQt5.QtWidgets import QComboBox, QLabel, QWidget, QLineEdit, QApplication, QHBoxLayout, QPushButton, QVBoxLayout, \
    QCheckBox, QListView, QListWidget
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QStringListModel
from photo_viewer_time import PhotoViewer
from mysql_conn_time import MySqlConn
from test import CheckableComboBox
import PyQt5_stylesheets

# 日历的中文索引
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
        "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九",
       "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

lunar = sxtwl.Lunar()  # 实例化日历库
filename = "timeInfo"
filename_eve = "json/eventInfo"
person_obj = "json/perInfo"
contour_points = []


class CustomComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # 底图和地点模式
        self.choose_sites_set = []
        self.perFlag = False
        self.eve_clicked = ""
        self.eveSite_dict = {}
        self.year_click_flag = False
        self.clickedyear = 0
        self.baseMap_flag = True
        self.site_flag = False
        self.site_dc = {}
        self.eve_list = []
        self.choose_sites = []
        self.choose_year = ''
        # 记录公历时间

        # 第一行信息
        self.lable = QLabel("查询类型：", self)
        format_list = ["公历时间", "农历时间", "纪年时间", "儒略日", "事件对象", "人物对象"]

        self.combox = QComboBox(self)
        self.combox.addItems(format_list)
        self.combox.activated.connect(self.time_format)

        self.textLine = QLineEdit(self)
        self.textLine.setPlaceholderText("公历时间 例：2019-1-1")

        self.transButton = QPushButton("查询  ", self)
        self.transButton.clicked.connect(self.swift)

        self.label = QLabel("生肖  ", self)
        self.labelText = QLineEdit(self)

        self.label1 = QLabel("公历时间", self)
        self.labelText1 = QLineEdit(self)

        self.label2 = QLabel("农历时间", self)
        self.labelText2 = QLineEdit(self)

        self.label3 = QLabel("年号时间", self)
        self.labelText3 = QLineEdit(self)

        self.label4 = QLabel("干支时间", self)
        self.labelText4 = QLineEdit(self)

        self.label5 = QLabel("儒略日", self)
        self.labelText5 = QLineEdit(self)

        self.eve_listView = QListView(self)
        self.eve_detail = QListWidget()
        self.eve_detail.setFixedHeight(25)
        self.eve_detail.itemClicked.connect(self.year_click)
        self.eve_detail.setFlow(QListView.LeftToRight)
        self.viewer = PhotoViewer(self)

        # 总布局
        v_layout = QVBoxLayout(self)

        # 左上角布局
        v_layout_1 = QVBoxLayout()
        # 右上角布局
        v_layout_2 = QVBoxLayout()

        h_layout_top = QHBoxLayout()

        h_layout = QHBoxLayout(self)
        h_layout.addWidget(self.lable)
        h_layout.addWidget(self.combox)
        h_layout.addWidget(self.textLine)
        h_layout.addWidget(self.transButton)

        h_layout_ru = QHBoxLayout(self)
        h_layout_ru.addWidget(self.label5)
        h_layout_ru.addWidget(self.labelText5)

        h_layout_2 = QHBoxLayout(self)
        h_layout_2.addWidget(self.label)
        h_layout_2.addWidget(self.labelText)

        h_layout_3 = QHBoxLayout(self)
        h_layout_3.addWidget(self.label1)
        h_layout_3.addWidget(self.labelText1)

        h_layout_4 = QHBoxLayout(self)
        h_layout_4.addWidget(self.label2)
        h_layout_4.addWidget(self.labelText2)

        h_layout_5 = QHBoxLayout(self)
        h_layout_5.addWidget(self.label3)
        h_layout_5.addWidget(self.labelText3)

        h_layout_6 = QHBoxLayout(self)
        h_layout_6.addWidget(self.label4)
        h_layout_6.addWidget(self.labelText4)

        v_layout_1.addLayout(h_layout)
        v_layout_1.addLayout(h_layout_ru)
        v_layout_1.addLayout(h_layout_2)
        v_layout_1.addLayout(h_layout_3)
        v_layout_1.addLayout(h_layout_4)
        v_layout_1.addLayout(h_layout_5)
        v_layout_1.addLayout(h_layout_6)

        v_layout_2.addWidget(self.eve_listView)
        v_layout_2.addWidget(self.eve_detail)
        h_layout_top.addLayout(v_layout_1)
        h_layout_top.addLayout(v_layout_2)

        v_layout.addLayout(h_layout_top)

        self.qLabel = QLabel("选中轮廓")
        self.qlineText = QLineEdit(self)
        self.combox_checkBox = CheckableComboBox()
        self.checkBoxButton = QPushButton(self)
        self.checkBoxButton.setText("确定")
        self.checkBoxButton.clicked.connect(self.draw_contour_points)

        self.cb1 = QCheckBox("Base map")
        self.cb1.setChecked(True)
        self.cb1.stateChanged.connect(self.cb1Change)
        self.cb2 = QCheckBox("site")
        self.cb2.stateChanged.connect(self.cb2Change)

        h_layout_7 = QHBoxLayout(self)
        h_layout_7.addWidget(self.qLabel)
        h_layout_7.addWidget(self.qlineText)
        h_layout_7.addWidget(self.combox_checkBox)
        h_layout_7.addWidget(self.checkBoxButton)
        h_layout_7.setStretchFactor(self.qlineText, 20)
        h_layout_7.setStretchFactor(self.combox_checkBox, 5)
        h_layout_7.setStretchFactor(self.checkBoxButton, 1)
        h_layout_8 = QHBoxLayout(self)
        h_layout_8.addStretch()
        h_layout_8.addWidget(self.cb1)
        h_layout_8.addWidget(self.cb2)

        v_layout.addWidget(self.viewer)
        v_layout.addLayout(h_layout_7)
        v_layout.addLayout(h_layout_8)

        v_layout.setStretchFactor(h_layout_top, 1)
        v_layout.setStretchFactor(self.viewer, 5)

        app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_gray"))
        self.setGeometry(500, 300, 800, 600)
        self.setWindowTitle('时空框架')
        self.show()

    def time_format(self):
        if self.combox.currentText() == "公历时间":
            self.textLine.setPlaceholderText("公历时间 例：2019-1-1")
        elif self.combox.currentText() == "农历时间":
            self.textLine.setPlaceholderText("农历时间 例：2019-1-1")
        elif self.combox.currentText() == "纪年时间":
            self.textLine.setPlaceholderText("纪年时间 例：唐-贞观-3年")
        elif self.combox.currentText() == "儒略日":
            self.textLine.setPlaceholderText("儒略日 例：18963")
        elif self.combox.currentText() == "事件对象":
            self.textLine.setPlaceholderText("事件对象 例：班超出使西域")
        else:
            self.textLine.setPlaceholderText("人物对象 例：宋-苏轼")

    def eve_input(self):
        eve_string = self.textLine.text()
        with open(filename_eve, encoding='utf-8') as f:
            eveList = json.load(f)
        for eventItem in eveList:
            if eve_string in eventItem["event"]:
                self.clickedyear = str(eventItem["eve_start"])
                self.year_click_flag = True
                break

    def person_input(self):
        per_string = self.textLine.text()
        with open(person_obj, encoding='utf-8') as f:
            personList = json.load(f)
        for personItem in personList:
            if per_string == personItem["name"]:
                self.clickedyear = str(personItem["start"])
                self.year_click_flag = True
                break

    def swift(self):
        if self.combox.currentText() == "公历时间":
            self.input_calendar()
            self.perFlag = False
        elif self.combox.currentText() == "农历时间":
            self.perFlag = False
            self.lunar_input()
        elif self.combox.currentText() == "事件对象":
            self.perFlag = False
            self.eve_input()
            self.input_calendar()
        elif self.combox.currentText() == "人物对象":
            self.perFlag = True
            self.person_input()
            self.input_calendar()
        elif self.combox.currentText() == "儒略日":
            self.rulue()
        else:
            self.perFlag = False
            self.naohao_input()
        conn = MySqlConn()
        result = conn.img_select(self.choose_year)[0]
        print(self.choose_year)
        f = open('img\\' + self.choose_year + ".jpg", "wb")
        f.write(result)
        f.close()
        image = QImage.fromData(result)
        pixmap = QPixmap.fromImage(image)
        self.viewer.setPhoto(pixmap)
        self.viewer.fitInView()
        year_change = conn.year_change(self.choose_year)
        contours_name = conn.contours_select(year_change[0])
        self.combox_checkBox.clear()
        for index, element in enumerate(contours_name):
            self.combox_checkBox.addItem(element)
            item = self.combox_checkBox.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        year_int = int(self.choose_year)
        event_list_year = self.eve_show(year_int)
        self.eve_list = event_list_year
        slm = QStringListModel()
        slm.setStringList(event_list_year)
        self.eve_listView.setModel(slm)
        self.eve_listView.clicked.connect(self.eveClick)

    def cb1Change(self):
        if self.cb1.checkState() == Qt.Checked:
            self.baseMap_flag = True
        elif self.cb1.checkState() == Qt.Unchecked:
            self.baseMap_flag = False

    def cb2Change(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(False)
            self.site_flag = False
        elif self.cb1.checkState() == Qt.Unchecked:
            if self.cb2.checkState() == Qt.Checked:
                self.site_flag = True
            elif self.cb2.checkState() == Qt.Unchecked:
                self.site_flag = False

    def draw_contour_points(self):
        self.eveSite_dict = {}
        text = ''
        cntList = []
        contours_list = self.combox_checkBox.getCheckItem()
        conn = MySqlConn()
        for contour in contours_list:
            text = text + contour + ","
            year_change = conn.year_change(self.choose_year)
            cntB = conn.contour_points(year_change[0], contour)
            cntA = loads(cntB[0][0])
            cntList.append(cntA)
        self.qlineText.setText(text)
        imgb = cv.imread("img/" + self.choose_year + ".jpg")

        imgB = cv.medianBlur(imgb, 71)
        if self.baseMap_flag:
            img_contour = cv.drawContours(imgB.copy(), cntList, -1, (255, 255, 255), 3)
        elif not self.baseMap_flag:
            background = np.ones(imgB.shape, np.uint8) * 255
            img_contour = cv.drawContours(background.copy(), cntList, -1, (0, 0, 255), 2)
        image_height, image_width, image_depth = img_contour.shape
        QIm = cv.cvtColor(img_contour, cv.COLOR_BGR2RGB)
        pil_im = Image.fromarray(QIm)
        icon = Image.open("img/icon.png")
        site = Image.open("img/site.png")
        if self.site_flag:
            site_list = self.site_show(self.choose_year, contours_list)
            for key, value in site_list.items():
                draw = ImageDraw.Draw(pil_im)
                l_value = int(value[0]) // 2
                font = ImageFont.truetype("font/simfang.ttf", 15, encoding="utf-8")
                c_value = value[1].split(",", 1)
                x_l = float(c_value[0][1:].rstrip())
                y_l = float(c_value[1][:-1].rstrip())
                icon_x = int(0.8 * l_value)
                icon_y = int(0.5 * l_value)
                y_2 = y_l - icon_y
                x_2 = x_l + 0.6 * icon_x
                x_3 = x_2 + 6
                y_3 = y_2 - 10
                icon = icon.resize((icon_x, icon_y), Image.ANTIALIAS)
                r, g, b, a = icon.split()
                pil_im.paste(icon, (int(x_2), int(y_2)), mask=a)
                if key in self.choose_sites:
                    mark = self.choose_sites.index(key) + 1
                    self.eveSite_dict[mark] = (x_2, y_2)
                    site = site.resize((10, 10), Image.ANTIALIAS)
                    r1, g1, b1, a1 = site.split()
                    pil_im.paste(site, (int(x_3), int(y_3)), mask=a1)
                    draw.text((x_l, y_l), (str(mark) + key), (255, 255, 255), font=font)
                else:
                    draw.text((x_l, y_l), key, (0, 0, 0), font=font)
        for i in range(1, len(self.eveSite_dict)):
            value1 = self.eveSite_dict[i]
            value2 = self.eveSite_dict[i + 1]
            draw.line((value1[0], value1[1], value2[0], value2[1]), fill=(150, 150, 255), width=5)
        QIm = np.array(pil_im)
        QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth,
                     QImage.Format_RGB888)
        self.viewer.setPhoto(QPixmap.fromImage(QIm))

    def draw_contour_points_new(self):
        self.eveSite_dict = {}
        text = ''
        cntList = []
        contours_list = self.combox_checkBox.getCheckItem()
        conn = MySqlConn()
        for contour in contours_list:
            text = text + contour + ","
            year_change = conn.year_change(self.choose_year)
            cntB = conn.contour_points(year_change[0], contour)
            cntA = loads(cntB[0][0])
            cntList.append(cntA)
        self.qlineText.setText(text)
        imgb = cv.imread("img/" + self.choose_year + ".jpg")

        imgB = cv.medianBlur(imgb, 71)
        if self.baseMap_flag:
            img_contour = cv.drawContours(imgB.copy(), cntList, -1, (255, 255, 255), 3)
        elif not self.baseMap_flag:
            background = np.ones(imgB.shape, np.uint8) * 255
            img_contour = cv.drawContours(background.copy(), cntList, -1, (0, 0, 255), 2)
        image_height, image_width, image_depth = img_contour.shape
        QIm = cv.cvtColor(img_contour, cv.COLOR_BGR2RGB)
        pil_im = Image.fromarray(QIm)
        icon = Image.open("img/icon.png")
        site = Image.open("img/site.png")
        if self.site_flag:
            site_list = self.site_show(self.choose_year, contours_list)
            for key, value in site_list.items():
                draw = ImageDraw.Draw(pil_im)
                l_value = int(value[0]) // 2
                font = ImageFont.truetype("font/simfang.ttf", 15, encoding="utf-8")
                c_value = value[1].split(",", 1)
                x_l = float(c_value[0][1:].rstrip())
                y_l = float(c_value[1][:-1].rstrip())
                icon_x = int(0.8 * l_value)
                icon_y = int(0.5 * l_value)
                y_2 = y_l - icon_y
                x_2 = x_l + 0.6 * icon_x
                x_3 = x_2 + 6
                y_3 = y_2 - 10
                icon = icon.resize((icon_x, icon_y), Image.ANTIALIAS)
                r, g, b, a = icon.split()
                pil_im.paste(icon, (int(x_2), int(y_2)), mask=a)
                print(self.choose_sites_set)
                if key in self.choose_sites_set:
                    mark = self.choose_sites_set.index(key) + 1
                    site = site.resize((10, 10), Image.ANTIALIAS)
                    r1, g1, b1, a1 = site.split()
                    pil_im.paste(site, (int(x_3), int(y_3)), mask=a1)
                    draw.text((x_l, y_l), (str(mark) + key), (255, 255, 255), font=font)
                else:
                    draw.text((x_l, y_l), key, (0, 0, 0), font=font)
            for index, item in enumerate(self.choose_sites):
                mysite = conn.site_select_one(self.choose_year, item)
                l_value = int(mysite[1]) // 2
                icon_x = int(0.8 * l_value)
                icon_y = int(0.5 * l_value)
                c_value_new = mysite[2].split(",", 1)
                a = float(c_value_new[0][1:].rstrip())
                b = float(c_value_new[1][:-1].rstrip())
                b = b - icon_y
                a = a + 0.6 * icon_x
                self.eveSite_dict[index] = (a, b)
            for i in range(len(self.eveSite_dict) - 1):
                value1 = self.eveSite_dict[i]
                value2 = self.eveSite_dict[i + 1]
                angle = atan2((value1[1] - value2[1]), (value1[0] - value2[0]))
                x_u = value2[0] + 10 * np.cos(angle + 3.14 * 25 / 180)
                y_u = value2[1] + 10 * np.sin(angle + 3.14 * 25 / 180)
                x_l = value2[0] + 10 * np.cos(angle - 3.14 * 25 / 180)
                y_l = value2[1] + 10 * np.sin(angle - 3.14 * 25 / 180)

                draw.line((value1[0], value1[1], value2[0], value2[1]), fill=(153, 51, 255), width=2)
                draw.line((x_u, y_u, value2[0], value2[1]), fill=(255, 255, 255), width=2)
                draw.line((x_l, y_l, value2[0], value2[1]), fill=(255, 255, 255), width=2)
        QIm = np.array(pil_im)
        QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth,
                     QImage.Format_RGB888)
        self.viewer.setPhoto(QPixmap.fromImage(QIm))

    def site_show(self, chosse_year, sites_contour):
        self.site_dc = {}
        conn = MySqlConn()
        for item in sites_contour:
            year_change = conn.year_change(chosse_year)
            result = conn.site_select(year_change[0], item)
            for item in result:
                key = item[0]
                value = [item[1], item[2]]
                self.site_dc[key] = value
        return self.site_dc

    def eve_show(self, choose_year):
        eveList_year = []
        if self.perFlag == True:
            with open(person_obj, encoding='utf-8') as f:
                perList = json.load(f)
                for perItem in perList:
                    pStart = perItem["start"]
                    pEnd = perItem["end"]
                    if pStart <= choose_year and pEnd >= choose_year:
                        choose_event = perItem["name"]
                        eveList_year.append(choose_event)
        else:
            with open(filename_eve, encoding='utf-8') as f:
                eveList = json.load(f)
                for eventItem in eveList:
                    eStart = eventItem["eve_start"]
                    eEnd = eventItem["eve_end"]
                    if eStart <= choose_year and eEnd >= choose_year:
                        choose_event = eventItem["event"]
                        eveList_year.append(choose_event)
        return eveList_year

    def eveClick(self, qModelIndex):
        self.eve_detail.clear()
        self.choose_sites = []
        self.eve_clicked = self.eve_list[qModelIndex.row()]

        if self.perFlag == True:
            with open(person_obj, encoding='utf-8') as f:
                personList = json.load(f)
            for perItem in personList:
                if perItem["name"] == self.eve_clicked:
                    details = perItem["details"]
                    for item in details:
                        time = item["time"]
                        self.eve_detail.addItem(str(time))
                        if item["time"] == int(self.choose_year):
                            self.choose_sites = item["sites"]
        else:
            with open(filename_eve, encoding='utf-8') as f:
                eveList = json.load(f)
            for eventItem in eveList:
                if eventItem["event"] == self.eve_clicked:
                    details = eventItem["details"]
                    for item in details:
                        time = item["time"]
                        self.eve_detail.addItem(str(time))
                        if item["time"] == int(self.choose_year):
                            self.choose_sites = item["sites"]
        self.eve_detail.addItem("all")
        self.draw_contour_points()

    def year_click(self, item):
        if self.perFlag == True:
            if item.text() == "all":
                all_list = []
                self.choose_sites = []
                with open(person_obj, encoding='utf-8') as f:
                    eveList = json.load(f)
                for eventItem in eveList:
                    if eventItem["name"] == self.eve_clicked:
                        details = eventItem["details"]
                        for myitem in details:
                            all_list = all_list + myitem["sites"]
                print(all_list)
                self.choose_sites = list(set(all_list))
                self.choose_sites.sort(key=all_list.index)
                # print(self.choose_sites)
                self.draw_contour_points()
            else:
                self.choose_sites = []
                with open(filename_eve, encoding='utf-8') as f:
                    eveList = json.load(f)
                for eventItem in eveList:
                    if eventItem["event"] == self.eve_clicked:
                        details = eventItem["details"]
                        for myitem in details:
                            if str(myitem["time"]) == item.text():
                                self.choose_sites = myitem["sites"]
                self.draw_contour_points()
                self.clickedyear = item.text()
        else:
            if item.text() == "all":
                all_list = []
                self.choose_sites = []
                self.choose_sites_set = []
                with open(filename_eve, encoding='utf-8') as f:
                    eveList = json.load(f)
                for eventItem in eveList:
                    if eventItem["event"] == self.eve_clicked:
                        details = eventItem["details"]
                        for myitem in details:
                            all_list = all_list + myitem["sites"]
                # print(self.choose_sites)
                self.choose_sites = all_list
                self.choose_sites_set = list(set(all_list))
                self.choose_sites_set.sort(key=all_list.index)
                # print(self.choose_sites)
                self.draw_contour_points_new()
            else:
                self.choose_sites = []
                self.choose_sites_set = []
                with open(filename_eve, encoding='utf-8') as f:
                    eveList = json.load(f)
                for eventItem in eveList:
                    if eventItem["event"] == self.eve_clicked:
                        details = eventItem["details"]
                        for myitem in details:
                            if str(myitem["time"]) == item.text():
                                self.choose_sites = myitem["sites"]
                self.choose_sites_set = list(set(self.choose_sites))
                self.choose_sites_set.sort(key=self.choose_sites.index)
                self.draw_contour_points_new()
                self.clickedyear = item.text()
            # self.year_click_flag = True

    def gyjn(self, year):
        if year >= 1:
            year = year
        elif year <= 0:
            year = year - 1
        return year

    def rulue(self):
        JD = self.textLine.text()
        JD = float(JD) + 0.5
        Z = int(JD)
        if Z < 2299161:  # 儒略历
            A = Z
        else:  # 格里历
            a = int((Z - 2305447.5) / 36524.25)
            A = Z + 10 + a - int(a / 4)
        B = A + 1524
        C = int((B - 122.1) / 365.25)
        D = int(365.25 * C)
        E = int((B - D) / 30.6001)
        d = B - D - int(30.6001 * E)
        if E < 14:
            m = E - 1
        elif E < 16:
            m = E - 13
        if m > 2:
            year = C - 4716
        elif m in [1, 2]:
            year = C - 4715
        y = self.gyjn(year)
        self.choose_year = str(y)
        day = lunar.getDayBySolar(int(y), int(m), int(d))
        gongli = str(day.y) + "-" + str(day.m) + "-" + str(day.d)
        print(gongli)
        if day.Lleap:
            nongli = "润" + ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
        else:
            nongli = ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
        ganzhi = Gan[day.Lyear2.tg] + Zhi[day.Lyear2.dz] + "年" + Gan[day.Lmonth2.tg] + Zhi[day.Lmonth2.dz] + "月" + \
                 Gan[day.Lday2.tg] + Zhi[day.Lday2.dz] + "日"
        year = lunar.getYearCal(y)
        Shx = ShX[year.ShX]
        nianhao = self.queryEmperorYear(y)

        rulue = sxtwl.J2000 + day.d0

        self.labelText.setText(Shx)
        self.labelText1.setText(gongli)
        self.labelText2.setText(nongli)
        self.labelText3.setText(nianhao)
        self.labelText4.setText(ganzhi)
        self.labelText5.setText(str(rulue) + "日")

    def input_calendar(self):
        symbol = '年月日 \/.'
        if self.year_click_flag == True:
            date_string = self.clickedyear
            # self.textLine.setText(date_string)
        else:
            date_string = self.textLine.text()
        date_list = self.go_split(date_string, symbol)

        if len(date_list) == 3:
            y = int(date_list[0])
            self.choose_year = str(y)
            m = int(date_list[1])
            d = int(date_list[2])
            day = lunar.getDayBySolar(y, m, d)
            gongli = str(day.y) + "-" + str(day.m) + "-" + str(day.d)
            if day.Lleap:
                nongli = "润" + ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
            else:
                nongli = ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
            ganzhi = Gan[day.Lyear2.tg] + Zhi[day.Lyear2.dz] + "年" + Gan[day.Lmonth2.tg] + Zhi[day.Lmonth2.dz] + "月" + \
                     Gan[day.Lday2.tg] + Zhi[day.Lday2.dz] + "日"
            year = lunar.getYearCal(y)
            Shx = ShX[year.ShX]
            nianhao = self.queryEmperorYear(y)
            rulue = sxtwl.J2000 + day.d0

        elif len(date_list) == 2:
            y = int(date_list[0])
            self.choose_year = str(y)
            m = int(date_list[1])
            month = sxtwl.Lunar().yueLiCalc(y, m)
            gongli = date_string
            nongli = "条件不足"
            ganzhi = Gan[month.yearGan] + Zhi[month.yearZhi] + "年"
            Shx = ShX[month.ShX]
            nianhao = self.queryEmperorYear(y)
            rulue = "未知"

        elif len(date_list) == 1:
            y = int(date_list[0])
            self.choose_year = str(y)
            year = lunar.getYearCal(y)
            print(y)
            gongli = date_string
            nongli = "条件不足"
            ganzhi = Gan[year.yearGan] + Zhi[year.yearZhi] + "年"
            Shx = ShX[year.ShX]
            nianhao = self.queryEmperorYear(y)
            rulue = "未知"

        else:
            Shx = "未知"
            gongli = "未知"
            nongli = "未知"
            nianhao = "未知"
            ganzhi = "未知"
            rulue = "未知"
        self.labelText.setText(Shx)
        self.labelText1.setText(gongli)
        self.labelText2.setText(nongli)
        self.labelText3.setText(nianhao)
        self.labelText4.setText(ganzhi)
        self.labelText5.setText(str(rulue) + "日")

    def lunar_input(self):
        symbol = '年月日 /'
        date_string = self.textLine.text()
        date_list = self.go_split(date_string, symbol)

        if len(date_list) == 3:
            y = int(date_list[0])
            m = int(date_list[1])
            d = int(date_list[2])
            day = lunar.getDayByLunar(y, m, d)
            gongli = str(day.y) + "-" + str(day.m) + "-" + str(day.d)
            self.choose_year = str(day.y)
            if day.Lleap:
                nongli = "润" + ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
            else:
                nongli = ymc[day.Lmc] + "月" + rmc[day.Ldi] + "日"
            ganzhi = Gan[day.Lyear2.tg] + Zhi[day.Lyear2.dz] + "年" + Gan[day.Lmonth2.tg] + Zhi[day.Lmonth2.dz] + "月" + \
                     Gan[day.Lday2.tg] + Zhi[day.Lday2.dz] + "日"
            year = lunar.getYearCal(y)
            Shx = ShX[year.ShX]
            nianhao = self.queryEmperorYear(y)
        else:
            Shx = "未知"
            gongli = "未知"
            nongli = date_string
            nianhao = "未知"
            ganzhi = "未知"

        self.labelText.setText(Shx)
        self.labelText1.setText(gongli)
        self.labelText2.setText(nongli)
        self.labelText3.setText(nianhao)
        self.labelText4.setText(ganzhi)

    def queryDateByEmporerYear(self, strs):
        if "元" in strs:
            year_offset = 1
        else:
            year_offset = re.findall("\d+", strs)[0]
        with open(filename, encoding='utf-8') as f:
            dynasty = json.load(f)
            dynasty_flag = False
            for mydynasty in dynasty:
                dychoose = mydynasty['dynasty']
                if dychoose in dychoose:
                    dynasty_flag = True
                    regintitleList = mydynasty['children']
                    for myregintitle in regintitleList:
                        reginchoose = myregintitle['reignTitle']
                        if reginchoose in strs:
                            year_list = myregintitle['children']

                            for my_year in year_list:
                                year_start = my_year['start']
                                year = year_start + int(year_offset) - 1

            if not dynasty_flag:
                year = "未录入"

        return year

    def naohao_input(self, ):
        date_string = self.textLine.text()
        y = self.queryDateByEmporerYear(date_string)
        self.choose_year = str(y)
        if y != "未录入":
            year = lunar.getYearCal(y)

        Shx = ShX[year.ShX]
        gongli = str(year.y) + "年"
        nongli = "条件不足"
        nianhao = date_string
        ganzhi = Gan[year.yearGan] + Zhi[year.yearZhi] + "年"

        self.labelText.setText(Shx)
        self.labelText1.setText(gongli)
        self.labelText2.setText(nongli)
        self.labelText3.setText(nianhao)
        self.labelText4.setText(ganzhi)

    def go_split(self, str, symbol):
        # 拼接正则表达式
        symbol = "[" + symbol + "]"
        # 一次性分割字符串
        result = re.split(symbol, str)
        # 去除空字符串
        return [x for x in result if x]

    def queryEmperorYear(self, year):
        # 加载的json文件
        with open(filename, encoding='utf-8') as f:
            mydynasty = json.load(f)
            dynasty_flag = False
            for mydate in mydynasty:
                pe_start = mydate['dy_start']
                pre_end = mydate['dy_end']
                if pe_start <= year <= pre_end:
                    dynasty_flag = True
                    dy = mydate['dynasty']
                    reign = mydate['children']
                    for title in reign:

                        mytitle = title['reignTitle']
                        pre_regin = title['children']

                        for myregin in pre_regin:
                            reign_start = myregin['start']
                            reign_end = myregin['end']

                            if reign_start <= year <= reign_end:

                                offset = year - reign_start + 1
                                if offset == 1:
                                    offset = "元"
                                strs = dy + "-" + mytitle + str(offset) + "年\n"
            if not dynasty_flag:
                strs = "该时间未录入"
        return strs

    def showImg(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    timeWindow = CustomComboBox()
    sys.exit(app.exec_())
