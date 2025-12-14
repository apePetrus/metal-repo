from database.db_connector import DbConnector

INSERT_ALBUM_SQL = """
    INSERT INTO album (
        nmalbum,
        dtrelease,
        fgtype,
        cdband
    ) VALUES (
        :nmalbum,
        :dtrelease,
        :fgtype,
        :cdband
    )
"""


class AlbumRepository:
    def save_album(self, album_data):
        cdalbum = DbConnector().execute_insert(INSERT_ALBUM_SQL, album_data)
        return cdalbum
