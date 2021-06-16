import re
import os
from .skills import skills_extract

temp_result = {
    "exp_text": "",
    "exp_history": 
        [{"id": "",
        "organization": "",
        "job_designation": "",
        "start_date": "",
        "end_date": ""}],
    "workex_skills": []
    }



exp_heading = "XPERIENCE|MPLOYMENT|AREER"
exp_heading_2 = "Experience|ROFESSIONAL|Professional|Career|Employment"
end_heading = "DUCATION|ERSONAL"
end_heading_2 = "DUCATION|ERSONAL|CADEMIC|Education|Acadmic|Personal"


company_end_titles ="Corporation|Institute|Studios|University|Strategists|Limited|LIMITED|LLC|llc|L\.L\.C|limited|LTD|Ltd|LTd|Ltd|Ldt|LDT|ltd|group|Group|GROUP|Bank|Financial Services|Scientific|Technology Solution|Technologies|Consulting|GLOBAL SERVICES|agency|Corp|Scientific"
not_exp_word = "bjective|summary"

current = "present|current|till|onwards"
year_range = "1985|1986|1987|1989|1990|1991|1992|1993|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021"
month_range= "jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"
digit_year_range ="85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20"
digit_month_range = "1|2|3|4|5|6|7|8|9|10|11|12"


def experience_text(terms):

    #Check for Capital Titles
    chk = 0
    temp_terms = []
    for i in range(len(terms)):
        if re.search(exp_heading,terms[i]) and  len(terms[i].split())<4 and not re.search(not_exp_word,terms[i].lower()):
            temp_terms = terms[i:]
            chk =1
            break
    
    if not len(temp_terms) == 0:
        terms = temp_terms

        for i in range(len(terms)):
            if re.search(end_heading,terms[i]) and  len(terms[i].split())<6:
                temp_terms =terms[:i]
                break

        terms = temp_terms
    
    if not chk ==1:
        # Check for small titles 

        temp_terms = []
        for i in range(len(terms)):
            if re.search(exp_heading_2,terms[i]) and  len(terms[i].split())<4:
                temp_terms = terms[i:]
                break
        terms = temp_terms

        for i in range(len(terms)):
            if re.search(end_heading_2,terms[i]) and  len(terms[i].split())<6:
                temp_terms =terms[:i]
                break

        terms = temp_terms


    return terms 



def extract_experience(terms):
    exp_result = {
    "exp_text": "",
    "exp_history": 
        [{"id": "",
        "organization": "",
        "job_designation": "",
        "start_date": "",
        "end_date": ""}],
    "workex_skills": []
    }
    
    exp_text = ""
   
    try:
        terms=experience_text(terms)

        for i in range(len(terms)):
            exp_text =exp_text +" "+terms[i]

        
        total_dur = duration_experience(terms)
        present_employer = extract_present_employer(terms)
        present_designation = extract_present_designation(terms)
        workex_skill = skills_extract(exp_text)

        exp_result["exp_text"] = exp_text
        exp_result["exp_history"][0]["id"]=str(0)
        exp_result["exp_history"][0]["organization"] = present_employer
        exp_result["exp_history"][0]["job_designation"]= present_designation
        exp_result["workex_skills"] = workex_skill

        return exp_result,total_dur
    except:
        return temp_result,"0"


def duration_experience(terms):
    try:
        year_range = "1985|1986|1987|1989|1990|1991|1992|1993|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021"
        two_digit_year_range = "85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20"
        min_year = 2100
        res = []
        
        for i in range(len(terms)):
            temp = terms[i].split()
            res = res + temp

        for i in range(len(res)):
            if re.search(year_range,res[i]):
                
                if int(re.search(year_range,res[i])[0]) <min_year:
                    min_year = int(re.search(year_range,res[i])[0])

        
        if min_year<2022:
            total_dur =2021-min_year
        else :
            total_dur =0

        min_year = 2100
        if total_dur == 0:
            for i in range(len(res)):
                    if re.search(two_digit_year_range,res[i]):
                        if int(re.search(two_digit_year_range,res[i])[0])<21:
                            min_year = int(re.search(two_digit_year_range,res[i])[0])+2000
                        elif int(re.search(two_digit_year_range,res[i])[0])>84:
                            min_year = int(re.search(two_digit_year_range,res[i])[0])+1900


            if min_year<2022:
                total_dur =2021-min_year
            else :
                total_dur =0



        return str(total_dur)

    except:
        return "0"


def extract_present_employer(terms):
    try:
        present_employer = ""
        for i in range(len(terms)):
            if re.search(company_end_titles,terms[i]):
                present_employer=terms[i]
                break
        
        return present_employer
    except:
        return ""


def extract_present_designation(terms):
    try:
        present_designation = ""
        terms_txt = ""
        for i in range(len(terms)):
            terms_txt = terms_txt + " "+ terms[i]



        return present_designation
    except:
        return ""