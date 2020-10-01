from flask import Flask, render_template, request
import json
import os
import psycopg2

application = Flask(__name__)
STATIC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/static"

# TODO: use environment variables
conn = psycopg2.connect(dbname="postgres", 
    user="segmed", password="DBPassword", 
     host="aaa36glo5oxh08.ciudugbqudrn.us-west-1.rds.amazonaws.com", 
     port=5432)

@application.route('/')
def home():
    cur = conn.cursor()
    cur.execute("SELECT * FROM photos p ORDER BY p.id")
    photos = cur.fetchall()
    return render_template('index.html', photos=photos)

@application.route('/api/v1/flag', methods=['POST'])
def flagPicture():
    cur = conn.cursor()
    if 'id' not in request.args:
        return 'Must specify id!', 400
    photoId = request.args['id']
    cur.execute("UPDATE photos SET flagged = not flagged WHERE id = %s", (photoId,))
    return ""

if __name__ == "__main__":
    application.run()