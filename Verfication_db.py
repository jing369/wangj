import pymysql

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(host='test1-57-mysql.bj.startimes.com.cn',
                           port= 3306,
                           user='root',
                           passwd='star123',
                           db='cms_info',
                           charset='utf8')  #如果查询有中文需要指定测试集编码
        self.cur = self.conn.cursor()


    def check_rowcount(self,sql):
        self.cur.execute(sql)
        db_result = self.cur.fetchall()
        db_rowcount =self.cur.rowcount
        return db_rowcount

    def __del__(self):  #析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()










