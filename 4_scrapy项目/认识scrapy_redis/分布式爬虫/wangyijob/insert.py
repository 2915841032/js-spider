# 初始化Redis队列的示例脚本 (单独运行)
import json

if __name__ == '__main__':
    import redis

    r = redis.Redis(host='localhost', port=6379, db=2,password='root')

    # 添加1-29页的任务到队列
    for page in range(100, 130):
        task = json.dumps({'page': page})
        r.lpush('wangyi:start_urls', task)
    print("成功添加29个任务到Redis队列")
