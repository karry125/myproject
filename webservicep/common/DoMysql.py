# -*- coding:utf-8 -*-
# @Time:2019/4/19
# @Author:wangym
# @Email:123@qq.com
# @File:DoMysql

import pymysql
from common.readconf import conf


class DoMysql:

    def __init__(self):
        url =conf.getstr("mysql","url")  # "test.lemonban.com"
        port=conf.getint("mysql","port")  # 3306
        use=conf.getstr("mysql","use")  # " test"
        pwd=conf.getstr("mysql","pwd")  # "test"
        #database=conf.getstr("mysql","database")  # "future"
        # 建立数据库连接
        self.con = pymysql.connect(host=url,port =port,user=use,password=pwd
                              ,charset="utf8")  # 不能utf-8，会报错
        # 创建游标，查询页面
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)

    def fetchall(self,sql):
        """返回元祖嵌套"""
        # sql = "select * from loan where id =308"
        # 执行sql语句
        self.cur.execute(sql)
        r = self.cur.fetchall()
        return r

    def fetchone(self,sql):
        """返回元祖单个"""
        print(type(sql))
        try:
            # if type(eval(sql))== dict:
            #     r=[]
            #     sql = eval(sql)
            #     for sq in sql:
            #         sql = sql[sq]
            #         self.cur.execute(sql)
            #         self.con.commit()
            #         re = self.cur.fetchone()
            #         r.append(re)
            # else:
                self.cur.execute(sql)
                self.con.commit()
                r = self.cur.fetchone()
        except Exception as e:
                raise e
        return r

    def commitsql(self,sql):
        # 增删改sql，需要提交才能更新成功
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        # 关闭游标 查询
        self.cur.close()
        # 关闭数据库连接
        self.con.close()

if __name__ == '__main__':
    my =DoMysql()
    # sql = "select * from loan where id =308"
    # r = my.fetchall(sql)
    # m=my.fetchone(sql)[0]
    # print(r)
    # print(m)
    # sql = 'select max(Fmobile_no) from sms_db_12.t_mvcode_info_9 where Fmobile_no like "137%912"'
    #
    # sqle='select * from sms_db_21.t_mvcode_info_9 where Fmobile_no="13700000921"'
    sqls='{"2":"4"} '
    if type(eval(sqls)) == dict:
        print("rr")
    # loan_id = my.fetchone(sqls)
    # print(loan_id)

