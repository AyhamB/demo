# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /code
ENV FLASK_APP=./src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --no-cache-dir matplotlib pandas
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]