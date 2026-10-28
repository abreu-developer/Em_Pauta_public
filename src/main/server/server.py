from flask import Flask
from src.main.routes.movies_routes import movie_routes_bp

app = Flask(__name__)
app.register_blueprint(movie_routes_bp)