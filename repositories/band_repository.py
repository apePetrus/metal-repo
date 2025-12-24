from database.db_connector import DbConnector

GET_ALL_BANDS_SQL = """
    SELECT
        band.cdband,
        band.nmband,
        country.nmcountry,
        band.fgstatus
    FROM band
    INNER JOIN country ON (country.cdcountry = band.cdcountry)
"""

GET_BAND_GENRE_SQL = """
    SELECT
        genre.nmgenre
    FROM genre
    INNER JOIN bandgenre ON (bandgenre.cdgenre = genre.cdgenre)
    INNER JOIN band ON (band.cdband = bandgenre.cdband)
    WHERE band.cdband = ?
"""

INSERT_BAND_SQL = """
    INSERT INTO band (
        nmband,
        cdcountry,
        fgstatus
    ) VALUES (
        :nmband,
        :cdcountry,
        :fgstatus
    )
"""


class BandRepository:
    def get_all_bands(self):
        bands_raw = DbConnector().execute_query(GET_ALL_BANDS_SQL)

        return bands_raw

    def get_band_genres(self, cdband):
        band_genres_raw = DbConnector().execute_query(GET_BAND_GENRE_SQL, [int(cdband)])

        return band_genres_raw

    def save_band(self, band_data):
        cdband = DbConnector().execute_insert(INSERT_BAND_SQL, band_data)

        return cdband
