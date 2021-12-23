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
    cur.execute("""
    SELECT
      decimalLatitude, decimalLongitude, image_url, verbatimScientificName, eventTime , rights_holder, wiki_url
    FROM
    occurrence_images
    JOIN
    occurrences
    ON
    occurrences.gbifid = occurrence_images.gbifid
    LEFT JOIN
    wiki_info
    on
    wiki_info.scientific_name
    LIKE
    verbatimScientificName GROUP BY occurrences.gbifid  """)
    location_records = cur.fetchall()
    points = [dict(lat=i[0], long=i[1], pic=i[2], name =i[3],eventtime = i[4], rightsholder = i[5], wiki_url = i[6]) for i in location_records]
    if conn:
        cur.close()
        conn.close()
    return render_template('cluster.html',points = points)
'''
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        cursor.execute("SELECT name, author from Book WHERE name
                        LIKE %s OR author LIKE %s", (book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cursor.execute("SELECT name, author from Book")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')
'''
@app.route('/updateserver', methods=['POST']) #github webhook
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/widad/Invasive-species-in-EU-Mapper')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400



