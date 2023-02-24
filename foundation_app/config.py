"""Initialize Config class to access environment variables."""
from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    """Set environment variables."""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#postgres://db_yj2e_user:6Fk09FVsCnLrvOKz6rL7xf6rvDXnfQWN@dpg-cfs26jpgp3jqrlf3q4h0-a.ohio-postgres.render.com/db_yj2e