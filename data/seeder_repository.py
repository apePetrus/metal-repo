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


class SeederRepository:
    def save_genre_ref(self, nmgenre):
        cdgenre = DbConnector().execute_insert(
            INSERT_GENRE_REF_SQL, {"nmgenre": nmgenre}
        )

        return cdgenre

    def save_band_genre(self, rel_data):
        DbConnector().execute_insert(INSERT_BAND_GENRE_SQL, rel_data)
