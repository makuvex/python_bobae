import mysql.connector
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from preference import preference

def create_table(db_name, table_name):
    mydb = mysql.connector.connect(
      host = "localhost",
      user = preference.user,
      passwd= preference.passwd,
      database = db_name
    )

    mycursor = mydb.cursor()

    query = "CREATE TABLE " + table_name + " (sno int(11) PRIMARY KEY, subject VARCHAR(255), author VARCHAR(255), link text, regdate VARCHAR(100), recomm VARCHAR(10), viewcount VARCHAR(10))"
    mycursor.execute(query)
    
    
'''
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| sno       | int(11)      | NO   | PRI | NULL    |       |
| subject   | varchar(255) | YES  |     | NULL    |       |
| author    | varchar(255) | YES  |     | NULL    |       |
| link      | varchar(255) | YES  |     | NULL    |       |
| regdate   | varchar(100) | YES  |     | NULL    |       |
| recomm    | varchar(10)  | YES  |     | NULL    |       |
| viewcount | varchar(10)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+      
'''    
