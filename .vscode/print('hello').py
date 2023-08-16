import pymysql

#打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Qjj030107', db='demo')

#创建游标对象
cur = conn.cursor()

# #创建数据库表
cur.execute("DROP TABLE IF EXISTS STUDENT3")
sql = """CREATE TABLE STUDENT3 (
         id  INT,
         number  CHAR(50),
         name CHAR(50),  
         gender CHAR(6))"""
cur.execute(sql)

# #向表中插入数据
sql = """INSERT INTO STUDENT3(id,
         number, name, gender)
         VALUES (1, 'U202112269', 'wangletian', 'male'),(2,'a','b','v')"""
cur.execute(sql)
conn.commit()

# #删除数据
delete_query = "DELETE FROM STUDENT3 WHERE NAME = %s"
name_to_delete = 'qu'
cur.execute(delete_query, (name_to_delete,))
conn.commit()

# #改数据
update_query = "UPDATE STUDENT3 SET name = %s, gender = %s, number = %s WHERE id = %s"
id_to_update = 2
new_name = 'qu'
new_gender = 'male'
new_number = 'U202112266'
cur.execute(update_query, (new_name, new_gender, new_number,id_to_update))
conn.commit()

#查询数据
sql = "SELECT * FROM STUDENT3 WHERE id = %s"
try:
   # 执行SQL语句
   id_to_select=1
   cur.execute(sql,(id_to_select))
   # 获取所有记录列表
   results = cur.fetchall()
   for row in results:
      id = row[0]
      number = row[1]
      name = row[2]
      gender = row[3]
       # 打印结果
      print ("id=%s,number=%s,name=%s,sex=%s" % \
             (id, number, name, gender ))
except:
   print ("Error: unable to fetch data")

cur.close
conn.close()
0