GET_BAND_GENRE_SQL = """
    SELECT
        genre.nmgenre
    FROM genre
    INNER JOIN bandgenre ON (bandgenre.cdgenre = genre.cdgenre)
    INNER JOIN band ON (band.cdband = bandgenre.cdband)
    WHERE band.cdband = ?
"""
