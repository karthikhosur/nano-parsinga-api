import re 


def email_id_extractor(terms,text):
    try:

        email_id =""
        email_escape_chars =":|,|\-|=|EMAIL|Email|email"

        text =re.sub(email_escape_chars," ",text)

        if re.search("\s@",text):
            text =re.sub("\s@","@",text)
        if re.search("@\s",text):
            text =re.sub("@\s","@",text)
        if re.search("\.\s",text):
            text =re.sub("\.\s",".",text)
        if re.search("\s\.",text):
            text=re.sub("\s\.",".",text)


        if  re.search(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text):
            email_id = re.search(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)[0]
            if len(email_id.split())>2:
                res =email_id.split()
                email_id = res[0]

        emailid_temp = email_id.split(" ")
        if len(emailid_temp)>1:
            email_id = emailid_temp[0]


        #print(email_id)

        return email_id
    except:
        return ""