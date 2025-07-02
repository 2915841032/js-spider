import redis

redis_client = redis.from_url('redis://:root@10.1.80.1:6379/2')
redis_client.lpush('douban:start_urls', 'https://movie.douban.com/top250?start=0&filter=')
print('插入完成...')
redis_client.close()