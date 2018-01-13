# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 检查MySql是否正常安装


import pymysql
pymysql.install_as_MySQLdb()



conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='s59', port=3306, charset='utf-8')
cur = conn.cursor()

print(conn)