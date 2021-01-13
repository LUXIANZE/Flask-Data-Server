from flask import Flask
import pymongo 
import ssl

CONNECTION_STRING = "mongodb+srv://LU-Developer-98:stJK1QzNedyCQwLL@lu-dev-cluster-5pzdu.mongodb.net/CDSS?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING, ssl_cert_reqs=ssl.CERT_NONE)
db = client.get_database('CDSS') 
reports_collection = db.reports 
patients_collection = db.patients