GET_ALL_BANDS_SQL = """
    SELECT
        band.cdband,
        band.nmband,
        country.nmcountry,
        band.fgstatus
    FROM band
    INNER JOIN country ON (country.cdcountry = band.cdcountry)
"""
