SQLITE = 'sqlite:///project.db'
POSTGRESQL = "postgresql+psycopg2://postgres:Kodak2025@localhost:5432/BlogPOSTS_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGRESQL