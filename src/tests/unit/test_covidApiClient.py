from ...covidApiClient import CovidApiClient
import pandas as pd


def test_covidApiClientInit():
    """
    GIVEN a covidApiClient instance
    WHEN a new covidApiClient is created
    THEN check the pandas dataframe is initialized correctly
    """
    countries_df = pd.DataFrame(columns=['date', 'iso'])
    countries_df = countries_df.append(
        {'date': "2020-04-09", 'iso': 'USA'}, ignore_index=True)
    _covidApiClient = CovidApiClient(countries_df=countries_df)
    assert _covidApiClient.countries_df.iso[0] == "USA"


def test_covidApiClientGetSummaries():
    """
    GIVEN a covidApiClient instance
    WHEN a get summaries is passed a json with valid return from covid-api, it calculates the summaries
    THEN check the summaries for num_confirmed, num_deaths, num_recovered are correct
    """
    json_response = {
        "data": [
            {
                "date": "2020-04-16",
                "confirmed": 9840,
                "deaths": 490,
                "recovered": 0,
                "confirmed_diff": 1393,
                "deaths_diff": 105,
                "recovered_diff": 0,
                "last_update": "2020-04-16 23:38:03",
                "active": 9350,
                "active_diff": 1288,
                "fatality_rate": 0.0498,
                "region": {
                    "iso": "CAN",
                    "name": "Canada",
                    "province": "Ontario",
                    "lat": "51.2538",
                    "long": "-85.3232",
                    "cities": []
                }
            },
            {
                "date": "2020-04-16",
                "confirmed": 1561,
                "deaths": 75,
                "recovered": 0,
                "confirmed_diff": 44,
                "deaths_diff": 3,
                "recovered_diff": 0,
                "last_update": "2020-04-16 23:38:03",
                "active": 1486,
                "active_diff": 41,
                "fatality_rate": 0.048,
                "region": {
                    "iso": "CAN",
                    "name": "Canada",
                    "province": "British Columbia",
                    "lat": "53.7267",
                    "long": "-127.6476",
                    "cities": []
                }
            }
        ]
    }

    _covidApiClient = CovidApiClient(countries_df=None)

    num_confirmed, num_deaths, num_recovered = _covidApiClient.get_summaries(
        json_response)

    assert num_confirmed == 11401
    assert num_deaths == 565
    assert num_recovered == 0
