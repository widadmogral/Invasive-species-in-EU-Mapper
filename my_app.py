from flask import Flask, request
from flask import render_template
import sqlite3
import git
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['DEBUG'] = True

@app.route('/')
@app.route('/home')
def create_map():
    conn = sqlite3.connect('euinvasive.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT  decimalLatitude, decimalLongitude, image_url, verbatimScientificName, eventTime , rights_holder FROM occurrences JOIN occurrence_images ON occurrences.gbifid = occurrence_images.gbifid GROUP BY occurrences.gbifid 
                            """)
    location_records = cur.fetchall()
    points = [dict(lat=i[0], long=i[1], pic=i[2], name =i[3],eventtime = i[4], rightsholder = i[5]) for i in location_records]
    if conn:
        cur.close()
        conn.close()
    return render_template('cluster.html',points = points)

@app.route('/updateserver', methods=['POST']) #github webhook
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/widad/Invasive-species-in-EU-Mapper')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400



