import re


not_names = "email|phone|SUMMARY|professional|experience|education|job|personal|information|Objective|contact|profile|careers|objectives|experience|college|university|education|description|date|internal|administration|Phone"

def name_extractor_new(text, terms, email_id, file_type, filename, phone):
    name_text = ""
    
    # Indian Names Module
    # If Naukri Resume
    
    name_text = indian_names_module(terms,text)

    return name_text

def naukri_resume_name(terms,text):
    name_text = ""
    if "Desired Job Details"  in text and "Affirmative Action" in text and "Other Details" in text:
        name_text = terms[0]
    return name_text

def indian_names_module(terms,text):
    name_text = ""
    name_text = naukri_resume_name(terms,text)
    
    if name_text.isspace() and len(name_text.split()) < 5:
        name_text = name_search_mention(terms)
        

    if  name_text.isspace() and len(name_text.split()) < 5: 
        name_text = name_search_suffix(terms)
   
    
    return name_text

def name_search_mention(terms):
    name_text = ""
    for i in range(len(terms)):
            if len(terms[i].split()) <7:
                if re.search("name|n ame", terms[i].lower()) and not re.search("father|project|mother|company", terms[i].lower()):
                    name_text = terms[i].lower()
                    name_text = re.sub("name|n ame", "", name_text)
                    name_text = re.sub("\.|:|=", "", name_text)
        
    return name_text.upper()





def name_search_suffix(terms):
    common_indian_names  = "Patel|Sharma|Dangi|Dhawan|Shah|Chauhan|Chavan|Chaudhari|Chaudhary|Chaudhry|Singh|Patel|Reddy|Konda|Kumar|Gupta|Yadav|Agarwal|Pandey|Mukherjee|Chatterjee|Kapoor|Mehta|Tyagi|Khan|Desai|Joshi|Mehta|Srinivasan|Iyer|Nair|Malhotra|Verma"
    for i in range(len(terms)):
        if re.search(common_indian_names,terms[i], re.IGNORECASE):
            if re.search(not_names, terms[i], re.IGNORECASE):
                if len(terms[i].split()) > 1 and len(terms[i].split()) < 7:
                    return terms[i]
    return ""


def name_text_edit(name_text):
    try:
        name_text = re.sub("\s+|\-|\|", " ", name_text)
        name_text = re.sub("[^a-zA-Z\s]+", " ", name_text)
        res = name_text.split()
        name_text = ""
        for i in range(len(res)):
            if res[i][0].isupper():
                name_text = name_text+" " + res[i]

        if len(name_text.split()) > 3 and len(name_text) > 22:
            res = name_text.split()
            temp = ""
            for i in range(0, 3):
                temp = temp + " " + res[i]
            name_text = temp

        return name_text
    except:
        return ""

