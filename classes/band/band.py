from sql_query.get_band_genre_sql import getBandGenreSql
from sql_query.get_band_sql import getBandSql
from classes.utils import Utils


class Band:
    def getBandGenres(self, band):
        conn = Utils.get_db_connection()
        genres = conn.execute(getBandGenreSql.get_sql, [int(band["cdband"])]).fetchall()

        # print(genres[]["nmgenre"])

        band_genres = ""
        for genre in genres:
            band_genres += genre["nmgenre"] + ", "

        print(band_genres)

    def getBands(self):
        conn = Utils.get_db_connection()
        bands = conn.execute(getBandSql.get_sql).fetchall()
        conn.close()

        for band in bands:
            self.getBandGenres(band)

        return bands
