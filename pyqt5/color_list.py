# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 21:56
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : color_list.py
# @Software: PyCharm

# hsv列表
from collections import defaultdict
from numpy import array


def get_corlor_list():
    dict = defaultdict(list)

    # 1 red_红色
    lower_1_1 = array([0, 160, 130])
    upper_1_1 = array([9, 255, 255])
    color_list = []
    color_list.append(lower_1_1)
    color_list.append(upper_1_1)
    dict['1_1'] = color_list

    # 粉色_信德——1172
    lower_1_2 = array([0, 100, 120])
    upper_1_2 = array([9, 160, 255])
    color_list = []
    color_list.append(lower_1_2)
    color_list.append(upper_1_2)
    dict['1_2'] = color_list

    # 瓦纳斯 ——1172 褐红
    lower_1_3 = array([0, 160, 90])
    upper_1_3 = array([9, 200, 130])
    color_list = []
    color_list.append(lower_1_3)
    color_list.append(upper_1_3)
    dict['1_3'] = color_list

    # 渤海 757 红
    lower_1_4 = array([6, 90, 125])
    upper_1_4 = array([14, 145, 190])
    color_list = []
    color_list.append(lower_1_4)
    color_list.append(upper_1_4)
    dict['1_4'] = color_list

    # 243
    lower_1_7 = array([0, 60, 80])
    upper_1_7 = array([10, 140, 255])
    color_list = []
    color_list.append(lower_1_7)
    color_list.append(upper_1_7)
    dict['1_7'] = color_list

    # 243 贵霜沙
    lower_1_4 = array([11, 45, 100])
    upper_1_4 = array([42, 125, 255])
    color_list = []
    color_list.append(lower_1_4)
    color_list.append(upper_1_4)
    dict['1_4'] = color_list

    # 室韦都督 757
    lower_1_5 = array([5, 145, 130])
    upper_1_5 = array([14, 185, 175])
    color_list = []
    color_list.append(lower_1_5)
    color_list.append(upper_1_5)
    dict['1_5'] = color_list

    # 瓦纳斯 ——1172 褐红
    lower_1_6 = array([0, 144, 40])
    upper_1_6 = array([20, 255, 140])
    color_list = []
    color_list.append(lower_1_6)
    color_list.append(upper_1_6)
    dict['1_6'] = color_list

    # 2_花剌子模_黄褐色
    lower_2_1 = array([11, 135, 80])
    upper_2_1 = array([25, 200, 200])
    color_list = []
    color_list.append(lower_2_1)
    color_list.append(upper_2_1)
    dict['2_1'] = color_list

    # 533 魏
    lower_2_21 = array([10, 135, 95])
    upper_2_21 = array([16, 255, 255])
    color_list = []
    color_list.append(lower_2_21)
    color_list.append(upper_2_21)
    dict['2_21'] = color_list

    # 吐故浑 533
    lower_2_22 = array([16, 95, 95])
    upper_2_22 = array([27, 200, 200])
    color_list = []
    color_list.append(lower_2_22)
    color_list.append(upper_2_22)
    dict['2_22'] = color_list

    lower_2_14 = array([10, 145, 100])
    upper_2_14 = array([20, 220, 240])
    color_list = []
    color_list.append(lower_2_14)
    color_list.append(upper_2_14)
    dict['2_14'] = color_list

    lower_2_18 = array([15, 62, 110])
    upper_2_18 = array([28, 147, 220])
    color_list = []
    color_list.append(lower_2_18)
    color_list.append(upper_2_18)
    dict['2_18'] = color_list

    # 457 蕨达
    lower_2_13 = array([8, 0, 140])
    upper_2_13 = array([63, 60, 255])
    color_list = []
    color_list.append(lower_2_13)
    color_list.append(upper_2_13)
    dict['2_13'] = color_list

    # 伊利色 14
    lower_14_1 = array([15, 120, 90])
    upper_14_1 = array([30, 145, 170])
    color_list = []
    color_list.append(lower_14_1)
    color_list.append(upper_14_1)
    dict['14_1'] = color_list

    # 明黄色，深黄 ——金，蒲甘 -1172
    lower_2_2 = array([20, 110, 110])
    upper_2_2 = array([35, 255, 255])
    color_list = []
    color_list.append(lower_2_2)
    color_list.append(upper_2_2)
    dict['2_2'] = color_list

    # 草绿色 古尔-1210 明黄
    lower_2_3 = array([25, 150, 85])
    upper_2_3 = array([38, 255, 235])
    color_list = []
    color_list.append(lower_2_3)
    color_list.append(upper_2_3)
    dict['2_3'] = color_list

    # 淡绿色--帕拉玛拉-1210
    lower_2_4 = array([25, 120, 150])
    upper_2_4 = array([35, 145, 200])
    color_list = []
    color_list.append(lower_2_4)
    color_list.append(upper_2_4)
    dict['2_4'] = color_list
    # 安蔡 草绿 14
    lower_2_11 = array([24, 120, 150])
    upper_2_11 = array([35, 155, 255])
    color_list = []
    color_list.append(lower_2_11)
    color_list.append(upper_2_11)
    dict['2_11'] = color_list

    lower_2_24 = array([37, 135, 90])
    upper_2_24 = array([52, 255, 255])
    color_list = []
    color_list.append(lower_2_24)
    color_list.append(upper_2_24)
    dict['2_24'] = color_list

    # 青绿色--吴哥--喀喀边那-1210
    lower_2_5 = array([33, 160, 100])
    upper_2_5 = array([45, 255, 200])
    color_list = []
    color_list.append(lower_2_5)
    color_list.append(upper_2_5)
    dict['2_5'] = color_list

    # 457 吐蕃
    lower_2_15 = array([33, 80, 114])
    upper_2_15 = array([48, 135, 200])
    color_list = []
    color_list.append(lower_2_15)
    color_list.append(upper_2_15)
    dict['2_15'] = color_list

    # 黄绿色 -色那-1210
    lower_2_6 = array([28, 175, 150])
    upper_2_6 = array([38, 230, 215])
    color_list = []
    color_list.append(lower_2_6)
    color_list.append(upper_2_6)
    dict['2_6'] = color_list

    # 深绿色 --卡拉丘里 赵-457
    lower_2_7 = array([43, 135, 80])
    upper_2_7 = array([60, 220, 140])
    color_list = []
    color_list.append(lower_2_7)
    color_list.append(upper_2_7)
    dict['2_7'] = color_list

    # 青绿色 蒙古 -1120
    lower_2_8 = array([43, 145, 60])
    upper_2_8 = array([63, 255, 255])
    color_list = []
    color_list.append(lower_2_8)
    color_list.append(upper_2_8)
    dict['2_8'] = color_list

    lower_2_17 = array([40, 170, 140])
    upper_2_17 = array([60, 255, 230])
    color_list = []
    color_list.append(lower_2_17)
    color_list.append(upper_2_17)
    dict['2_17'] = color_list

    # 淡绿色 -高丽
    lower_2_9 = array([35, 95, 145])
    upper_2_9 = array([60, 155, 225])
    color_list = []
    color_list.append(lower_2_9)
    color_list.append(upper_2_9)
    dict['2_9'] = color_list

    lower_2_16 = array([43, 110, 75])
    upper_2_16 = array([65, 185, 255])
    color_list = []
    color_list.append(lower_2_16)
    color_list.append(upper_2_16)
    dict['2_16'] = color_list

    # 桔色 14 花剌子模
    lower_2_10 = array([9, 150, 90])
    upper_2_10 = array([20, 255, 225])
    color_list = []
    color_list.append(lower_2_10)
    color_list.append(upper_2_10)
    dict['2_10'] = color_list

    # 14 *离
    lower_2_12 = array([49, 15, 165])
    upper_2_12 = array([72, 65, 220])
    color_list = []
    color_list.append(lower_2_12)
    color_list.append(upper_2_12)
    dict['2_12'] = color_list

    lower_2_25 = array([34, 70, 110])
    upper_2_25 = array([60, 200, 210])
    color_list = []
    color_list.append(lower_2_25)
    color_list.append(upper_2_25)
    dict['2_25'] = color_list

    # -110 乌孙
    lower_2_19 = array([55, 73, 115])
    upper_2_19 = array([73, 185, 225])
    color_list = []
    color_list.append(lower_2_19)
    color_list.append(upper_2_19)
    dict['2_19'] = color_list

    # 14乌桓
    lower_2_23 = array([48, 95, 95])
    upper_2_23 = array([65, 148, 230])
    color_list = []
    color_list.append(lower_2_23)
    color_list.append(upper_2_23)
    dict['2_23'] = color_list

    # -110 安息
    lower_2_20 = array([60, 88, 84])
    upper_2_20 = array([78, 197, 170])
    color_list = []
    color_list.append(lower_2_20)
    color_list.append(upper_2_20)
    dict['2_20'] = color_list
    # 3 大理 粉白
    lower_3_1 = array([50, 20, 145])
    upper_3_1 = array([70, 60, 215])
    color_list = []
    color_list.append(lower_3_1)
    color_list.append(upper_3_1)
    dict['3_1'] = color_list

    # 蓝绿色 伊巴德派-1120
    lower_3_2 = array([68, 120, 150])
    upper_3_2 = array([76, 190, 255])
    color_list = []
    color_list.append(lower_3_2)
    color_list.append(upper_3_2)
    dict['3_2'] = color_list

    # 河流色-墨绿
    lower_3_3 = array([67, 190, 170])
    upper_3_3 = array([75, 235, 190])
    color_list = []
    color_list.append(lower_3_3)
    color_list.append(upper_3_3)
    dict['3_3'] = color_list

    # 14印度 提帕亚
    lower_3_5 = array([62, 80, 155])
    upper_3_5 = array([80, 180, 255])
    color_list = []
    color_list.append(lower_3_5)
    color_list.append(upper_3_5)
    dict['3_5'] = color_list

    # 457 乌落侯
    lower_3_9 = array([69, 100, 80])
    upper_3_9 = array([80, 255, 135])
    color_list = []
    color_list.append(lower_3_9)
    color_list.append(upper_3_9)
    dict['3_9'] = color_list

    # 457 契丹
    lower_3_10 = array([48, 170, 110])
    upper_3_10 = array([66, 255, 165])
    color_list = []
    color_list.append(lower_3_10)
    color_list.append(upper_3_10)
    dict['3_10'] = color_list

    # 243
    lower_3_8 = array([47, 76, 73])
    upper_3_8 = array([76, 238, 150])
    color_list = []
    color_list.append(lower_3_8)
    color_list.append(upper_3_8)
    dict['3_8'] = color_list

    # 457 柔然
    lower_3_7 = array([68, 100, 140])
    upper_3_7 = array([88, 255, 255])
    color_list = []
    color_list.append(lower_3_7)
    color_list.append(upper_3_7)
    dict['3_7'] = color_list

    # 安息 14
    lower_3_6 = array([55, 35, 80])
    upper_3_6 = array([80, 170, 145])
    color_list = []
    color_list.append(lower_3_6)
    color_list.append(upper_3_6)
    dict['3_6'] = color_list

    # 天蓝绿 --女王国-1120
    lower_3_4 = array([77, 130, 150])
    upper_3_4 = array([88, 255, 220])
    color_list = []
    color_list.append(lower_3_4)
    color_list.append(upper_3_4)
    dict['3_4'] = color_list

    # 浅蓝 -西辽
    lower_4_1 = array([90, 100, 135])
    upper_4_1 = array([103, 255, 255])
    color_list = []
    color_list.append(lower_4_1)
    color_list.append(upper_4_1)
    dict['4_1'] = color_list

    # 14 康居 天蓝
    lower_14_2 = array([84, 110, 127])
    upper_14_2 = array([100, 255, 200])
    color_list = []
    color_list.append(lower_14_2)
    color_list.append(upper_14_2)
    dict['14_2'] = color_list

    # 深蓝-屈出律
    lower_4_8 = array([90, 70, 0])
    upper_4_8 = array([103, 255, 130])
    color_list = []
    color_list.append(lower_4_8)
    color_list.append(upper_4_8)
    dict['4_8'] = color_list

    # 更深蓝 1120 海蓝
    lower_4_2 = array([100, 130, 130])
    upper_4_2 = array([117, 255, 190])
    color_list = []
    color_list.append(lower_4_2)
    color_list.append(upper_4_2)
    dict['4_2'] = color_list

    # 396 贵霜
    lower_4_11 = array([92, 85, 85])
    upper_4_11 = array([127, 190, 194])
    color_list = []
    color_list.append(lower_4_11)
    color_list.append(upper_4_11)
    dict['4_11'] = color_list

    # 757 吐蕃
    lower_4_10 = array([108, 100, 105])
    upper_4_10 = array([129, 230, 240])
    color_list = []
    color_list.append(lower_4_10)
    color_list.append(upper_4_10)
    dict['4_10'] = color_list

    # 紫色 西夏 1120
    lower_4_3 = array([125, 105, 125])
    upper_4_3 = array([145, 230, 230])
    color_list = []
    color_list.append(lower_4_3)
    color_list.append(upper_4_3)
    dict['4_3'] = color_list

    # 浅紫色 日本
    lower_4_4 = array([110, 15, 100])
    upper_4_4 = array([140, 100, 200])
    color_list = []
    color_list.append(lower_4_4)
    color_list.append(upper_4_4)
    dict['4_4'] = color_list

    # 深紫色 拉塔 1120
    lower_4_5 = array([146, 80, 80])
    upper_4_5 = array([170, 200, 200])
    color_list = []
    color_list.append(lower_4_5)
    color_list.append(upper_4_5)
    dict['4_5'] = color_list

    # 深红 德里苏丹 1120
    lower_4_6 = array([170, 100, 125])
    upper_4_6 = array([180, 195, 255])
    color_list = []
    color_list.append(lower_4_6)
    color_list.append(upper_4_6)
    dict['4_6'] = color_list

    # 红 雅达瓦
    lower_4_7 = array([170, 45, 125])
    upper_4_7 = array([180, 100, 205])
    color_list = []
    color_list.append(lower_4_7)
    color_list.append(upper_4_7)
    dict['4_7'] = color_list

    # 457 悦般
    lower_4_9 = array([160, 125, 125])
    upper_4_9 = array([180, 225, 255])
    color_list = []
    color_list.append(lower_4_9)
    color_list.append(upper_4_9)
    dict['4_9'] = color_list

    return dict
