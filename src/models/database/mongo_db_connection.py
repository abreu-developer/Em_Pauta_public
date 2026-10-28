import os
from pymongo import MongoClient


class MongoDbConnection:
    def __init__(self) -> None:
        self.__connection_string = os.getenv("MONGO_URI")
        self.__db_name = os.getenv("MONGO_DB")
        self.__client = None
        self.__conn = None
        
    def connection(self):
        self.__client = MongoClient(self.__connection_string)
        self.__conn = self.__client[self.__db_name]
        
    def get_connection(self):
        return self.__conn
    