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

GET_ALL_ALBUMS_SQL = """
    SELECT
        album.cdalbum,
        album.nmalbum,
        album.dtrelease,
        album.fgtype,
        band.nmband
    FROM album
    INNER JOIN band ON (band.cdband = album.cdband)
"""


class AlbumRepository:
    def save_album(self, album_data):
        cdalbum = DbConnector().execute_insert(INSERT_ALBUM_SQL, album_data)
        return cdalbum

    def get_all_albums(self):
        albums_raw = DbConnector().execute_query(GET_ALL_ALBUMS_SQL)
        return albums_raw
