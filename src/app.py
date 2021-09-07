from flask import Flask, request, jsonify
import json
import logging
import uuid
import pandas as pd
from .covidApiClient import CovidApiClient
from datetime import datetime


app = Flask(__name__)

# Read app configurations from config.py
app.config.from_pyfile('config.py')

# Log to a file
logging.basicConfig(filename=app.config['LOG_FILE'], level=logging.DEBUG)


@app.route('/')
def get_covid_reports():

    # Read countries csv
    try:

        df = pd.read_csv(app.config["INPUT_FILE_NAME"])

    except Exception as e:

        app.logger.error(
            "couldn't read iso/date (countries.csv) file with error: {}".format(e))

        return jsonify({"error": "couldn't read the requested csv file. Make sure you have an entry in src/config.py with the key: INPUT_FILE_NAME set"})

    # Create an instance of the ApiClient
    _covidApiClient = CovidApiClient(countries_df=df)

    try:

        results_df = _covidApiClient.get_results()

        # Save dataframe into csv
        result_uuid = uuid.uuid1()

        results_df.to_csv("{}{}.csv".format(
            app.config["OUTPUT_FOLDER"], result_uuid))

    except Exception as e:

        app.logger.error(
            "couldn't retreive the results from the covid-api with error message: {}".format(e))

        return jsonify({"error": "couldn't retreive the results from https://covid-api.com/api/reports/, check the log file in {} for details".format(app.config["LOG_FILE"])})

    if results_df is None:

        return jsonify({"error": "couldn't retreive the results from https://covid-api.com/api/reports/, check the log file in {} for details".format(app.config["LOG_FILE"])})

    return jsonify({"output_file": "{}{}.csv".format(app.config['OUTPUT_FOLDER'], result_uuid)})
