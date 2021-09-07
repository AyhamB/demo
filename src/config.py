"""Flask configuration."""

TESTING = True
DEBUG = True
FLASK_ENV = 'development'

# To maintain context the countries.csv should be placed inside /data.
# By default the file is /data/input/countries.csv
INPUT_FILE_NAME = '/data/input/countries.csv'

# To maintain context the output directory should be placed inside /data.
OUTPUT_FOLDER = '/data/output/'

# Log file
LOG_DIR = "/data/log/"
LOG_FILE = LOG_DIR + "demo.log"

API_BASE_URL = "https://covid-api.com/api"
REPORTS_ENDPOINT = "/reports"
REPORTS_FULL_URL = API_BASE_URL + REPORTS_ENDPOINT
