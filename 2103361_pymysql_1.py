import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port= 3306,
                             user='root',
                             password='20020927',
                             database='mydb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()
 sql = "select * from users"
 cursor.execute(sql)

result = cursor.fetchall()
result
