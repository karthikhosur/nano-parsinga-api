import re 
# import phonenumbers

def phone_extraction(terms,text):
    phone_list =[]
    c= 0
    # phone_numbers =  phonenumbers.PhoneNumberMatcher(text, None)
    # try:
    #     for pno in phone_numbers:
    #         if c==0:
    #             phone_list.append(pno.raw_string)
    #             c+=1
    # except:
    #     phone_list.append(re.findall(r"\s*(?:\+?(\d{1,3}))?[-. (]*(\d{2,3})[-. )]*(\d{2,3})[-. ]*(\d{3,4,5})(?: *x(\d+))?\s*",text))

    if len(phone_list) ==0 and re.search(r"\s*(?:\+?(\d{1,3}))?[-. (]*(\d{2,3})[-. )]*(\d{2,3})[-. ]*(\d{3,4,5})(?: *x(\d+))?\s*",text) :
        if len(re.search(r"\s*(?:\+?(\d{1,3}))?[-. (]*(\d{2,3})[-. )]*(\d{2,3})[-. ]*(\d{3,4,5})(?: *x(\d+))?\s*",text)[0])>8 : 
            phone_list.append(re.search(r"\s*(?:\+?(\d{1,3}))?[-. (]*(\d{2,3})[-. )]*(\d{2,3})[-. ]*(\d{3,4,5})(?: *x(\d+))?\s*",text)[0])

    if len(phone_list) ==0 and re.search(r"\d{10}|\d{3}\s{1}\d{3}\s{1}\d{4}",text) :
        if len(re.search(r"\d{10}|\d{3}\s{1}\d{3}\s{1}\d{4}",text)[0])>8:
            phone_list.append(re.search(r"\d{10}|\d{3}\s{1}\d{3}\s{1}\d{4}",text)[0])

    if len(phone_list)==0 and re.search(r"\d{3}(-)\d{3}(-)\d{4}",text):
        if len(re.search(r"\d{3}(-)\d{3}(-)\d{4}",text)[0])>8:
            phone_list.append(re.search(r"\d{3}(-)\d{3}(-)\d{4}",text)[0])

    if len(phone_list)==0 and re.search(r"(\()\d{3}(\))(-)\d{3}(-)\d{4}",text) :
        if len(re.search(r"(\()\d{3}(\))(-)\d{3}(-)\d{4}",text)[0])>8:
            phone_list.append(re.search(r"(\()\d{3}(\))(-)\d{3}(-)\d{4}",text)[0])

    if len(phone_list)==0 and re.search(r"(\()\d{3}(\))\s{0,1}\d{3}(-)\d{4}",text) :
        if len(re.search(r"(\()\d{3}(\))\s{0,1}\d{3}(-)\d{4}",text)[0])>8:
            phone_list.append(re.search(r"(\()\d{3}(\))\s{0,1}\d{3}(-)\d{4}",text)[0])

    if len(phone_list)==0 and re.search(r"(\()\d{3}(\))\s{1}\d{3}\s{1}\d{4}",text):
        if len(re.search(r"(\()\d{3}(\))\s{1}\d{3}\s{1}\d{4}",text)[0])>8:
            phone_list.append(re.search(r"(\()\d{3}(\))\s{1}\d{3}\s{1}\d{4}",text)[0])

    if len(phone_list)==0 and re.search(r"\d{3}(.)\d{3}(.)\d{4}",text):
        if len(re.search(r"\d{3}(.)\d{3}(.)\d{4}",text)[0])>8:
            phone_list.append(re.search(r"\d{3}(.)\d{3}(.)\d{4}",text)[0])


    if len(phone_list)==0:
        phone_list.append("")


    isd_code= ""
    if re.search("\+1|\+91|\+971|\+44|\+61|\+81",text):
        isd_code = re.search("\+1|\+91|\+971|\+44|\+61|\+81",text)[0]
    
    
    
    
    temp_isd_code,phone_list = isd_code_extraction(phone_list)

    return isd_code,phone_list[0]


def isd_code_extraction(phone_list):
    isd_code = ""
    try: 
        temp_pno = str(phone_list[0])
        temp_pno = re.sub("\s","",temp_pno)
        if re.search("\+91|\+1|\+971",temp_pno):
            isd_code = re.search("\+91|\+1|\+971",temp_pno)[0]
    except:
        isd_code = ""

    try:
        temp = phone_list[0]
        if len(temp)>10:
                temp= re.sub('[^0-9]+', '', temp)
                temp = temp[-10:]
                phone_list= [temp]
    except :
        phone_list =phone_list 

    return isd_code,phone_list
