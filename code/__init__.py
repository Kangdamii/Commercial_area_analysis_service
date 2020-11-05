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
    newKeyword = '%'+keyword+'%'
    # sql = '''   SELECT name, sigoongo_name, admin_dong_name,longitude,latitude from busan_store
    #             where division = %s and admin_dong_name in
    #             (SELECT distinct dong from dong_info where goo like %s)
    #     '''
    sql = '''   SELECT name,doro_adr, longitude,latitude from busan_store
                where division = %s and admin_dong_name = %s
        '''
    cursor.execute(sql,(division,keyword))
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

@app.route("/getdongName", methods=['GET', 'POST'])
def getdongName():
    keyword = request.form['keyword'] 
    newKeyword = '%'+keyword+'%'
    sql = "SELECT  distinct dong from dong_info where goo like %s"
    cursor.execute(sql,newKeyword)
    data_list=cursor.fetchall()       
    jsondata=json.dumps(data_list) 
    return jsondata


@app.route("/getpopulation", methods=['GET', 'POST'])
def getpopulation():
    keyword = request.form['keyword'] 
    sql = "SELECT population from busan_admin_population where dong = %s"
    cursor.execute(sql,keyword)
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)