import pymysql
import csv
import pandas as pd

db = pymysql.connect(host='localhost', user='root', passwd='ekal1929', db='testdata', charset='utf-16')
cur = db.cursor()

tfile = open('/Users/dami/flask_proj/code/select_seoul.csv','r')
reader = csv.reader(tfile)

for row in reader:
    idx = (row[0])
    name = (row[1])
    category = (row[2])
    sido = (row[3])
    goo = (row[4])
    dong = (row[5])
    zibun = (row[6])
    doro = (row[7])
    floor = (row[8])
    latitd = (row[9])              # 경도
    longitd = (row[10])            # 위도

sql = """insert into info (idx, name, category, sido, goo, dong, zibun, doro, floor, latitd, longitd) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
cur.execute(sql, (idx,name,category,sido,goo,dong,zibun,doro,floor.latitd,longitd))

db.commit()
f.close()
db.close()

def make_csv(feature):
    column = []
    sql = "show full columns from %s"
    cur.execute(sql)
    rows = cur.fetchall()
    for i in range (len(row)):
        column.append(row[i][0])