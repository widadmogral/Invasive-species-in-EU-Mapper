import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password = password")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS occurrences(
    gbifid BIGINT PRIMARY KEY,
    datasetName VARCHAR(200),
    eventTime  timestamp,
    countryCode VARCHAR(3),
    decimalLatitude NUMERIC(8,6),
    decimalLongitude NUMERIC(8,6),
    taxonkey bigint,
    verbatimScientificName VARCHAR(200)
)
""")

with open('loadtodb.tsv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'occurrences', sep='\t', null = "")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS occurrence_images(
    gbifid bigint,
    imageformat varchar(50),
    imagelink VARCHAR(500),
    license VARCHAR(100)
)
""")

with open('media.tsv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'occurrence_images', sep='\t', null = "")
conn.commit()

cur.execute("""ALTER TABLE occurrence_images ADD COLUMN imageid BIGSERIAL PRIMARY KEY;""")

conn.commit()
if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
