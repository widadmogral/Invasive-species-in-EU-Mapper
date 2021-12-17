import sqlite3
import csv
def load_to_db(csvfile):
    con = sqlite3.connect('euinvasive.sqlite')
    cur = con.cursor()
    with open(csvfile, 'rt', encoding='utf-8') as f:  # default is that first line are the headers
        dr = csv.DictReader(f, delimiter='\t')  # comma is default delimiter,changing it to \t
        next(dr)  # skip header
        to_db = [(i['gbifID'], i['datasetName'], i['eventDate'], i['countryCode'], i['decimalLatitude'],
                  i['decimalLongitude'], i['taxonKey'], i['verbatimScientificName']) for i in dr]

    cur.executemany(
        "INSERT OR IGNORE INTO occurrences (gbifid, datasetName, eventTime, countryCode, decimalLatitude, decimalLongitude, taxonkey, verbatimScientificName) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        to_db)
    con.commit()
    con.close()
qry = open('create_occurrences.sql', 'r').read()
conn = sqlite3.connect('euinvasive.sqlite')
cur = conn.cursor()
cur.executescript(qry)
cur.close()
conn.commit()
conn.close()
load_to_db('loadtodb.tsv')
