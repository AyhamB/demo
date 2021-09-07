# covid-api demo application
Demo application using Flask, Docker, and Pytest

# QuickStart
Clone this repo and run 
```sh
docker-compose build
docker-compose up
```
Using `postman` or a browser, make the following GET request
`http://localhost:5000/`
This endpoint will return the location of the output excel file. Here is a sample output
```json
{
    "output_file": "/data/output/37536460-0fe0-11ec-98d1-0242ac140002.csv"
}
```


# Getting Started
This is a dockerized Flask application, you need to have docker and docker-compose installed to run it
## Prerequisites
- **Docker**: Please follow the [official installation](https://docs.docker.com/compose/install/) guide
- **Docker Compose**: Please follow the [official installation](https://docs.docker.com/get-docker/) guide

## Configuration
The configuration file is located at `src/config.py`.
#### INPUT_FILE_NAME
This is the file name of the input excel `countries.csv` , by default this file is located at `/data/input/countries.csv`
 Below are the default configurations
```py
# To maintain context, the countries.csv should be placed inside /data.
# By default the file is /data/input/countries.csv
INPUT_FILE_NAME = '/data/input/countries.csv'
```
#### OUTPUT_FOLDER
This is the location where the output excel containing the results will be located at. The output filename is unique per each request and will be returned for each GET request. By default the output folder set to '/data/output/`
```py
# To maintain context the output directory should be placed inside /data.
OUTPUT_FOLDER = '/data/output/'
```
#### LOG_FILE
The log file contains all logs for all requests made to the application. At this point the log level is set to info. By default the log file is at '/data/log/demo.log`
```py
# Log file
LOG_FILE = "/data/log/demo.log"
```

## Building the application
From the project root execute
```sh
docker-compose build
docker-compose up
```
This will create the container and run the flask application using port `5000`

## Running the app
This application has only one endpoint at `/`. After setting the desired values of `/data/input/countries.csv` execute the following GET request using either `postman` or your browser
`http://localhost:5000/`

This endpoint will return the location and filename of the output excel file with the results.


## Running unit tests
This app uses `pytest`. Tests live in `/src/tests/unit/`. To run the unit tests modify the DockerFile as follows
```py
# To run unit tests - uncomment below
CMD ["pytest"]

# To run unit test - comment out below
#CMD ["flask", "run"]
```
Then run 
```sh
docker-compose build
docker-compose up
```
