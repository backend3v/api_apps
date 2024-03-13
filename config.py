import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    def __init__(self):
        self.secret_key = os.getenv('SECRET_KEY')
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')
        self.debu = os.getenv('DEBUG')
        self.ttl_token = int(os.getenv('TTL'))
        self.iss = os.getenv('ISS')
        self.db_host = os.getenv('db_host')
        self.db_user = os.getenv('db_user')
        self.db_password = os.getenv('db_password')
        self.db_database = os.getenv('db_database')
        self.algorithm = os.getenv('algorithm')
        self.secret_app = os.getenv('secret')
