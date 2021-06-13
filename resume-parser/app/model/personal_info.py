import re
import pgeocode
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
import os


nlp = spacy.load('en_core_web_sm')

personal_info_headings= ["personal"]

base_path = os.path.dirname(__file__)



file = os.path.join(base_path,"list_cities_ind.txt")
file = open(file, "r", encoding='utf-8')
location_nlp = [line.strip().lower() for line in file]
locationmatcher_ind = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(text) for text in location_nlp if len(nlp.make_doc(text)) < 10]
locationmatcher_ind.add("Location Address", None, *patterns)


file1 = os.path.join(base_path,"list_cities_us.txt")
file1 = open(file1, "r", encoding='utf-8')
location_nlp = [line.strip().lower() for line in file1]
locationmatcher_us = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(text) for text in location_nlp if len(nlp.make_doc(text)) < 10]
locationmatcher_us.add("Location Address", None, *patterns)


def extract_address(temp_line_text):
    # india code =0 and us code =1 
    country_code = 1 
    address={"postal_code":" ","place_name":" ","state_name":" ","city_name":" ","area_name":" ","longitude":" ","latitude":""}
    pincode = ""
    backup_temp_line_text =temp_line_text
    if re.search(r"\b\d{3}\s{0,1}\d{3}\b",temp_line_text):
        ind_pincode =str(re.search(r"\b\d{3}\s{0,1}\d{3}\b",temp_line_text)[0])
        if int(ind_pincode[0])>0 and int(ind_pincode[0])<9:
            pincode = ind_pincode


    if len(pincode)>0:
        if len(str(pincode))==6:
            nomi = pgeocode.Nominatim('in')
            #print(nomi.query_postal_code(str(pincode))["place_name"])
            address["postal_code"]= str(nomi.query_postal_code(str(pincode))["postal_code"])
            address["place_name"]= str(nomi.query_postal_code(str(pincode))["place_name"])
            address["state_name"]= str(nomi.query_postal_code(str(pincode))["state_name"])
            address["city_name"]= str(nomi.query_postal_code(str(pincode))["county_name"])
            address["area_name"]= str(nomi.query_postal_code(str(pincode))["community_name"])
            address["longitude"]= str(nomi.query_postal_code(str(pincode))["longitude"])
            address["latitude"]= str(nomi.query_postal_code(str(pincode))["latitude"])
            country_code = 0




    elif re.search(r"\b\d{5}([-+]?\d{4})?\b",temp_line_text):
        us_pincode=str(re.search(r"\b\d{5}([-+]?\d{4})?\b",temp_line_text)[0])
        if int(us_pincode[0])>0 and int(us_pincode[0])<9:
            pincode =us_pincode


    if re.search(r"\b\d{5}\b",temp_line_text):
        us_zipcode = re.search(r"\b\d{5}\b",temp_line_text)[0]
        pincode =us_zipcode


    if len(pincode)>0:
        if len(str(pincode))==5:
            nomi = pgeocode.Nominatim('us')
            #print(nomi.query_postal_code(str(pincode))["place_name"])
            address["postal_code"]= str(nomi.query_postal_code(str(pincode))["postal_code"])
            address["place_name"]= str(nomi.query_postal_code(str(pincode))["place_name"])
            address["state_name"]= str(nomi.query_postal_code(str(pincode))["state_name"])
            address["city_name"]= str(nomi.query_postal_code(str(pincode))["county_name"])
            address["area_name"]= str(nomi.query_postal_code(str(pincode))["community_name"])
            address["longitude"]= str(nomi.query_postal_code(str(pincode))["longitude"])
            address["latitude"]= str(nomi.query_postal_code(str(pincode))["latitude"])

    if address["postal_code"] =="NaN" or address["postal_code"] =="i" or address["postal_code"] =="None":
        address["postal_code"]=" "
    if address["place_name"] =="NaN" or address["place_name"] =="i" or address["place_name"] =="None" or len(address["place_name"])<5:
        address["place_name"]=" "
        address["state_name"] =" "
        address["city_name"]=" "
    if address["state_name"] =="NaN" or address["state_name"] =="i" or address["state_name"] =="None":
        address["state_name"]=" "
    if address["city_name"] =="NaN" or address["city_name"] =="i" or address["city_name"] =="None":
        address["city_name"]=" "
    if address["area_name"] =="NaN"  or address["area_name"] =="i" or address["area_name"] =="None":
        address["area_name"]=" "
    if address["longitude"] =="NaN":
        address["longitude"]=" " 
    if address["latitude"] =="NaN":
        address["latitude"]=" "

    if address["postal_code"] == " ":
        location_extra=[]
        #print(skill_text)
        try:
            temp_line_text=temp_line_text.lower()
            nlp_new = nlp(temp_line_text)
            matches = locationmatcher_ind(nlp_new)
            for match_id, start, end in matches:
                span = nlp_new[start:end]
                location_extra.append(span.text)
                address["place_name"] = span.text
                address["city_name"] = span.text
                country_code = 0
        except:
            location_extra = []

    if address["place_name"] == " ":
        location_extra=[]
        #print(skill_text)
        try:
            state_name = "" 

            
            temp_line_text = re.sub(",|\.|-|:"," ",temp_line_text)
            if re.search("AL|AZ|AR|CA|CO|CT|DE|FL|GA|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",backup_temp_line_text):
                state_name= re.search("AL|AZ|AR|CA|CO|CT|DE|FL|GA|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY",backup_temp_line_text)[0]
            elif re.search("alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|district of columbia|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|maryland|massachusetts|michigan|minnesota|mississippi|missouri|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming",temp_line_text.lower()):
                state_name =re.search("alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|district of columbia|florida|georgia|hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|montana|nebraska|nevada|new hampshire|new jersey|new mexico|new york|north carolina|north dakota|ohio|oklahoma|oregon|maryland|massachusetts|michigan|minnesota|mississippi|missouri|pennsylvania|rhode island|south carolina|south dakota|tennessee|texas|utah|vermont|virginia|washington|west virginia|wisconsin|wyoming",temp_line_text.lower())[0]
            place_name= ""
            if state_name != "":
                res = temp_line_text.split()
                for i in range(len(res)):
                    if state_name.lower()  in res[i]:
                        place_name = res[i-1]
                        country_code = 1 
                        break

            address["place_name"] = place_name
            address["city_name"] = place_name
            address["state_name"] = state_name

        except: 
            location_extra = []

    # print(address)
    return address,country_code

def extract_dob(text):
    try:
        birth_date = ""
        match_dob=""
        dob_words = "Born on|Date of birth|DOB :|DOB|DOB:|DATE OF BIRTH|Birth Date|Birth :|D.O.B|d. o. b|d o b|d  o  b|date and place of birth:|date and place of birth|date and country of birth|dateofbirth|data of birth|date of  birth|birthdate|date of birth/age:|date of birth/age|date of birthage|b\\'date|b’date|date  of  birth|date of birth|date ofbirth|dob|date & place of birth|d.o.b|date of birth|date-of-birth|date   of   birth|BORN:"
        date_text = ""
        if re.search(dob_words,text):
            date_end = re.search(dob_words,text).end() 
            date_text = text[date_end:date_end+20]
            print("date : ", date_text)
            if re.search("\d{4}",date_text):
                date_end = re.search("\d{4}",date_text).end()
                date_text =date_text[:date_end]
            if not re.search("\d{4}|\d{2}",date_text):
                date_text= ""
        return date_text
    except:
        return ""

def extract_gender(text):
    try:
        gender =""
        re_gender = "Male|MALE|FEMALE|Female|female|male"

        if re.search(re_gender,text):
            gender =re.search(re_gender,text)[0]

        return gender
    except:
        return ""
