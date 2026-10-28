from src.models.database.mongo_db_connection import MongoDbConnection
from src.models.repository.mongo_repository import MongoRepository
from src.usercase.movie.movie_update import MovieUpdate



def update_movie_composer():
    conn = MongoDbConnection.get_connection()
    repo = MongoRepository(conn)
    usecase = MovieUpdate(repo)
    
    return usecase