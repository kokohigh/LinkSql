import pymysql
import hashlib

username = input('请输入用户名：')
password = input('请输入密码：')

h = hashlib.md5()
h.update(password.encode('utf8'))
password = h.hexdigest()


#打开数据库连接
db = pymysql.connect(host='localhost',
                   user='root',
                   password='Galaxy1993^^',
                   database='python_data',
                   port=3306,
                   charset='utf8')
cursor = db.cursor()

sql = 'select * from user where name="%s" and password="%s"'
cursor.execute(sql,(username,password))
cursor.close()
db.commit()

result = cursor.fetchone()
if not result:
    print('用户名或者密码错误')
else:
    print('欢迎回来%s' %username)

#关闭数据库连接
db.close()