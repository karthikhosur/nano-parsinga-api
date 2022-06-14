FROM tiangolo/uvicorn-gunicorn:python3.9-slim

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt

