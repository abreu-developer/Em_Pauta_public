from redis import Redis
from .interface.redis_interface import RedisRepository

class RedisRepository(RedisRepository):
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn
        
        
    def insert_ex(self, key: str, value: any, ex: int)-> None:
        self.__redis_conn.set(key,value,ex)
        
        
    def get_key(self, key: str) -> str:
        value = self.__redis_conn.get(key)
        if value:
            return value.decode("utf8")
        return None