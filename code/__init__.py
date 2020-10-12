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

@app.route("/getposition", methods=['GET', 'POST'])
def getposition():
    ids = []
    longitude = []
    latitude = []
    keyword = request.form['keyword']
    division = request.form['division']
    sql = '''
        SELECT name,longitude,latitude from new_busan_store where law_dong_name = %s and division = %s
    '''
    cursor.execute(sql,(keyword,division))
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)