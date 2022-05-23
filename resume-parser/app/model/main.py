import textract
import re
from .name_parser import name_extractor
from .email_id import email_id_extractor
from .phone import phone_extraction
from .skills import skills_extract
from .personal_info import extract_address, extract_dob, extract_gender, passport_no
from .experience import extract_experience
from .education import extract_education
from .industry import industry_class
import concurrent.futures
from PIL import Image


result_template = {
    "personal_info": [
        {
            "name": [
                ""
            ],
            "phone": [
                ""
            ],
            "isd_code": [
                ""
            ],
            "email": [
                ""
            ],
            "url": [
                ""
            ],
            "address": [
                {
                    "postal_code": " ",
                    "place_name": "",
                    "state_name": "",
                    "city_name": "",
                    "area_name": " ",
                    "longitude": " ",
                    "latitude": ""
                }
            ],
            "passport_no": "",
            "dob": "",
            "gender": ""
        }
    ],
    "education": {
        "edu_text": "",
        "edu_history": [
            {
                "id": "",
                "degree": "",
                "university": "",
                "grade": "",
                "graduation_year": ""
            }
        ]
    },
    "experience": {
        "exp_text": "",
        "exp_history": [
            {
                "id": "",
                "organization": "",
                "job_designation": "",
                "start_date": "",
                "end_date": ""
            }
        ],
        "workex_skills": []
    },
    "total_experience": "0",
    "priority_skills": [
        []
    ],
    "all_skills": [
        []
    ],
    "other_sections": [
        []
    ],
    "text": [
        ""
    ],
    "industry": ""
}


def main(file_name, file_type):
    try:

        s = textract.process(file_name)

        filename = re.sub("pdf|doc|docx|\.", "", file_name)

        text = str(s, 'utf-8', 'ignore')
        skills_list = []

        text = re.sub("\\xad|\\u200b|\\t|\t", " ", text)
        temp_terms = []
        exclude_re = "Bio-Data|BIODATA|RE S U M E|R E S U M E|Bio data|P a g e|biodata|Page|PAGE|page|CURRICULUMVITAE|CURRICULAM VITAE|CURRICULUM VITAE|●|Curriculum Vitae|CV|Resume|RESUME|CONFIDENTIAL|Look forward|My CV is detailed below|Work is Worship|Not keen on sales" + "|DSP MERRILYNCH|Private & Confidential|(Private and Confidential)" + "|Private and Confidential|Please feel free to contact|Moved to" + "|a manager who is……..|Here is the resume of the applicant|trial version can convert" + "|(this message is omitted in registered version)|converted by activertf trial version" + "|planman consulting|referred|reffered|Last active|Last Modified|NOT LOOKING FOR CHANGE" + "|Timesjobs profile|Jobstreet profile|Monster profile|Naukri Profile" + "|click here to view resume in doc format|click here to unsubscribe" + "|Add Comments to Resume|BIO -  DATA|Consultants|Names will be provided on request|circulam vitae|urriculam vitae" + "|Qualification|Total Exp|Skill sets|CIRRUCULAM VITAE|C  U  R  R  I  C  U  L  U  M      V  I  T  A  E" + \
            "|circulam vitae|urriculam vitae|SAP-|Ref. By|CIRCULAM - VITAE|CIRCULAM-VITAE|job code" + "|i am writing|my objective is|i am confident|currently i am|i am enclosing|my norm is" + "|BIO - DATA|.Curriculum  Vitae|Carriculam Vitae|CIRRICULAM VITAE|CARRICULUM VITAE|urriculum Vitae|CRRICULUM VITAE|CUURICLUM VITAE|urriculum Vitae|- CIRCULLUM VITAE -|DCURRICULAM|CARICULAM VITAE" + "|RICULUM VITAE|CARRICULAM VITAE|Initial Contact - Curriculum Vitae|CIRCULUM VITAE|CIRRICULUM VITAE|comprehensive|URRICULUM  VITAE|CURRICULUM  VITAE|IRCULUM VITAE" + \
            "|CURICURUM VITAE|CIRICULAM-REVITA|RESUMẾ|Om Sai Ram|Contact Address :" + "|Age :|Contact No. :|Email Id :|Nationality/Sex :|Languages known :" + \
            "|CARRICULAM VITE|CERTIFIED|POST APPLIED|MICROSOFT CERTIFIED|rRESUME|CONCISE RESUME|View Resume|(Word 2000 Format)|View Text Resume Only|Forward This Resume|Contact by Email|Print Resume|Save to Folder|Close Window|Go to:"

        text = re.sub(exclude_re, " ", text)
        terms = text.splitlines()
        temp = ""

        count_split_words = 0

        for i in range(len(terms)):
            if re.search("\s[a-zA-Z]{1}\s", terms[i]):
                count_split_words += 1

                temp = re.sub(" +", "", terms[i])
                if len(temp) < 18:
                    temp_terms.append(temp)
                else:
                    temp_terms.append(terms[i])
            else:
                temp_terms.append(terms[i])

        terms = temp_terms

        temp_terms = []

        for i in range(len(terms)):
            temp_terms.append(re.sub('\s{2,}', ' ', terms[i]))

        terms = temp_terms

        for i in range(len(terms)):
            text = text + " " + terms[i]

        if 1:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future1 = executor.submit(email_id_extractor, terms, text)
                future2 = executor.submit(phone_extraction, terms, text)
                future3 = executor.submit(skills_extract, text)
                # future4 = executor.submit(extract_address,text)
                future5 = executor.submit(extract_experience, terms, text)
                future6 = executor.submit(extract_education, terms, text)
                future7 = executor.submit(industry_class, text)
                future8 = executor.submit(extract_dob, text)
                future9 = executor.submit(extract_gender, text)
                future10 = executor.submit(passport_no, text)
                email_id = future1.result()
                isd_code, phone_no = future2.result()
                skills_list = future3.result()
                # address,country_code= future4.result()
                exp_result, exp_dur = future5.result()
                edu_result = future6.result()
                industry = future7.result()
                dob = future8.result()
                gender = future9.result()
                passport = future10.result()

        person_name = name_extractor(
            text, terms, email_id, file_type, filename, phone_no)
        address, country_code = extract_address(text, phone_no)
        print(person_name)
        # if person_name == "" and re.search("pdf", file_name):
        #     s2 = textract.process(file_name, method='tesseract')
        #     text2 = str(s2, 'utf-8', 'ignore')
        #     text2 = re.sub(exclude_re, " ", text2)

        #     text2 = re.sub("\\xad|\\u200b|\\t", " ", text2)
        #     terms2 = text2.splitlines()
        #     person_name = name_extractor(
        #         text2, terms2, email_id, file_type, filename, phone_no)
        #     if phone_no == "":
        #         phone_no = phone_extraction(terms2, text2)
        #         email_id = email_id_extractor(terms2, text2)
        result = result_template
        result["personal_info"][0]["name"][0] = person_name
        result["personal_info"][0]["phone"][0] = phone_no
        result["personal_info"][0]["isd_code"][0] = isd_code
        result["personal_info"][0]["email"][0] = email_id
        result["personal_info"][0]["address"][0] = address
        result["personal_info"][0]["dob"] = dob
        result["personal_info"][0]["gender"] = gender
        result["personal_info"][0]["passport_no"] = passport
        result["education"] = edu_result
        result["experience"] = exp_result

        result["total_experience"] = exp_dur
        result["all_skills"][0] = skills_list

        result["text"][0] = text
        result["industry"] = industry

        return result

    except:
        return result_template
