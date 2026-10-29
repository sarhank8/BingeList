import os

def _database_uri():
    default = 'sqlite:////tmp/bingelist.db' if os.environ.get('VERCEL') else 'sqlite:///bingelist.db'
    uri = os.getenv('DATABASE_URL', default)
    # Some providers (Heroku, older Neon/Supabase strings) give "postgres://",
    # which SQLAlchemy 1.4+ rejects
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    return uri

class Config:
    SQLALCHEMY_DATABASE_URI = _database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping': True}
    UPLOAD_FOLDER = 'static/uploads/avatars'
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-only-change-me'