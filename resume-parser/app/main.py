from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.param_functions import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.base import SecurityBase
from pydantic import BaseModel
from base64 import b64decode,b64encode
import base64
from model.main import main
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    base64file: str
    file_name: str
	#api_key : str

class Item1(BaseModel):
    skill_title: str


class Item2(BaseModel):
    job_title: str

class Item3(BaseModel):
    wrong_name: str


@app.get("/")from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.param_functions import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.base import SecurityBase
from pydantic import BaseModel
from base64 import b64decode,b64encode
import base64
from model.main import main
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    base64file: str
    file_name: str
	#api_key : str

class Item1(BaseModel):
    skill_title: str


class Item2(BaseModel):
    job_title: str

class Item3(BaseModel):
    wrong_name: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/v2/fileupload")
async def fileupload(image: UploadFile = File(...)):
        filename = str(image.filename)
        temp_filename = filename
        
        filename = (filename.partition('.'))
        filetype = filename[2].lower()

        with open(temp_filename,'wb+') as f:
            f.write(image.file.read())
            f.close()

        results = main(temp_filename,filetype)
        os.remove(temp_filename)
        return results

@app.post("/v2/resumesbase64")
async def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title= filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename,'wb+') as f:
            f.write(bytes)
            f.close()
            
    results = main(temp_filename,filetype)
    os.remove(temp_filename)
    return results



@app.post("/v1/fileupload")
async def fileupload(image: UploadFile = File(...)):
        filename = str(image.filename)
        temp_filename = filename
        
        filename = (filename.partition('.'))
        filetype = filename[2].lower()

        with open(temp_filename,'wb+') as f:
            f.write(image.file.read())
            f.close()

        results = main(temp_filename,filetype)
        os.remove(temp_filename)
        return results

@app.post("/v1/resumesbase64")
async def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title= filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename,'wb+') as f:
            f.write(bytes)
            f.close()
            
    results = main(temp_filename,filetype)
    os.remove(temp_filename)
    return results

@app.post("/skills")
async def create_item(item: Item1):
	skill_name = item.skill_title
	return True
	
	
@app.post("/job_designation")
async def create_item(item: Item2):
	job_name = item.job_title
	return True
	
	
@app.post("/wrong_name")
async def create_item(item: Item3):
	wrong_name = item.wrong_name
	return True
async def root():
    return {"message": "Hello World"}


@app.post("/v2/fileupload")
async def fileupload(image: UploadFile = File(...)):
        filename = str(image.filename)
        temp_filename = filename
        
        filename = (filename.partition('.'))
        filetype = filename[2].lower()

        with open(temp_filename,'wb+') as f:
            f.write(image.file.read())
            f.close()

        results = main(temp_filename,filetype)
        os.remove(temp_filename)
        return results

@app.post("/v2/resumesbase64")
async def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title= filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename,'wb+') as f:
            f.write(bytes)
            f.close()
            
    results = main(temp_filename,filetype)
    os.remove(temp_filename)
    return results



@app.post("/v1/fileupload")
async def fileupload(image: UploadFile = File(...)):
        filename = str(image.filename)
        temp_filename = filename
        
        filename = (filename.partition('.'))
        filetype = filename[2].lower()

        with open(temp_filename,'wb+') as f:
            f.write(image.file.read())
            f.close()

        results = main(temp_filename,filetype)
        os.remove(temp_filename)
        return results

@app.post("/v1/resumesbase64")
async def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title= filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename,'wb+') as f:
            f.write(bytes)
            f.close()
            
    results = main(temp_filename,filetype)
    os.remove(temp_filename)
    return results

@app.post("/skills")
async def create_item(item: Item1):
	skill_name = item.skill_title
	return True
	
	
@app.post("/job_designation")
async def create_item(item: Item2):
	job_name = item.job_title
	return True
	
	
@app.post("/wrong_name")
async def create_item(item: Item3):
	wrong_name = item.wrong_name
	return True