from sql_query.get_band_genre_sql import getBandGenreSql
from sql_query.get_band_sql import getBandSql
from enums.band_fgstatus_enum import BandStatus
from classes.utils import Utils


class Band:
    def getBandGenres(self, cdband):
        conn = Utils.get_db_connection()
        genres = conn.execute(getBandGenreSql.get_sql, [int(cdband)]).fetchall()

        band_genres = []
        for genre in genres:
            band_genres.append(genre["nmgenre"])

        genres_str = ", ".join(band_genres)

        return genres_str

    def getBandStatus(self, status):
        match status:
            case BandStatus.ACTIVE.value:
                return "Active"
            case BandStatus.SPLIT_UP.value:
                return "Split up"
            case BandStatus.CHANGED_NAME.value:
                return "Changed name"
            case BandStatus.UNKNOWN.value:
                return "Unknown"

    def getBands(self):
        conn = Utils.get_db_connection()
        bands = conn.execute(getBandSql.get_sql).fetchall()
        conn.close()

        dictbands = []

        for idx, band in enumerate(bands):
            dictbands.append({})
            dictbands[idx]["name"] = band["nmband"]
            dictbands[idx]["country"] = band["nmcountry"]
            dictbands[idx]["genre"] = self.getBandGenres(band["cdband"])
            dictbands[idx]["status"] = self.getBandStatus(band["fgstatus"])

        return dictbands
