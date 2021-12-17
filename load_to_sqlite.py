import sqlite3
import csv

qry = open('create_occurrences.sql', 'r').read()
conn = sqlite3.connect('euinvasive.sqlite')
cur = conn.cursor()
cur.executescript(qry)
cur.close()
conn.commit()
conn.close()
'''
with open('loadtodb.tsv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'occurrences', sep='\t', null = "")

conn.commit()
'''

def load_to_db(csvfile):
    con = sqlite3.connect('euinvasive.sqlite')
    cur = con.cursor()
    with open(csvfile, 'rt', encoding='utf-8') as f:  # default is that first line are the headers
        dr = csv.DictReader(f, delimiter='\t')  # comma is default delimiter,changing it to \001
        next(dr)  # skip header
        to_db = [(i['gbifID'], i['datasetName'], i['eventDate'], i['countryCode'], i['decimalLatitude'],
                  i['decimalLongitude'], i['taxonKey'], i['verbatimScientificName']) for i in dr]

    cur.executemany(
        "INSERT INTO occurrences (gbifid, datasetName, eventTime, countryCode, decimalLatitude, decimalLongitude, taxonkey, verbatimScientificName) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        to_db)
    con.commit()
    con.close()


load_to_db('loadtodb.tsv')
