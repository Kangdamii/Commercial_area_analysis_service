import pymysql
import csv

db = pymysql.connect(host='database-1.c4y1s8zaxihb.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='admin', passwd='mypassword', db='retail_info', charset='utf8')

cursor = db.cursor()
db.commit()

f = open('2019년도 부산시 총인구(동별).csv', 'r', encoding='cp949')
csvReader = csv.reader(f)

cursor.execute("select * from busan_population")
i = 0
for row in csvReader:
    i += 1
    if i not in [1,2]:
        user_no = (row[0])
        user_pred = (row[1])
        user_pred2 = int(row[2])

        print (user_pred)
        print (user_no)
        print(user_pred2)

        sql = """insert into busan_population (sigoodong, info, population) values (%s, %s, %s)"""

        cursor.execute(sql, (user_no, user_pred, user_pred2))

db.commit()
f.close()    
db.close()
