import sqlite3

class Utils:
    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect("./db/metal-repo.db")
        conn.row_factory = sqlite3.Row
        return conn
