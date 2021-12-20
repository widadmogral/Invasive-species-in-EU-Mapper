from flask import Flask
from flask import render_template
import sqlite3
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['DEBUG'] = True

conn = sqlite3.connect('euinvasive.sqlite')
cur = conn.cursor()
cur.execute("""SELECT  decimalLatitude
                       ,decimalLongitude
                       ,image_url
                        FROM
                        occurrences JOIN occurrence_images
                        ON occurrences.gbifid = occurrence_images.gbifid;

""")
location_records = cur.fetchall()
points = [dict(lat = i[0], long = i[1], pic = i[2]) for i in location_records]
if conn:
        cur.close()
        conn.close()
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('cluster.html',points = points)

#return render_template("m.html")
