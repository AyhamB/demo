import pandas as pd
import logging
import requests
from flask import current_app

log = logging.getLogger('demo.covidapiclient')

# covid-api client


class CovidApiClient:

    countries_df = None

    # init method or constructor
    def __init__(self, countries_df):

        self.countries_df = countries_df

    # Get data
    def get_results(self):

        if self.countries_df is None:

            return None

        # Init results df
        results_df = pd.DataFrame(
            columns=['date', 'iso', 'num_confirmed', 'num_deaths', 'num_recovered'])

        for index, row in self.countries_df.iterrows():

            # Create payload
            payload = {
                'iso': row['iso'],
                'date': row['date']
            }

            # GET Request
            try:

                r = requests.get(
                    current_app.config["REPORTS_FULL_URL"], params=payload).json()

            except Exception as e:

                log.error(
                    "couldn't retreive data from covid-api with error: {}\n Make sure you're using YYYY-MM-DD format in the input csv file (default: /input/countries.csv".format(e))

                return None

            # Get summaries
            num_confirmed, num_deaths, num_recovered = self.get_summaries(r)

            # Add results into a result_df
            results_df = results_df.append({'date': row['date'], 'iso': row['iso'], 'num_confirmed': num_confirmed, 'num_deaths': num_deaths, 'num_recovered': num_recovered},
                                           ignore_index=True)

        return results_df

    # Aggregate country data to obtain total summaries for that country
    def get_summaries(self, r):

        # Check data is valid
        if r.get("data") is None or len(r.get("data")) == 0:

            return None, None, None

        # Init
        num_confirmed = 0
        num_deaths = 0
        num_recovered = 0

        for region in r.get("data"):

            num_confirmed = num_confirmed + region.get("confirmed")

            num_deaths = num_deaths + region.get("deaths")

            num_recovered = num_recovered + region.get("recovered")

        return num_confirmed, num_deaths, num_recovered
