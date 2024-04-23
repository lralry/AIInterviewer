import base64
import cv2
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
# 使用 Haar 级联分类器进行人脸检测
def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

# 情绪识别函数，这里只是一个示例
def analyze_emotion(image):
    # 在这里添加情绪识别模型的代码，返回积极情绪和消极情绪的占比
    # 例如，可以使用 OpenCV、TensorFlow、PyTorch 等框架进行情绪识别
    return {'positive': 0.7, 'negative': 0.3}

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion_endpoint():
    image_data = request.json['image_data']
    image = cv2.imdecode(np.frombuffer(base64.b64decode(image_data.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
    faces = detect_faces(image)
    # 如果检测到人脸，进行情绪识别
    if len(faces) > 0:
        emotion_result = analyze_emotion(image)
        return jsonify(emotion_result)
    else:
        return jsonify({'error': 'No faces detected'})


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
