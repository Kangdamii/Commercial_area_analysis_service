from flask import Flask, request, render_template
import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook

app = Flask(__name__)

url = 'http://192.168.0.96:8080/client/api'

@app.route("/")
def keyword():
    return render_template("mapsearch.html")

@app.route("/test")
def home():
    return render_template("test.html")

if(__name__)=='__main__':
    app.run(host='0.0.0.0', debug=True)