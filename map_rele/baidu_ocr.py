# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 9:28
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : baidu_ocr.py
# @Software: PyCharm

from aip import AipOcr
import configparser


file_config = 'password.txt'


class BaiDuAPI:
    """
    调用百度API进行文字识别
    """

    def __init__(self):
        self.file_path = file_config
        try:
            target = configparser.ConfigParser()
            target.read(self.file_path, encoding='utf-8')  # 注意编码方式
            app_id = target.get('MyPassWord', 'APP_ID')
            api_key = target.get('MyPassWord', 'API_Key')
            secret_key = target.get('MyPassWord', 'Secret_Key')
            self.client = AipOcr(app_id, api_key, secret_key)
        except IOError:
            print("Error: 没有加载配置文件")

    def picture2text(self,filePath):
        # 图片识别成文字
        image = self.get_picture(filePath)
        texts = self.client.basicGeneral(image)
        all_texts = ''

        if texts['words_result'] !=[]:
            for word in texts['words_result']:
                all_texts = all_texts + word.get('words',' ')
        else:
            all_texts = "未能识别"
        return all_texts

    @staticmethod #装饰器
    def get_picture(filePath):
        with open(filePath,'rb') as fp:
            return fp.read()

