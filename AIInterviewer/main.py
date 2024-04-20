from flask import Flask, render_template, request, redirect, url_for,flask
#from models.config import flask_default
#from view.momgodb_do import mongo_view
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")  # 地址与接口
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


@app.route('/c')
def forensic():
    print('this is forensic ,waiting a moment')
    # 数据库信息
    listx = []
    # 查询数据库
    for x in mycol.find({}, {"_id": 0}):
        print(x)
        listx.append(x)
    print(listx)
    # 将数据库信息转换为Json格式传给前端
    return jsonify(listx)


#run
if __name__ == '__main__':
    app.run(debug=True)
