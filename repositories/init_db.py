from database.db_connector import DbConnector


def init_db():
    with open("./database/schema.sql", "r") as schema:
        DbConnector().execute_script(schema.read())
