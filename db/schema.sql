CREATE TABLE IF NOT EXISTS country (
    cdcountry INTEGER PRIMARY KEY,
    nmcountry VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS band (
    cdband INTEGER PRIMARY KEY,
    nmband VARCHAR(50) NOT NULL,
    cdcountry INTEGER NOT NULL,
    fgstatus INTEGER NOT NULL,
    FOREIGN KEY (cdcountry) REFERENCES country (cdcountry)
);

CREATE TABLE IF NOT EXISTS genre (
    cdgenre INTEGER PRIMARY KEY,
    nmgenre VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS bandgenre (
    cdband INTEGER NOT NULL,
    cdgenre INTEGER NOT NULL,
    FOREIGN KEY (cdband) REFERENCES band (cdband),
    FOREIGN KEY (cdgenre) REFERENCES genre (cdgenre)
);
