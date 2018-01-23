# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 测试连接MySQL数据库

import pymysql
from pymysql import cursors
## 这里需要注意，编码是utf8不是utf-8

connection = pymysql.connect(host='127.0.0.1', db='sunjob', user='root', password='root', port=3306, charset='utf8')
try:
    ## 获取连接对应的操作游标，然后就可以了
    with connection.cursor() as cursor:
        sql_1 = "SELECT * FROM dep"
        result = cursor.execute(sql_1)
        for row in cursor.fetchall():
            print(row)
finally:
    connection.close()

print(connection.charset)
print(connection.server_status)




