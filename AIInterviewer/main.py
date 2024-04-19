from flask import Flask,request,render_template,flash
from model.config import flask_default
from view.momgodb_do import mongo_view

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
