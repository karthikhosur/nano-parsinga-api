
FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
# Set environment varibles

COPY ./app /app

WORKDIR /app

RUN apk update

RUN apk add cython  g++ gcc libxslt-dev py-lxml python3-dev libxml2-dev antiword poppler-utils tesseract-ocr flac ffmpeg lame  swig
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip3 install -r requirements.txt


RUN pip3 install textract
 
# RUN python -c "import nltk;nltk.download('words')"


#RUN python -m nltk.downloader words
