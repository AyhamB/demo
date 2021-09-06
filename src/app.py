from flask import Flask, request, jsonify
import json
import logging
import uuid

app = Flask(__name__)

# Read app configurations from config.py
app.config.from_pyfile('config.py')

# Log to a file
logging.basicConfig(filename=app.config['LOG_FILE'], level=logging.DEBUG)


@app.route('/')
def get_covid_reports():

    return jsonify({"Output_file": "{}{}.csv".format(app.config['OUTPUT_FOLDER'], uuid.uuid1())})
