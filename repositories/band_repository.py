from classes.utils import Utils
from sql_query.band.get_all_bands import GET_ALL_BANDS_SQL
from sql_query.band.get_band_genre import GET_BAND_GENRE_SQL


class BandRepository:
    def get_all_bands(self):
        bands_raw = Utils().execute_query(GET_ALL_BANDS_SQL)

        return bands_raw

    def get_band_genres(self, cdband):
        band_genres_raw = Utils().execute_query(GET_BAND_GENRE_SQL, [int(cdband)])

        return band_genres_raw
