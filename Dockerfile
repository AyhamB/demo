# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /code
ENV FLASK_APP=./src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --no-cache-dir matplotlib pandas
# Install unit test dependencies
RUN pip install pytest pytest-cov
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

# To run unit tests - uncomment below
#CMD ["pytest"]

# To run unit test - comment out below
CMD ["flask", "run"]