from redis import Redis
import os

class RedisConnection:
    def __init__(self):
        self.__redis_conn = None
        
    def connect(self) -> Redis:
        redis_conn = Redis(
            host=os.getenv("REDIS_HOST"),
            port=os.getenv("REDIS_PORT"),
            password=os.getenv("REDIS_PASSWORD"),
            db=0
        )
        self.__redis_conn = redis_conn
        return redis_conn
        

    def get_connection(self)-> Redis:
        return self.__redis_conn