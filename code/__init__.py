from flask import Flask, request, render_template, url_for, jsonify
import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook

app = Flask(__name__)
url = 'http://192.168.0.96:8080/client/api'
db = pymysql.connect(host='database-1.c4y1s8zaxihb.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='admin', passwd='mypassword', db='retail_info', charset='utf8')
cursor = db.cursor()                     


@app.route("/")
def main():
    return render_template("main.html")

@app.route("/test")
def home():
    longitude = []
    latitude = []
   
    sql = '''
        create table test
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    for tup in result:
        longitude.insert(i, tup[0])
        latitude.insert(i,tup[1])
        i = i + 1
    storelen=len(result)
    return render_template("category.html", longitude=longitude, latitude=latitude)

@app.route("/getposition", methods=['GET', 'POST'])
def getposition():
    longitude = []
    latitude = []
    keyword = request.form['keyword']
    sql = '''
        SELECT longitude, latitude from busan_store where law_dong_name = %s limit 5
    '''
    cursor.execute(sql,keyword)
    result = cursor.fetchall()
    for tup in result:
        longitude.append(tup[0])
        latitude.append(tup[1])
    storelen=len(result)
    db.close()
    print(longitude)
    print(latitude)
    return jsonify(data=result)



if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)