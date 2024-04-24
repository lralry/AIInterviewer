import base64
import csv
import os

import cv2
import dlib
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, jsonify

from database import HRQuestions
# from models.config import flask_default


# 实例化一个Flask类的对象
app = Flask(__name__)

ques = HRQuestions.HRQuestions()
q,t = ques.ques_queue(4)

def cors(environ):
    environ.headers['Access-Control-Allow-Origin'] = '*'
    environ.headers['Access-Control-Allow-Method'] = '*'
    environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return environ


# 设置路由和函数对应关系
@app.route('/')
def web1():
    return render_template("web.html",questions=q)

@app.route('/', methods=['POST'])
def process_data():
    data = request.json  # 获取来自 JavaScript 的 JSON 数据
    happy_score = data.get('happyScore')  # 提取 happyScore 字段
    neutral_score = data.get('neutralScore')  # 提取 neutralScore 字段
    # 在这里对数据进行进一步的处理
    print(f'Happy Score: {happy_score}, Neutral Score: {neutral_score}')
    # 返回响应给 JavaScript（可选）
    return 'Data received successfully!', 200
@app.route('/result', methods=['POST', 'GET'])
def web2():
    return render_template("echarts.html",topic=t)


# run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
