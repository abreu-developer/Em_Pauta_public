from src.main.server.server import app
from dotenv import load_dotenv
from src.models.database.mongo_db_connection import MongoDbConnection

load_dotenv()

if __name__ == "__main__":
    mongoDb = MongoDbConnection()
    mongoDb.connection()
    app.run(host="0.0.0.0",port=3000,debug= True)