import sqlite3
import logging
import folium
logging.basicConfig(filename='map.log',
                    level=logging.INFO,
                    format='%(asctime)s:Line no-%(lineno)d:%(message)s')
logger = logging.getLogger(__name__)
try:
    conn = sqlite3.connect('euinvasive.sqlite')
except:
    logger.exception('failed to connect to sqlite database')
cur = conn.cursor()
cur.execute("""SELECT  
    decimalLatitude ,
    decimalLongitude 
    FROM occurrences
    LIMIT 1000
""")
location_records = cur.fetchall()

#create map object
m = folium.Map(location=[52.5373, 13.3603],
               tiles = 'Stamen Terrain',
               zoom_start=12)
for point in location_records:
    lat = point[0]
    long = point[1]
    try:
        folium.Marker([point[0], point[1]],
              popup='<strong>observation location</strong>',
              icon=folium.Icon(color='red')).add_to(m)
        logger.info('created marker at {},{}'.format(lat,long))
    except KeyboardInterrupt: # too many data points to render, for now killing it from terminal
        logger.exception('failed at marker {},{}'.format(lat,long))
        break
logger.info('saving map now')
m.save('map.html')
if conn:
        cur.close()
        conn.close()
        logger.info("SQLite connection is closed")
