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
exp_heading_2 = "Experience|ROFESSIONAL|Professional|Career|Employment|E xperience|P rofessional|C areer|E mployment|Work History|WORK HISTORY|WORK"
end_heading = "DUCATION|ERSONAL"
end_heading_2 = "DUCATION|ERSONAL|CADEMIC|Education|Acadmic|Personal"

job_titles = " marketing specialist | CEO | therapist | program manager | director | freelance | founder | tutor | coach | VP | senior | teamlead | team lead | assistant vice president | software architect | marketing manager | marketing director | graphic designer | hr |marketing research analyst | marketing communications manager | marketing consultant | product manager | public relations | social media assistant | brand manager | seo manager | content marketing manager | copywriter | media buyer | digital marketing manager | ecommerce marketing specialist | brand strategist | vice president of marketing | media relations coordinator | administrative assistant | receptionist | office manager | auditing clerk | bookkeeper | account executive | branch manager | business manager | quality control coordinator | administrative manager | chief executive officer | business analyst | risk manager | human resources | office assistant | secretary | office clerk | file clerk | account collector | administrative specialist | executive assistant | program administrator | program manager | administrative analyst | data entry | team leader | manager | talent acquisition | assistant manager | executive | director | coordinator | administrator | officer | organizer | supervisor | superintendent | head | overseer | chief | foreman | controller | principal | president | software developer | designer | developer | technician | web developer | software engineer | engineer | computer scientist | it professional | ux designer & ui developer | sql developer | web designer | web developer | help desk worker/desktop support | software engineer | data entry | devops engineer | programmer | computer programmer | network administrator | information security analyst | artificial intelligence engineer | cloud architect | it manager | technical specialist | application developer | sales associate | sales representative | sales manager | retail worker | store manager | sales representative | sales manager | real estate broker | sales associate | cashier | store manager | account executive | account manager | area sales manager | direct salesperson | director of inside sales | outside sales manager | sales analyst | market development manager | b2b sales specialist | sales engineer | marchandising associate | construction worker | taper | plumber | heavy equipment operator | vehicle or equipment cleaner | carpenter | electrician | painter | welder | handyman | boilermaker | crane operator | building inspector | pipefitter | sheet metal worker | iron worker | mason | roofer | solar photovoltaic installer | well driller | principal | owner | president | founder | administrator | director | partner | proprietor | human resource | accountant | supervisor | quality control | receptionist | virtual assistant | customer service | customer support | concierge | help desk | customer service manager | technical support specialist | account representative | client service specialist | customer care associate | operations manager | operations assistant | operations coordinator | operations analyst | operations director | operations professional | scrum master | continuous improvement lead | continuous improvement consultant |    •  credit authorizer | benefits manager | credit counselor | accountant | bookkeeper | accounting analyst | accounting director | accounts payable/receivable clerk | auditor | budget analyst | controller | financial analyst | finance manager | economist | payroll manager | payroll clerk | financial planner | financial services representative | finance director | commercial loan officer | engineer | mechanical engineer | civil engineer | electrical engineer | assistant engineer | chemical engineer | chief engineer | drafter | clerk | engineering technician | geological engineer | biological engineer | maintenance engineer | mining engineer | nuclear engineer | petroleum engineer | plant engineer | production engineer | quality engineer | safety engineer | sales engineer | researcher | research assistant | data analyst | business analyst | financial analyst | biostatistician | researcher | market researcher | medical researcher | tutor/online tutor | teacher | teaching assistant | substitute teacher | preschool teacher | test scorer | online esl instructor | professor | assistant professor | graphic designer | artist | interior designer | video editor | video or film producer | playwright | musician | novelist/writer | computer animator | photographer | camera operator | sound engineer | motion picture director | actor | music producer | director of photography | nurse | travel nurse | nurse practitioner | doctor | caregiver | cna | physical therapist | pharmacist | pharmacy assistant | medical administrator | medical laboratory tech | physical therapy assistant | massage therapy | dental hygienist | orderly | personal trainer | massage therapy | medical laboratory tech | phlebotomist | medical transcriptionist | telework nurse/doctor | reiki practitioner | housekeeper | flight attendant | travel agent | hotel front door greeter | bellhop | cruise director | entertainment specialist | hotel manager | front desk associate | front desk manager | concierge | group sales | event planner | porter | spa manager | wedding coordinator | cruise ship attendant | casino host | hotel receptionist | reservationist | events manager | meeting planner | lodging manager | director of maintenance | valet | waiter/waitress | chef | fast food worker | barista | line cook | cafeteria worker | restaurant manager | wait staff manager | bus person | restaurant chain executive | political scientist | chemist | conservation scientist | sociologist | biologist | geologist | physicist | astronomer | atmospheric scientist | molecular scientist | scientist | call center representative | customer service | telemarketer | telephone operator | phone survey conductor | dispatcher for trucks or taxis | customer support representative | over the phone interpreter | phone sales specialist | mortgage loan processor | counselor | mental health counselor | addiction counselor | school counselor | speech pathologist | guidance counselor | social worker | therapist | life coach | couples counselor | beautician | hair stylist | nail technician | cosmetologist | salon manager | makeup artist | esthetician | skin care specialist | manicurist | barber | journalist | copy editor | editor/proofreader | content creator | speechwriter | communications director | screenwriter | technical writer | columnist | public relations specialist | proposal writer | content strategist | grant writer | video game writer | translator | film critic | copywriter | travel writer | social media specialist | ghostwriter | warehouse worker | painter | truck driver | heavy equipment operator | welding | physical therapy assistant | housekeeper | landscaping worker | landscaping assistant | mover | animal breeder | veterinary assistant | farm worker | animal shelter worker | dog walker / pet sitter | zoologist | animal trainer | service dog trainer | animal shelter manager | animal control officer | delivery driver | school bus driver | truck driver | tow truck operator | ups driver | mail carrier | driver | recyclables collector | courier | bus driver | cab driver | animal shelter board member | office volunteer | animal shelter volunteer | hospital volunteer | youth volunteer | food kitchen worker | homeless shelter worker | conservation volunteer | meals on wheels driver | habitat for humanity builder | emergency relief worker | red cross volunteer | community food project worker | women’s shelter jobs | suicide hotline volunteer | school volunteer | community volunteer jobs | sports volunteer | church volunteer | volunteer | recruiter | paralegal | attorney | translator | architect | locksmith | operator | teller | tehnician | specialist | manager | director | designer | analyst | consultant | assistant | copywriter | buyer | strategist | coordinator | president | vice president | analyst | receptionist | clerk | bookkeeper | executive | coordinator | manager | officer | secretary | clerk | analyst | collector | administrator | data entry | chief | team leader | representative | attendant"


us_states_short_text = "AK|AL|AR|AZ|CA|CO|CT|DC|DE|FL|GA|GU|HI|IA|ID|IL|IN|KS|KY|LA|MA|MD|ME|MI|MN|MO|MS|MT|NC|ND|NE|NH|NJ|NM|NV|NY|OH|OK|OR|PA|PR|RI|SC|SD|TN|TX|UT|VA|VI|VT|WA|WI|WV|WY"

us_states_full_text ="Alaska|Alabama|Arkansas|Arizona|California|Colorado|Connecticut|Washington DC|Delaware|Florida|Georgia|Guam|Hawaii|Iowa|Idaho|Illinois|Indiana|Kansas|Kentucky|Louisiana|Massachusetts|Maryland|Maine|Michigan|Minnesota|Missouri|Mississippi|Montana|North Carolina|North Dakota|Nebraska|New Hampshire|New Jersey|New Mexico|Nevada|New York|Ohio|Oklahoma|Oregon|Pennsylvania|Puerto Rico|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Virginia|Virgin Islands|Vermont|Washington|Wisconsin|West Virginia|Wyoming|ALASKA|ALABAMA|ARKANSAS|ARIZONA|CALIFORNIA|COLORADO|CONNECTICUT|WASHINGTON DC|DELAWARE|FLORIDA|GEORGIA|GUAM|HAWAII|IOWA|IDAHO|ILLINOIS|INDIANA|KANSAS|KENTUCKY|LOUISIANA|MASSACHUSETTS|MARYLAND|MAINE|MICHIGAN|MINNESOTA|MISSOURI|MISSISSIPPI|MONTANA|NORTH CAROLINA|NORTH DAKOTA|NEBRASKA|NEW HAMPSHIRE|NEW JERSEY|NEW MEXICO|NEVADA|NEW YORK|OHIO|OKLAHOMA|OREGON|PENNSYLVANIA|PUERTO RICO|RHODE ISLAND|SOUTH CAROLINA|SOUTH DAKOTA|TENNESSEE|TEXAS|UTAH|VIRGINIA|VIRGIN ISLANDS|VERMONT|WASHINGTON|WISCONSIN|WEST VIRGINIA|WYOMING"

company_names ="ypf|american express|learningmate|central puerto|grupo galicia|mastercard|commonwealth|westpac ing|anz|national australia|bhp billiton|telstra|macquarie|wesfarmers|suncorp|qbe insurance|fortescue metals|woolworths|scentre|csl|woodside petroleum|amp|westfield|south32|origin|qantas|agl|vicinity centres|amcor|caltex australia|stockland australia|brambles|transurban|newcrest mining|ramsay health care|goodman|bendigo & adelaide|gpt|map|crown resorts|mirvac| of queensland|bluescope steel|erste |omv|raiffeisen  international|vienna insurance|voestalpine|uniqa|strabag|verbund|ahli united|arab ing|anheuser-busch inbev|kbc|solvay|ageas|ucb|dexia|proximus|colruyt|umicore|xl|athene holding|everest re|arch capital|banco btg pactual participations|assured guaranty|axis capital holdings|signet jewelers|renaissancere holdings|itaú unibanco holding|banco bradesco|banco do brasil|vale|petrobras|eletrobrás|itaúsa|jbs|ultrapar participacoes|cielo|braskem|brf|sabesp|oi|metalurgica gerdau|companhia brasileira de distribuicao|ccr|bm&f bovespa|cpfl energia|kroton educacional|royal  of canada|td | of nova scotia| of montreal|manulife|canadian imperial|brookfield asset management|enbridge|sun life financial|bce|power corp of canada|canadian national railway|magna international|suncor|couche tard|national  of canada|telus|rogers communications|barrick gold|george weston|transcanada|husky|teck resources|agrium|canadian natural resources|canadian pacific railway|fortis|fairfax|onex|cgi|restaurant brands international|hydro one|saputo|cenovus|canadian tire|intact financial|industrial alliance insurance|air canada|valeant pharmaceuticals|bombardier|potashcorp|open text|metro|goldcorp|pacific exploration & production|canadian utilities|pembina pipeline|empire|shaw communications|encana|waste connections|riocan real estate investment trust|emera|paramount res|first quantum minerals|laurentian|hudson's bay|dollarama|falabella|cencosud|antarchile|bci-banco credito|latam airlines|quinenco|banco de chile"
company_end_titles ="Corporation|CORP|Press|PRESS|Inc|INC|Pharmaceuticals|PHARMACEUTICAL|College|LABS|Technology Solutions|Technologies|TECHNOLOGIES|Labs|COMPANY|Company|ORGANISATION|Organisation|HOLDING|Holding|COLLEGE|Learning|LEARNING|Publicity|PUBLICITY|Hospitality|HOSPITALITY|UNIVERISTY|University|International|INSTITUTION|Institution|SCHOOL|Society|SOCIETY|School|ENERGY|Energy|PRIVATE LIMITED|Private Limited|Educational|EDUCATIONAL|Institute|Firm|Studios|University|Strategist|Partners|Strategies|Investments|Systems|Limited|LIMITED|LLC|Health Care|HEALTH CARE|llc|L\.L\.C|limited|LTD|Ltd|LTd|Ltd|Ldt|LDT|ltd|Group|GROUP|Bank|BANK|INVESTMENTS|Solutions|SOLUTIONS|TECHNOLOGY|Financial Services|Financial|FINANCIAL|Scientific|Technology Solution|RESORT|Resort|Spa|SPA|Technologies|Consulting|GLOBAL SERVICES|Agency|Corp|Scientific|AIRWAYS|Airways"
not_exp_word = "user|bjective|summary|verview|ynopsis|volunteer"

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
            if re.search(exp_heading_2,terms[i]) and  len(terms[i].split())<4 and  not re.search(not_exp_word,terms[i].lower()):
                temp_terms = terms[i:]
                break
        terms = temp_terms

        for i in range(len(terms)):
            if re.search(end_heading_2,terms[i]) and  len(terms[i].split())<6:
                temp_terms =terms[:i]
                break

        terms = temp_terms


    return terms 



def extract_experience(terms,text):
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
        terms = experience_text(terms)
        for i in range(len(terms)):
            exp_text =exp_text +" "+terms[i]

        total_dur = duration_experience(terms,text)
        present_employer = extract_present_employer(exp_text,terms)
        present_designation = extract_present_designation(exp_text,terms)
        workex_skill = skills_extract(exp_text)

        exp_result["exp_text"] = exp_text
        exp_result["exp_history"][0]["id"]=str(0)
        exp_result["exp_history"][0]["organization"] = present_employer
        exp_result["exp_history"][0]["job_designation"]= present_designation
        exp_result["workex_skills"] = workex_skill


        return exp_result,total_dur


    except:
        return temp_result,"0"

def duration_experience(terms,text):
    try:
        total_dur = ""
        text_piece = re.sub('[^A-Za-z0-9. ]+', ' ', text)
        text_piece = re.sub("\. | \.",".",text_piece)
        text_piece= text_piece.lower()
        res = text_piece.split()
        list_dur = []
        temp_dur = 0
        last = ""
        for i in range(len(res)):
            try :
                if re.search("year|years",res[i]) :
                    if  "experience" in res[i+1].lower() or "experience" in res[i+2].lower() or "experience" in res[i+3].lower() or  "experience" in res[i+4].lower() or "experience" in res[i+5].lower() or "experience" in res[i-1].lower() or "experience" in res[i-2].lower() or "experience" in res[i-3].lower() :
                        if re.search("\d",res[i-1]):
                            total_dur = res[i-1] + "+"
                            break
                        elif re.search("\d",res[i-2]):
                            total_dur = res[i-2] + "+"
                            break
                        elif re.search("\d",res[i-3]):
                            total_dur = res[i-3]  + "+"
                            break
            except:
                break
        if total_dur == "":
            year_range = "1985|1986|1987|1989|1990|1991|1992|1993|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021"
            two_digit_year_range = "85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20"
            min_year = 2100
            res = []
            total_dur =0
            
            for i in range(len(terms)):
                temp = terms[i].split()
                res = res + temp

            for i in range(len(res)):
                if re.search(year_range,res[i]):
                    
                    if int(re.search(year_range,res[i])[0]) <min_year:
                        min_year = int(re.search(year_range,res[i])[0])

            if min_year<2022:
                total_dur =2020-min_year
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


                if min_year<2021:
                    total_dur =2020-min_year
                else :
                    total_dur =0


        return str(total_dur)
    except:
        return "0"


def extract_present_employer(exp_text,terms):
    try:
        match = ""
        end_index = -1
        present_employer = ""
        terms = terms[:min(len(terms),10)]
        print(terms)
        temp_terms = []
        temp_text = ""
        for i in range(len(terms)):
            res= terms.split()
            temp_text =""
            for j in range(len(res)):
                if re.search("[A-Z]",res[i][0]):
                    temp_text = temp_text + " " + res[j]
            temp_terms.append(temp_text)


        for i in range(len(terms)): 
            if re.search("employer|organisation",terms[i].lower()):
                present_employer = terms[i]
                break
        
        if present_employer =="":
            for i in range(len(terms)):
                if re.search(company_names,terms[i].lower()) and re.search("[A-Z]",terms[i]) and len(terms[i].split())<6:
                    if len(re.search(company_names,terms[i].lower())[0])>4:
                        present_employer = re.search(company_names,terms[i].lower())[0]
                        break
        if present_employer =="":
            for i in range(len(terms)):
                temp = terms[i] + " "
                if re.search(us_states_short_text,temp) and len(terms[i].split())<10 :
                    present_employer = temp

                    present_employer = re.sub("[^a-zA-Z\s]+"," ",present_employer)
                    if len(present_employer.split())<3 :
                        present_employer = ""
                    break
                if present_employer=="" and  re.search(us_states_full_text,temp) and len(terms[i].split())<6:
                    present_employer = temp
                
                    present_employer = re.sub("[^a-zA-Z\s]+"," ",present_employer)
                    if len(present_employer.split())<3:
                        present_employer = ""
                    break

        if present_employer =="":
            for i in range(len(terms)):
                if re.search("at",terms[i].lower()):
                    ind = terms[i].lower().index("at")
                    temp = terms[i][ind:]
                    present_employer = temp

            for i in range(len(terms)):
                if re.search(company_end_titles,terms[i]) and len(terms[i].split())<6:
                    match =  re.search(company_end_titles,terms[i])[0]
                    present_employer=terms[i]
                    break
            if present_employer != "":
                res =present_employer.split()
                present_employer = ""
                for i in range(len(res)):
                    if match in res[i]:
                        k = i 
                        while(res[k][0].isupper()) and k >=0:
                            present_employer = res[k]  +" "+present_employer 
                            k =k-1

            res = exp_text.split()
            exp_text =""
            for i in range(len(res)):
                if re.search("[A-Z]",res[i][0]):
                    exp_text += res[i]
            if present_employer == "":
                for i in range(len(res)):
                    # words before the month or year
                    if re.search(month_range,exp_text.lower()):
                        temp_end_index = i
                        if temp_end_index<end_index or end_index == -1:
                            end_index = i

                    if re.search(digit_year_range,exp_text.lower()) or end_index == -1:
                        temp_end_index = i
                        if temp_end_index<end_index:
                            end_index = temp_end_index
                    
                    if re.search(month_range,exp_text.lower()) or end_index == -1:
                        temp_end_index = i
                        if temp_end_index<end_index:
                            end_index = temp_end_index
                
                if res[i-1][0].isupper():
                    present_employer = res[i-1]
                if res[i-2][0].isupper():
                    present_employer = res[i-2]+ " " +present_employer
                if res[i-3][0].isupper():
                    present_employer = res[i-3]+ " " +present_employer
                
                # words before location


        if present_employer != "":
            present_employer = re.sub("[0-9]"," ",present_employer)

        return present_employer
    except:
        return ""


def extract_present_designation(exp_text,terms):
    try:
        present_designation = ""
        
        for i in range(len(terms)):
            temp = " " +terms[i] + " " 
            if re.search(job_titles,temp.lower()) and  len(terms[i].split())<9:
                present_designation = temp
                break 


        if present_designation == "":
            exp_text = re.sub(":|,|\."," ",exp_text)

            if re.search(job_titles,exp_text.lower()):
                present_designation = re.search(job_titles,exp_text.lower())[0]
                present_designation.capitalize()
                for i in range(len(terms)):
                    if re.search(present_designation.lower(),terms[i].lower()) and  len(terms[i].split())<9:
                        present_designation = terms[i]
                        break
        if re.search(present_designation.lower(),job_titles):
            job_titles_match = re.search(present_designation.lower(),job_titles)[0]
            jt_index = present_designation.lower().index(job_titles_match)
            present_designation= present_designation[:jt_index]
        
        present_designation = re.sub(us_states_full_text,"",present_designation)
        present_designation = re.sub("[0-9]","",present_designation)
        present_designation = re.sub(us_states_short_text,"",present_designation)


        return present_designation
    except:
        return ""
