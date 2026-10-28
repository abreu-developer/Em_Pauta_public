from src.models.repository.interface.repository_interface import RepositoryInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse


class MovieDelete:
    def __init__(self, repo: RepositoryInterface) -> None:
        self.__repo = repo

    def delete(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["_id"]
        self.__delete_movie(movie_id)
        return self.__format_response()

    def __delete_movie(self, movie_id: str) -> None:
        if not self.__repo.remove_by_id(movie_id):
            raise ValueError("Movie not found")

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "movie",
                    "count": 1,
                    "remove": True
                }
            },
            status_code=200
        )
