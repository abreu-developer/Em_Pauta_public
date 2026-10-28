from abc import ABC, abstractmethod


class RepositoryInterface(ABC):

    @abstractmethod
    def insert_one(self, document: dict) -> None:
        pass

    @abstractmethod
    def select_one(self, filter: dict) -> dict:
        pass

    @abstractmethod
    def select_all(self, filter: dict) -> list:
        pass

    @abstractmethod
    def update_one(self, filters: dict, fields: dict) -> None:
        pass

    @abstractmethod
    def remove_by_id(self, id: str) -> None:
        pass
