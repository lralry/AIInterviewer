#数据表创建
import pymongo
mongo_client = pymongo.MongoClient(host='127.0.0.1', port=5000)
db = mongo_client['database']  # 选择数据库，如果这个数据库不存在，就创建一个

# 增
db.集合名.insert_one({})
db.集合名.insert_many([{}, {}, {}])
# 删
db.集合名.delete_one({})  # 如果有多条符合条件的数据，只会删除一条
db.集合名.delete_many({})  # 可以删除多条符合条件的数据
# 改
db.集合名.update_one({'name': 'zhangsan'}, {'$set': {'age': 0}})
db.集合名.update_many({"age": {"$gte": 0}}, {"$set": {"age": 0}})
# 查
items = db.集合名.find()  # 查所有
items = db.集合名.find_one({'name': 'zhangsan'})  # 查一个
for item in items:  # 返回的是游标，需要遍历
    print(item)
    print(item.get("name"))
