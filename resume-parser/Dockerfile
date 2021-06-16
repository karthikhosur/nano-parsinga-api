
FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
# Set environment varibles

COPY ./app /app

WORKDIR /app

RUN apk update

RUN apk add libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig


RUN pip3 install -r requirements.txt


RUN pip3 install textract

# RUN python -c "import nltk;nltk.download('words')"


#RUN python -m nltk.downloader words
