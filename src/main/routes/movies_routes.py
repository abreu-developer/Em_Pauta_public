from flask import jsonify, Blueprint, request

from src.view.http_types.http_request import HttpRequest
from src.main.composer.movies.movie_insert_composer import insert_movie_composer

movie_routes_bp = Blueprint("movies", __name__)


@movie_routes_bp.route("/movies/register", methods=['POST'])
def insert():
    usercase = insert_movie_composer()
    http_request = HttpRequest(request.json)
    http_response = usercase.insert(http_request)
    return jsonify(http_response.body),http_response.status_code