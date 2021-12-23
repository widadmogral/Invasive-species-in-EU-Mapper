import csv
import sqlite3
import logging
logging.basicConfig(filename='database_load.log',
                    level=logging.INFO,
                    format='%(asctime)s:Line no-%(lineno)d:%(message)s')
logger = logging.getLogger(__name__)
def load_to_occurrences(csvfile):
    con = sqlite3.connect('euinvasive.sqlite')
    cur = con.cursor()
    with open(csvfile, 'rt', encoding='utf-8') as f:  # default is that first line are the headers
        dr = csv.DictReader(f, delimiter='\t')  # comma is default delimiter,changing it to \t
        to_db = [(i['gbifID'], i['datasetName'], i['eventDate'], i['countryCode'], i['decimalLatitude'],
                  i['decimalLongitude'], i['taxonKey'], i['verbatimScientificName']) for i in dr]

    cur.executemany(
        "INSERT OR IGNORE INTO occurrences (gbifid"
        ", datasetName"
        ", eventTime"
        ", countryCode"
        ", decimalLatitude"
        ", decimalLongitude,"
        " taxonkey,"
        " verbatimScientificName) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
        to_db)
    con.commit()
    con.close()


def load_to_occurrence_images(csvfile):
    con = sqlite3.connect('euinvasive.sqlite')
    cur = con.cursor()
    with open(csvfile, 'rt', encoding='utf-8') as f:  # default is that first line are the headers
        dr = csv.DictReader(f, delimiter='\t')  # comma is default delimiter,changing it to \t
        to_db = [(i['gbifID'], i['identifier'], i['license'], i['rightsHolder']) for i in dr]

    cur.executemany(
        "INSERT OR IGNORE INTO occurrence_images (gbifid, image_url, license, rights_holder) VALUES (?, ?, ?, ?);",to_db)
    con.commit()
    con.close()

def load_to_wiki_info(csvfile):
    con = sqlite3.connect('euinvasive.sqlite')
    cur = con.cursor()
    with open(csvfile, 'rt', encoding='utf-8') as f:  # default is that first line are the headers
        dr = csv.DictReader(f, delimiter='\001')  # comma is default delimiter,changing it to \001
        to_db = [(i['verbatimScientificName'], i['wiki_url']) for i in dr]

    cur.executemany(
        "INSERT OR IGNORE INTO wiki_info (scientific_name,wiki_url) VALUES (?, ?);",
        to_db)
    con.commit()
    con.close()
def create_db():
    try:
        qry = open('create_occurrences.sql', 'r').read()
    except:
        logger.exception('failed to create sql database')
    conn = sqlite3.connect('euinvasive.sqlite')
    cur = conn.cursor()
    cur.executescript(qry)
    cur.close()
    conn.commit()
    conn.close()
def main():
    create_db()
    try:
        load_to_occurrences('loadtodb.tsv')
        logger.info('Loaded file to occurrences table in database')
    except:
        logger.exception('Unable to load to occurrence table in database')
    try:
        load_to_occurrence_images('media.tsv')
        logger.exception('Loaded to occurrence_images table in database')
    except:
        logger.exception('Unable to load to occurrence_images table in database')
    try:
        load_to_wiki_info('wiki_info.csv')
        logger.info('Loaded to wiki_info table in database')
    except:
        logger.exception('Unable to load to wiki_info table in database')
if __name__ =="__main__":
    main()
