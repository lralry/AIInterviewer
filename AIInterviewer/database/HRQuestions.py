from pymongo import MongoClient
import pandas as pd
import random


class HRQuestions:
    # 创建类的构造函数，self为类的实例
    def __init__(self):
        # 获取数据库的连接
        self.client = MongoClient(host='localhost', port=27017)
        # 打印信息以作检查
        print(self.client)

        self.__db = self.client["AIInterview"]
        self.__col = self.__db["HRQ"]

    # 导入初始面试问题
    def __default_input(self):
        df = pd.read_excel("Questions.xlsx")
        data = df.to_dict("records")

        self.__col.insert_many(data)

    # 随机抽取m个主题提问
    # 返回数字序列
    def __get_topics(self,num):
        # 获得数据库中的主题个数
        n = self.__col.count_documents({})
        # 在n中，选择m个不重复的数字,存放在m中
        random_documents = self.__col.aggregate([
            {"$sample": {"size": num}}
        ])

        return random_documents

    # 在话题中抽取问题
    # topic 挑出来的文档
    # 返回具体问题文字
    def ques_queue(self,num):
        ques = []
        top = ['表达能力']
        # 去除文档中的空值键值对
        # 数据量少，手动去除了

        topic = self.__get_topics(num)
        for doc in topic:
            if len(doc) > 1:  # 确保文档中至少有两对键值对
                # 创建一个不包含第一、二对键值对的字典
                keys_to_consider = list(doc.keys())[2:]  # 忽略第一个键
                # 随机选择一个键
                random_key = random.choice(keys_to_consider)
                # 将对应的值添加到新数组
                ques.append(doc[random_key])
                top.append(doc['topic'])


        return ques,top

# if __name__ == '__main__':
#     ques = HRQuestions()
#     q,t = ques.ques_queue(4)
#     print(q,t)
