import pymysql

db = pymysql.connect(host='database-1.c4y1s8zaxihb.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='admin', passwd='mypassword', db='retail_info', charset='utf8')

cursor = db.cursor()
longitude = []
latitude = []
sql1 = '''
            CREATE TABLE test (test int)

'''
sql2 = '''
        SELECT longitude, latitude from busan_store where law_dong_name = "금사동" limit 5
'''
cursor.execute(sql2)
# DB에 Complete 하기
result = cursor.fetchall()
for tup in result:
    longitude.append(tup[0])
    latitude.append(tup[1])
print(longitude)
print(latitude)
db.commit()
# DB 연결 닫기
db.close()
