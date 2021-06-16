
FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
# Set environment varibles

COPY ./app /app

WORKDIR /app

RUN apk update

RUN apk add cython libxml2-dev antiword poppler-utils tesseract-ocr flac ffmpeg lame  swig


RUN pip3 install -r requirements.txt


RUN pip3 install textract

# RUN python -c "import nltk;nltk.download('words')"


#RUN python -m nltk.downloader words
