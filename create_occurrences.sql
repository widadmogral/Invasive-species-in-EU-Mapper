
CREATE TABLE IF NOT EXISTS occurrences(
    gbifid BIGINT PRIMARY KEY,
    datasetName TEXT,
    eventTime  TIMESTAMP,
    countryCode TEXT,
    decimalLatitude REAL,
    decimalLongitude REAL,
    taxonkey BIGINT,
    verbatimScientificName TEXT
    );