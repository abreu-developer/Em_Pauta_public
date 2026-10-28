from src.models.repository.interface.repository_interface import RepositoryInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse


class MovieSelect:
    def __init__(self, repo: RepositoryInterface) -> None:
        self.__repo = repo

    def select(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["_id"]
        movie = self.__select_movie(movie_id)

        return self.__format_response(movie)

    def __select_movie(self, movie_id: str) -> dict:
        movie = self.__repo.select_one(movie_id)

        if not movie:
            raise ValueError("Movie Not Found")

        return movie

    def __format_response(self, movie: dict) -> HttpResponse:
        movie["_id"] = str(movie["_id"])

        return HttpResponse(
            body={
                "data": {
                    "type": "movie",
                    "count": 1,
                    "attributes": movie,
                }
            },
            status_code=200,
        )



class MovieSelectAll:
    def __init__(self, repo: RepositoryInterface) -> None:
        self.__repo = repo

    def select_all(self, http_request: HttpRequest) -> HttpResponse:
        movies = self.__select_movies()
        formatted_movies = self.__format_movies(movies)

        return self.__format_response(formatted_movies)

    def __select_movies(self) -> list[dict]:
        return self.__repo.select_all()

    def __format_movies(self, movies: list[dict]) -> list[dict]:
        formatted_movies = []

        for movie in movies:
            formatted_movies.append(
                {
                    "_id": str(movie["_id"]),
                    "poster_url": movie["poster_url"],
                }
            )

        return formatted_movies

    def __format_response(
        self, formatted_movies: list[dict]
    ) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "movie",
                    "count": len(formatted_movies),
                    "attributes": formatted_movies,
                }
            },
            status_code=200,
        )
