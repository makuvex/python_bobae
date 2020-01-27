import pymysql
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from preference import preference


class mySqlService:
    
    cur = None
    def __init__(self):
        print('__init__')
        con = pymysql.connect(host=preference.host, 
                              user=preference.user, 
                              password=preference.passwd, 
                              db=preference.db_name, 
                              charset='utf8')
        self.cur = con.cursor()

    def __del__(self):
        con.close()
        
    def insert(self, sno, subject, author, link, date, recomm, count):
        print('insert')
        sql = """insert into girl(sno,subject,author,link,regdate,recomm,viewcount) values (%s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(sql, (sno, subject, author, link, date, recomm, count))
        con.commit()

    def selectLink(self):
        print('selectLink')
        sql = "select link from " + preference.table_name
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows