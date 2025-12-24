from database.db_connector import DbConnector

INSERT_GENRE_REF_SQL = """
    INSERT INTO genre (
        nmgenre
    ) VALUES (
        :nmgenre
    )
"""

INSERT_BAND_GENRE_SQL = """
    INSERT INTO bandgenre (
        cdband,
        cdgenre
    ) VALUES (
        :cdband,
        :cdgenre
    )
"""

COUNT_GENRE_SQL = """
    SELECT COUNT(1) AS COUNT
    FROM genre
    WHERE nmgenre = :nmgenre
"""


class SeederRepository:
    def save_genre_ref(self, nmgenre):
        cdgenre = DbConnector().execute_insert(
            INSERT_GENRE_REF_SQL, {"nmgenre": nmgenre}
        )

        return cdgenre

    def save_band_genre(self, rel_data):
        DbConnector().execute_insert(INSERT_BAND_GENRE_SQL, rel_data)

    def count_genre(self, nmgenre):
        count = DbConnector().execute_insert(
            INSERT_GENRE_REF_SQL, {"nmgenre": nmgenre}
        )
