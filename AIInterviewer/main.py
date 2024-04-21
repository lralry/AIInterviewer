from flask import Flask, render_template, request, redirect, url_for,flask
#from models.config import flask_default
#from view.momgodb_do import mongo_view
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')  # 地址与接口
database = client.get_database('test')  # 数据库名
collection = database.get_collection('test_q')  # 表名


# 实例化一个Flask类的对象
app = Flask(__name__)

# 设置路由和函数对应关系
@app.route('/')
def web1():
    return render_template("web.html")

@app.route('/result',methods = ['POST', 'GET'])
def web2():
    return render_template("echarts6.html")


@app.route('/inser_test')
def inser_data():
    user = {'name': 'John Doe', 'age': 25, 'city': 'New York'}
    collection.insert_one(user)
    return 'Data inserted successfully!'

@app.route('/query')
def query_data():
    users = collection.find()
    result = ''
    for user in users:
        result += f"Name: {user['name']}, Age: {user['age']}, City: {user['city']}<br>"
    return result



#run
if __name__ == '__main__':
    app.run(host = 0.0.0.0)
