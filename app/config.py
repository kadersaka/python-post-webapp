import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'sqlite:///'+os.path.join(BASE_DIR, 'db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "dfqeodze49zdd"

    SECURITY_PASSWORD_SALT = "def685fe8z4f"

    SECURITY_PASSWORD_HASH = "sha512_crypt"