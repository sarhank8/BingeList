import os

class Config:
    if os.environ.get('VERCEL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:////tmp/bingelist.db')
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///bingelist.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads/avatars'
     # Hardcoded for now per user request
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-only-change-me'