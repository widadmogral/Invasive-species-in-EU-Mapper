
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
CREATE TABLE IF NOT EXISTS occurrence_images(
    image_id INTEGER PRIMARY KEY ,
    gbifid BIGINT,
    format	TEXT,
    image_url TEXT,
    license TEXT
    );