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
LOG_FILE = "/data/log/demo.log"
