
FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
# Set environment varibles

COPY ./app /app

WORKDIR /app

RUN apk update

RUN apk add make automake gcc g++ subversion python3-dev

RUN apt-get install -y libxml2-dev libxslt-dev zlib1g-dev 

RUN pip3 install --upgrade pip
RUN pip3 install lxml
RUN pip3 install -r requirements.txt

RUN apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

RUN pip3 install textract

# RUN python -c "import nltk;nltk.download('words')"


#RUN python -m nltk.downloader words
