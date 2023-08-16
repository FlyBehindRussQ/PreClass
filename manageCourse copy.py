import pymysql


#打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Qjj030107', db='demo')

#创建游标对象
cur = conn.cursor()



id=input()
name=input()
gender=input()
class1=input()



student_data = (id, name, gender,class1)


sql_insert = "INSERT INTO student (id, name, gender,class1) VALUES (%s, %s, %s, %s)"

cur.execute(sql_insert, student_data)
conn.commit()