import base64
import cv2
import dlib
import numpy as np
from flask import Flask, render_template, request, redirect, url_for,jsonify
#from models.config import flask_default
#from view.momgodb_do import mongo_view
from pymongo import MongoClient
from face.face_emotion import FaceEmotion

client = MongoClient('mongodb://localhost:27017')  # 地址与接口
database = client.get_database('test')  # 数据库名
collection = database.get_collection('test_q')  # 表名


# 实例化一个Flask类的对象
app = Flask(__name__)

# 设置路由和函数对应关系
@app.route('/')
def web1():
    return render_template("web.html")


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


@app.route('/process_image', methods=['POST'])
def process_image():
    # 从请求中获取图像数据
    image_data = request.json['image']

    # 解码图像数据
    nparr = np.frombuffer(base64.b64decode(image_data.split(',')[1]), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 转换图像为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用人脸检测器检测人脸
    faces = detector(gray, 0)

    # 计算积极情绪和消极情绪的占比
    positive_emotion_count = 0
    negative_emotion_count = 0

    for face in faces:
        # 使用特征提取器获取人脸特征点
        shape = predictor(gray, face)

        # 根据特征点分析情绪
        # 这里只是一个示例，你需要根据你的情绪分析算法进行具体实现

        # 假设这里是你的情绪分析算法，并根据分析结果更新 positive_emotion_count 和 negative_emotion_count

    total_faces = len(faces)

    # 构建计算结果的 JSON 格式数据
    result = {
        'positiveEmotion': positive_emotion_count / total_faces,
        'negativeEmotion': negative_emotion_count / total_faces
    }

    # 发送计算结果回前端
    return jsonify(result)


@app.route('/result',methods = ['POST', 'GET'])
def web2():
    return render_template("echarts.html")


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
    app.run(host='0.0.0.0', port=5000, debug=True)
