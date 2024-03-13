import mysql.connector
from config import Config


class Connection:
    @staticmethod
    def get_connection():
        connection = mysql.connector.connect(
            host=Config().db_host,
            user=Config().db_user,
            password=Config().db_password,
            database=Config().db_database
        )
        return connection
