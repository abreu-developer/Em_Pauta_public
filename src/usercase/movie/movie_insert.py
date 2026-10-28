from datetime import datetime

from src.models.repository.interface.repository_interface import RepositoryInterface
from src.validation.movie.movie_insert_validator import insert_movie_validator
from src.view.http_types.http_request import HttpRequest 
from src.view.http_types.http_response import HttpResponse

class MovieInsert:
    def __init__(self, repo: RepositoryInterface)-> None:
        self.__repo = repo
        
    def insert(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        self.__validator_body(body)
        new_movie = self.__format_new_movie(body)
        self.__insert_movie(new_movie)
        return self.__format_response()
  
  
    def __validator_body(self, body: dict) -> None:
        insert_movie_validator(body)
      
      
    def __format_new_movie(self, body: dict)->  dict:
        new_movie = body["data"]
        new_movie = {**new_movie,"created_at":datetime.now()}
        return new_movie
    
    
    def __insert_movie(self, new_movie: dict) -> None:
        self.__repo.insert_one(new_movie)
        
        
    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "movie",
                    "count": 1,
                    "registry" : True
                }
            },
            status_code=201
        )