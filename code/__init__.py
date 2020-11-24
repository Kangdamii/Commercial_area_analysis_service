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
def test():
    return render_template("map.html")

@app.route("/getposition", methods=['GET', 'POST'])
def getposition():
    ids = []
    longitude = []
    latitude = []
    keyword = request.form['keyword']
    division = request.form['division']
    newKeyword = '%'+keyword+'%'
    sql = '''   SELECT name,doro_adr,longitude,latitude, admin_dong_name from busan_store
                where division = %s and admin_dong_name in
                (SELECT dong from busan_dong_population where googoon like %s)
        '''
    cursor.execute(sql,(division,keyword))
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

@app.route("/getcoordinates", methods=['GET', 'POST'])
def getcoordinates():
    keyword = request.form['keyword'] 
    sql = "SELECT dong, longitude,latitude from busan_dong_boundary where goo like %s"
    cursor.execute(sql,keyword)
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

@app.route("/getpopulation", methods=['GET', 'POST'])
def getpopulation():
    keyword = request.form['keyword'] 
    sql = "SELECT dong,population from busan_dong_population where dong like %s"
    cursor.execute(sql,keyword)
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    return jsondata

@app.route("/getchartData", methods=['GET', 'POST'])
def getchartData():
    keyword = request.form['keyword']
    percent = '%'
    new_key = percent.join(keyword)
    sql = '''
            SELECT goo, dong, graph_ex_floating_population, graph_population, graph_ex_purchase_pow, graph_profit, graph_competitor,
            graph_avg_ex_floating_population, graph_avg_population, graph_avg_ex_purchase_pow, graph_avg_profit, graph_avg_competitor,grade
            from busan_dong_analysis_graph where dong like %s'''
    cursor.execute(sql,new_key)
    data_list=cursor.fetchall()           
    jsondata=json.dumps(data_list) 
    
    return jsondata

if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)