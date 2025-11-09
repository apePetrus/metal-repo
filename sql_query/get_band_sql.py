class getBandSql:
    get_sql = '''
        SELECT
            band.nmband,
            country.nmcountry,
            band.fgstatus
        FROM band
        INNER JOIN country ON (country.cdcountry = band.cdcountry)
    '''
