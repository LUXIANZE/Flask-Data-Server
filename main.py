from flask import Flask
from flask import request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Server Healthy'

@app.route('/report', methods=['POST'])
def report():
    if request.method == 'POST':
        payload = request.json

        print("payload: "+ str(payload))
        db.reports_collection.insert_one({"mRNNumber":payload['mRNNumber'], "report":payload['report'], "date":payload['date']})
        return "Success"

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        payload = request.json

        print("payload: " + str(payload))
        doc = db.patients_collection.find_one({"mRNNumber": payload['mRNNumber']})
        print("doc: " + str(doc))
        if doc['ic'] == payload['ic'] :
            return "Success"
        else:
            return 'Patient not found', 404


