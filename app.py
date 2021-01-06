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

        db.col.insert_one({"mRNNumber":payload['mRNNumber'], "report":payload['report'], "date":payload['date']})
        return "Success"
