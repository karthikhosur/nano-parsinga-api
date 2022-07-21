import re
import concurrent.futures


edu_headings = "DUCATION|CADEMIC|EGREE"
end_headings = "XPERIENCE|MPLOYMENT|AREER|ERSONAL"
edu_headings_2 ="Education|Academic|Degrees"
end_headings_2 = "Personal|Experience"

temp_edu_result = {"edu_text":"",
    "edu_history":
    [{"id": "",
    "degree": "",
    "university": "",
    "grade": "",
    "graduation_year": ""}]}

degree_list = ["Phd|P\.H\.D|Phd\.",
"Masters of Science|Master of Science|M\.Sc\.|MSc|MS|Master of Sciences|Master In Science|M\. Sc\.|M\.Sc\.|MSc|M\. Sc\.",
"Master in Commerce|M\.Com|MCom|M\.Com\.|MCom\.|MCOM|Mcom|M\.COM",
"Master in Education|M\.Ed\.|M\. Ed|Master in Edn\.|M\.ED",
"M\.Tech|m\.tech|Master of Technology|M\.Tech\.|M\.tech\.|M Tech|M tech",
"M\.Ped\.|M\.PED\.|MPED\.|MPED|Mped|Mped\.",
"M\.PHIL|MASTER OF PHILOSOPHY|M\.Phil\.|m\.phil\.|Master Of Philosophy|MPHIL|M\.PHIL\.|M\.Phil",
"Master of Fisheries Science|M\.S\.F\.|MSF|M\.S\.F"
,"M\.S\.W\.|m\.s\.w\.|Master Of Social Works|Masters of Social Works",
"Master in Pharmaceutical|M\.Pharm|MPharm|Master of Pharmaceutical",
"MD/MS",
"Master in Arts|M\.A|M A|Master of Arts|M\.A\.",
"MBA|M\.B\.A|M\.B\.A\.|Master in Business Administration|MSM|Masters of Business Administration",
"Master in Information Technology|Masters of Information Technology|Master in Information Tech\.",
"MSIT|MS\(IT\)|M\.S\.I\.T\.|Master of Information Technology|MS IT|M\.S\. IT",
"MCA|M\.C\.A|M\.C\.A\.|Masters Computer Application|Master of Computer Application|Masters in Computer Application|Master in Computer Applications|Masters of Computer Applications",
"M\.E\.|M\.E|Master of Engineering|Master of Engg\.|Master of Engg|Master in Engineering",
"B\.TECH|B\.Tech|Bachelor In Technology|B\.E\.|Bachelor of Engineering|Bachelors of Science|B\.TECH\(CSE\)|Bachelor of Engineering|B\.E\.|B\.E|BACHELOR OF ENGINEERING|BACHELOR DEGREE IN ENGINEERING|BACHELOR'S DEGREE IN ENGINEERING|bachelor of engineering|Bachelor Of Engineering|Bachelor's Degree in Engineering|BACHELOR'S DEGREE IN ENGINEERINGBACHELOR OF ENGINEERING|BACHELOR DEGREE IN ENGINEERING|BACHELOR'S DEGREE IN ENGINEERING|bachelor of engineering|Bachelor Of Engineering|Bachelor's Degree in Engineering|BACHELOR'S DEGREE IN ENGINEERING|BE",
"Bachelor of Arts|B\.A|B\.A\.|Bachelor Degree in Arts|Bachelor Degree in English|Bachelor Degree in Economics|Bachelor Degree in History|B\.A \(Hons\.\)|BA",
"Bachelor of Science|B S|B\.S\.|Bachelor Degree in Computer Science|Bachelors of Computer Science|Bachelor of Science|B\.Sc|B\.Sc\.|Bachelors of Sciences|BACHELOR OF SCIENCE|BACHELOR'S OF SCIENCE|BACHELOR DEGREE IN SCIENCE|B\.SC\.|BSC|BE|B\.sc|B\.Sc|B\.Sc\.|Bachelors of Sciences|BACHELOR OF SCIENCE|BACHELOR'S OF SCIENCE|BACHELOR DEGREE IN SCIENCE|B\.SC\.|BSC",
"BCA|Bachelor of Computer Application|BCA|Bachelor of Computer Application|B\.C\.A\.|Bachelor Of Computer Application|Bachelors of Computer Applications|BACHELOR OF COMPUTER APPLICATION|BACHELORS OF COMPUTER APPLICATIONS|bca|b\.c\.a\.|Bachelor Degree in Computer Applications|Bachelor Degree in Computer Application|B\.C\.A\.|Bachelors of Computer Science|Bachelor Of Computer Application|Bachelors of Computer Applications|BACHELOR OF COMPUTER APPLICATION|BACHELORS OF COMPUTER APPLICATIONS|bca|b\.c\.a\.|Bachelor Degree in Computer Applications|Bachelor Degree in Computer Application|Bachelor's Degree",
"BBA|BBA|Business Administration|Bachelor of Business Administration|B\.B\.A\.|B\.B\.A|BACHELOR OF BUSINESS ADMINISTRATION|Bachelor Of Business Administration|Bachelor Degree in Business Administration|Bachelor of Arts|B\.A|B\.A\.|Bachelor Degree in Arts|Bachelor Degree in English|Bachelor of Business Administration|B\.B\.A\.|B\.B\.A|BACHELOR OF BUSINESS ADMINISTRATION|Bachelor Of Business Administration|Bachelor Degree in Business Administration",
"B\. Com|Bcom|B\.COM|B\. COM|B\.Com|Bachelor of Commerce|Bachelor of Commerce|Bachelor Degree in Commerce|Bachelor's Degree in Commerce|b\.com\.|B\.COM\.|BACHELOR OF COMMERCE|BCOM|BACHELOR DEGREE IN COMMERCE|BACHELOR'S DEGREE IN COMMERCE",
"Bachelor of Education|BEd|B\.Ed|BACHELOR OF EDUCATION|BACHELOR'S DEGREE IN EDUCATION|B\.ED\.|Bachelor's Degree in Education|bachelor of education|Bachelor Of Education",
"Bachelor of Dental science|BDS|B\.D\.S\.|B\.D\.S|BACHELOR OF DENTAL SCIENCE",
"Bachelor of Paramaceutical|B\.Pharm|B\.PHARM|B\.PHARM\.",
"Law|L\.L\.B\.",
"C\.A|C\.A\.|Chartered Accountant",
"Company Secretary|C\.S ",
"Master of Law|L\.L\.M\.",
"B\.Tech|BTech|B\-Tech\.|Bachelor of Technology",
"Bachelor Of Law|B\.L\.|Bachelor of Law|BACHELOR OF LAW|BACHELOR DEGREE IN LAW|BACHELOR'S DEGREE IN LAW|Bachelor Degree in Law|Bachelor's Degree in Law|L\.L\.B\.",
"icwa",
"pgdm",
"M\.B\.B\.S|MBBS|MBBS\.",
"Post Graduate Diploma in Business Management",
"B\.Ped\.|B\.PED\.|Bachelor Of Physical Education|BACHELOR OF PHYSICAL EDUCATION",
"Bachelors of Information Technology|Bachelor of Information Technology",
"Diploma"]
degree_map = ["Ph.D","M.Sc","M.Com","M.Ed","M.Tech","M.PED","M.Phil","MSF","MSW","M.Pharm","MD/MS","M.A","M.B.A","M.I.T","MSIT","M.C.A","M.E","B.E","B.A","B.Sc","B.C.A","B.B.A","B.Com","B.Ed","B.D.S","B.Pharm","L.L.B","C.A","C.S","L.L.M","B.Tech","B.L","ICWA","PGDM","MBBS","PGDCA","B.PED","B.IT","Diploma"]
# degree_map_match = [["doctor","philosophy","phd"],["master","science","msc"],["master","commerce","mcom"],["master","education","med"],["master","tech","mtech"],["master","pedeatrics","mped"],["master","philosophy","mphil"],["master","finance","msf"],["master","socialwork","msw"],["master","pharma","mpharm",],["md/ms"],["master","art","ma"],["master","businessadministration","mba"],["master","informationtechnology","msit"],["master","science","information","technology","computer","mscs","mcs"],["master","computerapplication","mca"],["master","engineering","me"],["bachelor","engineering","be"],["bachelor","arts","ba"],["bachelor","science","bsc"],["bachelor","computerapplication","bca"],["bacehlor","businessadmin","bba",],["bachelor","commerce","bcom"],["bachelor","education","bed"],["bachelor","dental","bds"],["bachelor","pharma","bpharm"],["bachelor","law","llb"],["chartered","accountant"],[],["master","law"],["bachelor","technology","btech"],[],["icwa"],["postgraduate","diploma","pgdm"],["bachelor","medical","mbbs"],[],[],[],["diploma"]]



only_college_degree ="Bachelor of Engineering|Bachelor|Engineering|Commerce|Bachelors of Science|B.TECH(CSE)|B.COM|B. COM|B.Com|B.TECH|B.Tech|B.E.|MCA|B.E| BTECH |BACHELOR OF ENGINEERING|BACHELOR DEGREE IN ENGINEERING|BACHELOR'S DEGREE IN ENGINEERING|bachelor of engineering|Bachelor Of Engineering|Bachelor's Degree in Engineering|BACHELOR'S DEGREE IN ENGINEERING|BE|B.sc|Bachelor In Technology|Bachelor of Arts|B.A|B.A.|Bachelor Degree in Arts|Bachelor Degree in English|Bachelor Degree in Economics|Bachelor Degree in History|B.A (Hons.)|Bachelor Degree in Computer Science|Bachelors of Computer Science|Bachelor of Science|B.Sc|B.Sc.|Bachelors of Sciences|BACHELOR OF SCIENCE|BACHELOR'S OF SCIENCE|BACHELOR DEGREE IN SCIENCE|B.SC.|BSC|Master of Science|M.Sc.|MSc|Master of Sciences|Master Of Science|M. Sc.|BCA|Bachelor of Computer Application|B.C.A.|Bachelor Of Computer Application|Bachelors of Computer Applications|BACHELOR OF COMPUTER APPLICATION|BACHELORS OF COMPUTER APPLICATIONS|bca|b.c.a.|Bachelor Degree in Computer Applications|Bachelor Degree in Computer Application|Bachelor's Degree|BBA|Bachelor of Business Administration|B.B.A.|B.B.A|BACHELOR OF BUSINESS ADMINISTRATION|Bachelor Of Business Administration|Bachelor Degree in Business Administration|B. Com|Bcom|Bachelor of Commerce|Bachelor of Commerce|Bachelor Degree in Commerce|Bachelor's Degree in Commerce|b.com.|B.COM.|BACHELOR OF COMMERCE|BCOM|BACHELOR DEGREE IN COMMERCE|BACHELOR'S DEGREE IN COMMERCE|Bachelor of Education|BEd|B.Ed|BACHELOR OF EDUCATION|BACHELOR'S DEGREE IN EDUCATION|B.ED.|Bachelor's Degree in Education|bachelor of education|Bachelor Of Education|Bachelor of Dental science|BDS|B.D.S.|B.D.S|BACHELOR OF DENTAL SCIENCE|Bachelor of Paramaceutical|B.Pharm|B.PHARM|B.PHARM.|L.L.B.|C.A|C.A.|Chartered Accountant|Company Secretary|C.S|Master of Law|L.L.M.|Master in Commerce|M.Com|MCom|M.Com.|MCom.|Master in Education|M.Ed.|M. Ed|Master in Edn.|Master in Pharmaceutical|M.Pharm|MPharm|Master of Pharmaceutical|Master in Arts|M.A|M A|Master of Arts|M.A.|MBA|M.B.A|M.B.A.|Master in Business Administration|Master of Business Administration|Master in Information Technology|Masters of Information Technology|Master in Information Tech.|MCA|M.C.A|M.C.A.|Master of Computer Application|Masters in Computer Application|Master in Computer Applications|Masters of Computer Applications|M.E.|M.E|Master of Engineering|Master of Engg.|Master of Engg|Master in Engineering|Graduation BE|Bachelors of Technology|B.Tech|BTech|BTech.|Bachelor of Technology|M.Tech|m.tech|Master of Technology|M.Tech.|M.tech.|M Tech|M tech|MSIT|MS(IT)|M.S.I.T.|Master of Information Technology|MS IT|M.S. IT|Phd|P.H.D|Phd.|Bachelor Of Law|B.L.|Bachelor of Law|BACHELOR OF LAW|BACHELOR DEGREE IN LAW|BACHELOR'S DEGREE IN LAW|Bachelor Degree in Law|Bachelor's Degree in Law|MSc IT|MSc (IT)|Master of Information Technology|MSC(IT)|MScIT|Master in Information Technology|Master of IT.|Master of IT|Advance Diploma In Tourism & Travel Industry Management|Diploma Course In Labour Laws And Labour Welfare|Diploma in Advertising and Public Relations|Diploma In Analytical Instrumentation|Diploma in Business Management|Diploma In Communication|Diploma in Computer Application Technology|Diploma In Computer Management|Diploma In Computer Programming|Diploma in Computer Science|Diploma In Computerised Data Processing And Management Information System|Diploma in Electronics|Diploma in Engineering|Diploma In Financial Management|Diploma In French|Diploma In German|Diploma in Human Resource Management|Diploma in Information Technology|Diploma In Managment Studies (D.M.S)|Diploma In Marketing Management|Diploma in Mechanical|Diploma in Mechatronics|Diploma in Pharmacy|Diploma In System Management|Diploma In Tourism And Travel Industry Management. (Dip. In T.T.M.)|icwa|pgdm|M.B.B.S|MBBS|MBBS.|Post Graduate Diploma in Business Management|MD/MS|B.Ped.|B.PED.|Bachelor Of Physical Education|BACHELOR OF PHYSICAL EDUCATION|M.Ped.|M.PED.|MPED.|MPED|Mped|Mped.|M.PHIL|MASTER OF PHILOSOPHY|M.Phil.|m.phil.|Master Of Philosophy|MPHIL|M.PHIL.|M.Phil|Master of Fisheries Science|M.S.F.|MSF|M.S.F|M.S.W.|m.s.w.|Master Of Social Works|Masters of Social Works|Bachelors of Information Technology|Bachelor of Information Technology|Post Graduation Diploma in Banking|P.G.D.B|Bachelor of Engineering|Bachelor of Arts|Bachelor of Science|Master of Science|Bachelor of Computer Application|Bachelor of Business Application|Bachelor of Commerce|Bachelor of Education|Bachelor of Dental science|Bachelor of Paramacetuical|Law|Chartered Accountant|Company Secretary|Master of Law|Master in Commerce|Master in Education|Master in Pharmaceutical|Master in Arts|Master in Business Administration|Master in Information technology|MCA|M.E|M.Tech|Information Technology|Bachelor of Technology|B.E|B.A|B.Sc|M.Sc|B.C.A|B.B.A|B.Com|B.Ed|B.D.S|B.Pharm|L.L.B|C.A|C.S|L.L.M|M.Com|M.Ed|M.Pharm|M.A|M.B.A|M.I.T|M.C.A|M.E|M.Tech|MSIT|Ph.D|B.L|M.Sc IT|Diploma|ICWA|PGDM|MBBS|PGDCA|MD/MS|B.PED|M.PED|M.Phil|MSF|MSW|B.IT|SSLC|H.Sc|High School or Equivalent|Bachelor's Degree|Higher Degree|Master's Degree|Doctorate|P.G.D.B|B. Tech|B. Engg.|B. Engineering|B. Sc Agriculture|B. Sc BioTechnology|B. Sc Chemistry|B. Sc Computers|B. Sc Dairy Technology|B. Sc Food Technology|B. Sc Physics|B. Sc Statistics|B. Tech Aviation|B. Tech Chemical|B. Tech Civil|B. Tech Computers|B. Tech Electrical|B. Tech Electronics|B. Tech Instrumentation|B. Tech Mechanical|B. Tech Mining|B. Tech Environment|B. Tech Production|B. Tech Agriculture|B. Tech Architecture|B. Tech Automobile|B. Tech BioChemistry|B. Tech BioTechnology|B. Tech Dairy Technology|B. Tech Food Technology|B. Tech Industrial Engineering|B. Tech IT|B. Tech Fire|B. Tech Metallurgy|B. Tech Systems|B. Tech Telecommunications|B. Tech Textile|B.Com Commerce|B.Pharm Pharmacy|Bachelor in Arts Economics|Bachelor in Arts Journalism|Bachelor in Arts Literature|Bachelor in Arts Arts|Bachelor in Arts Psychology|BCA Computers|BDS Medicine|BE Aviation|BE Chemical|BE Civil|BE Computers|BE Electrical|BE Electronics|BE Instrumentation|BE Mechanical|BE Mining|BE Environment|BE Production|BE Agriculture|BE Architecture|BE Automobile|BE BioTechnology|BE Dairy Technology|BE Fire|BE Food Technology|BE Industrial Engineering|BE IT|BE Marine|BE Metallurgy|BE Textile|BSL Labour Law|CS Company Secretary|Diploma Computers|Diploma Fashion Design|Diploma Hotel Management|Diploma Management|Diploma Electronics|Diploma Automobile|Diploma Chemical|Diploma Civil|Diploma Electrical|Diploma Food Technology|Diploma IT|Diploma Instrumentation|Diploma Labour Law|Diploma Marketing|Diploma Mechanical|Diploma Production|Diploma Software|Diploma Architecture|Diploma Environment|Diploma Fire|Diploma Metallurgy|Diploma Pharmacy|Diploma Telecommunications|Diploma Training|Diploma Textile|ICWA Accounts|LLM Labour Law|M.com Commerce|M.IT IT|M.Pharm Pharmacy|M.Sc Agriculture|M.Sc BioTechnology|M.Sc Chemistry|M.Sc Computers|M.Sc Dairy Technology|M.Sc Food Technology|M.Sc Physics|M.Sc Statistics|M.Sc.Tech IT|M.Sc.Tech Textile|M.Tech Aviation|M.Tech Chemical|M.Tech Civil|M.Tech Computers|M.Tech Electrical|M.Tech Electronics|M.Tech Instrumentation|M.Tech Mechanical|M.Tech Mining|M.Tech Environment|M.Tech Production|M.Tech Textile|MA Economics|MA Journalism|MA Literature|MA Arts|MA Psychology|MBA Fire|MBA Finance|MBA Marketing|MBA Mass Communication|MBA IR|MBA Systems|MBA Manufacturing|MBBS Medicine|MCA Computers|MD/MS Medicine|ME Aviation|ME Chemical|ME Civil|ME Computers|ME Electrical|ME Electronics|ME Instrumentation|ME Mechanical|ME Mining|ME Environment|ME Production|ME Textile|MS IT IT|PGDCA Computers|PGDM Fire|PGDM Finance|PGDM IR|PGDM Marketing|PGDM Mass Communication|PGDM Systems|Ph.D Agriculture|Ph.D Mass Communication|Ph.D Fire|Ph.D Architecture|Ph.D Aviation|Ph.D BioTechnology|Ph.D Chemistry|Ph.D Civil|Ph.D Commerce|Ph.D Computers|Ph.D Dairy Technology|Ph.D Economics|Ph.D Electrical|Ph.D Electronics|Ph.D Fashion Design|Ph.D Finance|Ph.D Food Technology|Ph.D Hotel Management|Ph.D Journalism|Ph.D Labour Law|Ph.D Literature|Ph.D Mechanical|Ph.D Medicine|Ph.D Pharmacy|Ph.D Physics|Ph.D Psychology|Ph.D Software|Ph.D Statistics|Ph.D Telecommunications|B.E|B.A|B.Sc|M.Sc|B.C.A|B.B.A|B.Com|B.Ed|B.D.S|B.Pharm|L.L.B|C.A|C.S|L.L.M|M.Com|M.Ed|M.Pharm|M.A|M.B.A|M.I.T|M.C.A|M.E|M.Tech|MSIT|Ph.D|B.L|M.Sc IT|Diploma|ICWA|PGDM|MBBS|PGDCA|MD/MS|B.PED|M.PED|M.Phil|B.IT| BA| B.A"






current = "present|current|till|onwards"
year_range = "1985|1986|1987|1989|1990|1991|1992|1993|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021"

def education_txt(terms):
    
    #Check for Capital Titles
    chk = 0
    temp_terms = []
    for i in range(len(terms)):
        
        if re.search(edu_headings,terms[i]) :
            temp_terms = terms[i:]
            chk =1
            break
    
    if not len(temp_terms) == 0:
        terms = temp_terms

        for i in range(len(terms)):
            if re.search(end_headings,terms[i]) and  len(terms[i].split())<6:
                temp_terms =terms[:i]

        terms = temp_terms
    
    if not chk ==1:
        # Check for small titles 

        temp_terms = []
        for i in range(len(terms)):
            if re.search(edu_headings_2,terms[i]) and  len(terms[i].split())<4:
                temp_terms = terms[i:]
                break
        terms = temp_terms

        for i in range(len(terms)):
            if re.search(end_headings_2,terms[i]) and  len(terms[i].split())<6:
                temp_terms =terms[:i]

        terms = temp_terms


    return terms 


def extract_education(terms,text):
    # try:
        edu_result = {"edu_text":"",
        "edu_terms":[],
        "edu_history":
        [{"id": "",
        "degree": "",
        "university": "",
        "grade": "",
        "graduation_year": ""}]}
        
        terms =education_txt(terms)
        edu_text =""
        for i in range(len(terms)):
            edu_text = edu_text+" "+terms[i]


        with concurrent.futures.ThreadPoolExecutor() as executor:
            future21 = executor.submit(extract_degree_title, terms,edu_text,text)
            future22 = executor.submit(extract_university,terms)
            future23 = executor.submit(extract_grad_year,terms)
            degree_title= future21.result()
            university = future22.result()
            graduation_year= future23.result()

        # degree_title = extract_degree_title(terms,edu_text,text)
        # university = extract_university(terms)
        # graduation_year = extract_grad_year(terms)


        edu_result["edu_text"] = edu_text
        edu_result["edu_terms"] = terms
        edu_result["edu_history"][0]["id"]="0"
        edu_result["edu_history"][0]["degree"]=degree_title
        edu_result["edu_history"][0]["university"]=university
        edu_result["edu_history"][0]["graduation_year"]=graduation_year
        
        return edu_result
    # except:
    #     return temp_edu_result


def extract_degree_title(terms,edu_text,text):
    try:
        degree_title = ""
        for i in range(len(terms)):
            for j in range(len(degree_list)):
                if re.search(degree_list[j],terms[i]) and degree_title=="":
                    print(re.search(degree_list[j],terms[i])[0])
                    degree_title = degree_map[j]
                    break

            if degree_title == "":
                    if re.search("master|MASTER|Master|M\.",terms[i]) and degree_title == "":
                        if re.search("science|m\.sc",terms[i].lower()):
                            degree_title = "M.Sc"
                        elif re.search("commerce|m\.com",terms[i].lower()):
                            degree_title = "M.Com"
                        elif re.search("education|m\.ed",terms[i].lower()):
                            degree_title = "M.Ed"
                        elif re.search("tech|m\.tech",terms[i].lower()):
                            degree_title = "M.Tech"
                        elif re.search("phil|m\.phil",terms[i].lower()):
                            degree_title = "M.Phil"
                        elif re.search("finance",terms[i].lower()):
                            degree_title = "MSF" 
                        elif re.search("pharm",terms[i].lower()):
                            degree_title = "M.Pharm" 
                        elif re.search("arts|m\.a",terms[i].lower()):
                            degree_title = "M.A" 
                        elif re.search("business|m\.b\.a",terms[i].lower()):
                            degree_title = "M.B.A" 
                        elif re.search("engineering|m\.e",terms[i].lower()):
                            degree_title = "M.E" 
                        elif re.search("application|m\.c\.a",terms[i].lower()):
                            degree_title = "M.C.A" 
                        elif re.search("information",terms[i].lower()):
                            degree_title = "MSIT"
                        elif re.search("law",terms[i].lower()):
                            degree_title = "L.L.M"
                        # else : 
                        #     degree_title = "Masters"

                    if re.search("bachelor|BACHELOR|Bachelor|B\.",terms[i]) and degree_title == "":
                        if re.search("engineering|b\.e",terms[i].lower()) or  re.search("E",terms[i]):
                            degree_title = "B.E"
                        if re.search("science|b\.sc",terms[i].lower()) or  re.search("S",terms[i]):
                            degree_title = "B.Sc"
                        if re.search("dental",terms[i].lower()) or  re.search("D",terms[i]):
                            degree_title = "B.D.S"
                        elif re.search("commerce|b\.com",terms[i].lower()) or  re.search("C",terms[i]):
                            degree_title = "B.Com"
                        if re.search("education|b\.ed",terms[i].lower()) or  re.search("Ed|ED",terms[i]):
                            degree_title = "B.Ed"
                        elif re.search("tech|b\.tech",terms[i].lower()):
                            degree_title = "B.Tech"
                        elif re.search("phil",terms[i].lower()):
                            degree_title = "B.Phil"
                        elif re.search("finance",terms[i].lower()):
                            degree_title = "BSF" 
                        elif re.search("pharm",terms[i].lower()):
                            degree_title = "B.Pharm"
                        elif re.search("arts",terms[i].lower()):
                            degree_title = "M.A" 
                        elif re.search("business",terms[i].lower()):
                            degree_title = "B.B.A" 
                        elif re.search("engineering",terms[i].lower()):
                            degree_title = "B.E" 
                        elif re.search("application",terms[i].lower()):
                            degree_title = "B.C.A" 
                        elif re.search("information",terms[i].lower()):
                            degree_title = "BSIT" 
                        elif re.search("law",terms[i].lower()):
                            degree_title = "L.L.B"
                        # else:
                        #     degree_title = "Bachelors"

        if degree_title == "" and re.search(only_college_degree,edu_text):
            degree_title = re.search(only_college_degree,edu_text)[0]
            
        return degree_title

    except:
        return ""


def extract_university(terms):
    try:
        university_name = ""
        for i in range(len(terms)):
            if re.search("university|institute|academy|college|polytechnic|school",terms[i].lower()):
                university_name= terms[i]
                university_name = re.sub("[^a-zA-Z\s]+"," ",university_name)
                res = university_name.split()
                university_name =""
                for j in range(len(res)):
                    if  res[j][0].isupper():
                        university_name += " " +res[j]
                break
        # university_name =re.sub(only_college_degree," ", university_name)
        return university_name
    except:
        return ""

def extract_grad_year(terms):
    try:
        grad_year = -1
        for i in range(len(terms)):
            if re.search(current,terms[i].lower()):
                grad_year= 2021
            elif re.search(year_range,terms[i]):
                if int(re.search(year_range,terms[i])[0])>grad_year:
                    grad_year= int(re.search(year_range,terms[i])[0])
        
        return str(grad_year)
    except:
        return ""

