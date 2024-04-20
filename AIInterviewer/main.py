from flask import Flask, render_template, request, redirect, url_for,flask
#from models.config import flask_default
#from view.momgodb_do import mongo_view
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # 地址与接口
database = client.get_database('test')  # 数据库名
collection = database.get_collection('test_q')  # 表名


# 实例化一个Flask类的对象
app = Flask(__name__)

# 设置路由和函数对应关系
@app.route('/')
def web1():
    return render_template("web.html")

@app.route('/b')
def web2():
    return render_template("echarts6.html")

#run
if __name__ == '__main__':
    app.run(debug=True)
