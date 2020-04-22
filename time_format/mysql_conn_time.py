# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 16:08
# @Author  : Bo
# @Email   : mat_wu@163.com
# @File    : mysql_conn_time.py
# @Software: PyCharm

from configparser import ConfigParser
from pymysql import connect, Error

db_config = 'password.txt'


class MySqlConn(object):
    """数据库连接"""

    # 数据库初始化连接
    def __init__(self):
        try:
            target = ConfigParser()
            target.read(db_config, encoding='utf-8')  # 注意编码方式

            host = target.get('mysqlConfigure', 'host')
            db = target.get('mysqlConfigure', 'db')
            user = target.get('mysqlConfigure', 'user')
            password = target.get('mysqlConfigure', 'password')
            port = int(target.get('mysqlConfigure', 'port'))
            charset = target.get('mysqlConfigure', 'charset')
            self._conn = connect(host=host, user=user, passwd=password, db=db, port=port, charset=charset)
            if (self._conn):
                self._cur = self._conn.cursor()
        except IOError:
            print("Error: 无法连接数据库")

    # 图片出库
    def img_select(self, choose_year):
        insertString = "SELECT map_image FROM primal_map WHERE map_year = %s"
        try:
            self._cur.execute(insertString, choose_year)
            result = self._cur.fetchone()
            self._conn.commit()
            return result
        except Error as e:
            self._conn.rollback()
            print("查询失败")

    def year_change(self, choose_year):
        queryString = "select MAX(contour_year) from contour_info WHERE contour_year <= %s"
        try:
            self._cur.execute(queryString, choose_year)
            result = self._cur.fetchone()
            self._conn.commit()
            return result
        except Error as e:
            self._conn.rollback()
            print("查询失败")

    def contours_select(self, choose_year):
        contour_list = []
        insertString = "SELECT contour_name FROM contour_info WHERE contour_year = %s"
        try:
            self._cur.execute(insertString, choose_year)
            result = self._cur.fetchall()
            self._conn.commit()
            for item in result:
                contour_list.append(item[0])
            return contour_list
        except Error as e:
            self._conn.rollback()
            print("查询失败")

    def contour_points(self, choose_year, contours_name):
        insertString = "SELECT contour_points FROM contour_info WHERE contour_year = %s and contour_name = %s "
        try:
            self._cur.execute(insertString, (choose_year, contours_name))
            result = self._cur.fetchall()
            self._conn.commit()
            return result
        except Error as e:
            self._conn.rollback()
            print("查询失败")

    def site_select_one(self, choose_year, site_name):
        insertString = "SELECT site_name,site_lenth,site_centre FROM site_info WHERE site_year = %s and  site_name = %s "
        try:
            self._cur.execute(insertString, (choose_year, site_name))
            result = self._cur.fetchone()
            self._conn.commit()
            return result
        except Error as e:
            self._conn.rollback()
            print("查询失败")

    def site_select(self, choose_year, contour_name):
        insertString = "SELECT site_name,site_lenth,site_centre FROM site_info WHERE site_year = %s and  site_contour = %s "
        try:
            self._cur.execute(insertString, (choose_year, contour_name))
            result = self._cur.fetchall()
            self._conn.commit()
            return result
        except Error as e:
            self._conn.rollback()
            print("查询失败")


if __name__ == "__main__":
    conn = MySqlConn()
    result = conn.img_select("77")
    print(result)
