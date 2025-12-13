import sqlite3

class DbConnector:
    def get_db_connection(self):
        conn = sqlite3.connect("./db/metal-repo.db")
        conn.row_factory = sqlite3.Row
        return conn


    def execute_query(self, query, params = ()):
        with self.get_db_connection() as conn:
            data = conn.execute(query, params).fetchall()
            return data
