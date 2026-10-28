from src.models.repository.interface.repository_interface import RepositoryInterface
from src.validation.movie.movie_update_validador import update_movie_validator
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse


class MovieUpdate:
    def __init__(self, repo: RepositoryInterface) -> None:
        self.__repo = repo

    def update(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["_id"]
        body = http_request.body

        self.__validator_movie(body)
        self.__update_movie(movie_id, body)

        return self.__format_response(movie_id)

    def __validator_movie(self, body: dict) -> None:
        update_movie_validator(body)

    def __update_movie(self, movie_id: str, body: dict) -> None:
        self.__repo.update_one(movie_id, body)

    def __format_response(self, movie_id: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "movie_id": movie_id,
                    "type": "movie",
                    "count": 1
                }
            },
            status_code=200
        )
