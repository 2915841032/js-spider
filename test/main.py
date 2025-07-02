import pymongo
from pymongo.errors import OperationFailure


def test_mongo_connection():
    try:
        # MongoDB URI，包括用户名、密码和认证数据库
        mongo_uri = "mongodb://root:root@localhost:27017/test?authSource=admin"

        # 创建 MongoDB 客户端并连接
        client = pymongo.MongoClient(mongo_uri)

        # 获取数据库
        db = client.test

        # 测试是否能成功获取服务器状态
        server_info = client.server_info()
        print("MongoDB 服务器信息:", server_info)

        # 如果没有异常，连接正常
        print("MongoDB 连接成功!")

    except ConnectionError as e:
        print("MongoDB 连接错误:", e)
    except OperationFailure as e:
        print("身份验证失败:", e)
    except Exception as e:
        print("发生其他错误:", e)
    finally:
        client.close()

if __name__ == "__main__":
    test_mongo_connection()
