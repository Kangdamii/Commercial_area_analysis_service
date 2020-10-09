from flask import Flask, request, render_template, url_for, jsonify
import json
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
    return render_template("category.html")

@app.route("/getposition", methods=['GET', 'POST'])
def getposition():
    positions = {}
    keyword = request.form['keyword']
    sql = '''
        SELECT id,longitude, latitude from busan_store where law_dong_name = %s limit 5
    '''
    cursor.execute(sql,keyword)
    result = cursor.fetchall()
    for tup in result:
        storeId = tup[0]
        longitude = tup[1]
        latitude = tup[2]
        positions[storeId]={"positions":{"longitude":longitude,"latitude":latitude}}    
    # for item in content:
    # print(item["longitude"])
    jsonPos = json.dumps(positions)     #dictionary to json
    return jsonify(data = jsonPos)

if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)