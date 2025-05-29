from pymongo import MongoClient
from pymongo.errors import OperationFailure

# MongoDB连接字符串
uri = "mongodb://root:root@localhost:27017/"

try:
    # 尝试连接到MongoDB
    client = MongoClient(uri)
    # 测试连接
    client.admin.command('ping')
    print("连接成功！")
except OperationFailure as e:
    print(f"认证失败：{e}")
except Exception as e:
    print(f"发生错误：{e}")
