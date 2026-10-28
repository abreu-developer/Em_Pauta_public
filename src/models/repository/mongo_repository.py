from bson.objectid import ObjectId
from .interface.repository_interface import RepositoryInterface


class MongoRepository(RepositoryInterface):
    def __init__(self, mongo_conn, collection: str) -> None:
        self.__collection_name = collection
        self.__db_connection = mongo_conn

    def insert_one(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        collection.insert_one(document)

    def select_one(self, filter: dict) -> dict:
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        return collection.find_one(filter)

    def select_all(self, filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        return list(collection.find(filter))

    def update_one(self, filters: dict, fields: dict) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        collection.update_one(
            filters,
            {"$set": fields}
        )

    def remove_by_id(self, id: str) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        collection.delete_one(
            {"_id": ObjectId(id)}
        )