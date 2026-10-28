from abc import ABC,abstractmethod

class RedisRepository(ABC):

    @abstractmethod
    def insert_ex(self, key: str, value: any, ex: int)-> None:
        pass
        
    @abstractmethod    
    def get_key(self, key: str) -> str:
        pass