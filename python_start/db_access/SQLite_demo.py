"""
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小。
所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
"""

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("delete from user where id=?", ('1',))
conn.commit()
cursor.execute("drop table user")
cursor.execute("create table user (id varchar(20) PRIMARY KEY ,name VARCHAR (20))")
cursor.execute("insert into user(id,name) values('1','Micheal')")
print(cursor.rowcount)
conn.commit()

cursor.execute("select * from user WHERE id=?", ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()


