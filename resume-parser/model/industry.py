import re

def industry_class(text):
    try:
        industry_count =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        industry_type = ["Computers and Information Technology", "Healthcare","Hospitality","Pharma, Biotecnology and Clinical Research","Logistics and Supply Chain","Education","Creative and Design","Manpower and Staffing","Construction","Marketing and Social Media","Clean Energy","Banking, Financial Services and Insurance(BFSI)","Real Estate","Fabrication and Engineering","Aerospace","Airlines","BPO/KPO/Call Center","Entertainment","Facility Management", "Food and Beverages","Leather","Legal Services","Manufacturing","Mining", "Music","News and Broadcasting","Oil and Gas","Professional Services","Taxation, Audit, Compliance","Telecommunication and Internet","Textile, Garments and Fashion","Wellness, Fitness, Sports and Beauty","Travel and Tourism","Electronics"]
        
        information_technology_re= "embedded|software|ajax|agile|android|c\#|c\+\+|css|haskell|software|html|java|javascript|julia|matlab|octave|perl|php|python|ruby|scala|sql|angular|asp.net|aws|cassandra|django|hadoop|hbase|hive|jquery|laravel|linux|mongodb|mysql|nltk|node|numpy|pandas|pig|postgresql|rails|react|spark|tensorflow|react"
        healthcare = "medic|clinic|prescription|health|nurs|patient"
        hospitality = "hospitality|guest|hotel|cafe|restaurant"
        pharmacy = "drug|pharma|biotech|bioscience"
        logistics = "logistic|distribution|transport|customs|supply|shipping|inventory"
        education = "educator|trainer|teacher|professor|lecturer"
        creative = "graphic|arts|adobe|draw|paint|visualize|bootstrap|storyboard|game|infographic|design|wireframe|illustrator|photoshop"
        recruitment = "recruit|hiring|hr|placement|staffing|hcm|human"
        construction = "construction|labor|labour|civil|architect|cadd|carpenter|mason|plumber|electrician"
        media ="media|social|blog|edit|hootsuite|sprout|webcast|advertis|relations|sales|marketing"
        clean_energy = "batteries|turbine|hydro|solar|wind|battery"
        banking ="bank|investment|brokerage|broker|financ|fund|hedge|revenue|debt|insurance|cash"
        real_estate = "property|real|estate|mortgage|property"
        engineer ="industrial|civil|mechanical|mettallurgy"
        aviation = "aviation|aeronautic"
        airlines = "pilot|airline|airhostess|air"
        bpo = "bpo|kpo|ites|call"
        entertainment ="drama|theatre|cinema|camera"
        facility = "fms|facility|hvac"
        food = "food|brewery|distillery|bake|baking|cook|cullinary|chef"
        leather ="tanning|animal"
        legal = "law|court|justice|advocate"
        manufacturing = "production|manufacturing|fabrication|factory|oem"
        mining = "geology|earth|drill|mining|mine"
        music = "recording|music|voice|studio|mic"
        broadcast = "televis|journalism|news|broadcast"
        oil = "petrol|oil|gas|offshore|chemical|drill"
        professional_services = "accounting|book|keeping|chartered|cpa|advisory"
        tax = "tax|laws|irs|income"
        telecomunication = "isp|tsp|internet|telecom|cable"
        fashion = "fashion|textile|garment|stitch|cloth|merch|apparel"
        wellness = "therapy|wellness|fitness|workout|stylist|salon|massage|haircut"
        tourism = "tourism|travel"
        electronic = "instrumentation|electronic"

        res = text.split()


        if 1:
            for i in range(len(res)):
                    if res[i].isalpha():
                            res[i] =res[i].lower()
                            if re.search(information_technology_re,res[i]):
                                industry_count[0]+=1
                            elif re.search(healthcare,res[i]):
                                industry_count[1] +=1
                            elif re.search(hospitality,res[i]):
                                industry_count[2] +=1
                            elif re.search(pharmacy,res[i]):
                                industry_count[3] +=1
                            elif re.search(logistics,res[i]):
                                industry_count[4] +=1
                            elif re.search(education,res[i]):
                                industry_count[5] +=1
                            elif re.search(creative,res[i]):
                                industry_count[6] +=1
                            elif re.search(recruitment,res[i]):
                                industry_count[7] +=1
                            elif re.search(construction,res[i]):
                                industry_count[8] +=1
                            elif re.search(media,res[i]):
                                industry_count[9] +=1
                            elif re.search(clean_energy,res[i]):
                                industry_count[10] +=1
                            elif re.search(banking,res[i]):
                                industry_count[11] +=1
                            elif re.search(real_estate,res[i]):
                                industry_count[12] +=1
                            elif re.search(engineer,res[i]):
                                industry_count[13] +=1
                            elif re.search(aviation,res[i]):
                                industry_count[14] +=1
                            elif re.search(airlines,res[i]):
                                industry_count[15] +=1
                            elif re.search(bpo,res[i]):
                                industry_count[16] +=1
                            elif re.search(entertainment,res[i]):
                                industry_count[17] +=1
                            elif re.search(facility,res[i]):
                                industry_count[18] +=1
                            elif re.search(food,res[i]):
                                industry_count[19] +=1
                            elif re.search(leather,res[i]):
                                industry_count[20] +=1
                            elif re.search(legal,res[i]):
                                industry_count[21] +=1
                            elif re.search(manufacturing,res[i]):
                                industry_count[22] +=1
                            elif re.search(mining,res[i]):
                                industry_count[23] +=1
                            elif re.search(music,res[i]):
                                industry_count[24] +=1
                            elif re.search(broadcast,res[i]):
                                industry_count[25] +=1
                            elif re.search(oil,res[i]):
                                industry_count[26] +=1
                            elif re.search(professional_services,res[i]):
                                industry_count[27] +=1
                            elif re.search(tax,res[i]):
                                industry_count[28] +=1
                            elif re.search(telecomunication,res[i]):
                                industry_count[29] +=1
                            elif re.search(fashion,res[i]):
                                industry_count[30] +=1
                            elif re.search(wellness,res[i]):
                                industry_count[31] +=1
                            elif re.search(tourism,res[i]):
                                industry_count[32] +=1
                            elif re.search(electronic,res[i]):
                                industry_count[33] +=1

        output = ["","",""]

 
        
        for i in range(len(output)):
            if sum(industry_count)>0:
                if output[i] == "":
                    
                    index_industry = industry_count.index(max(industry_count))  
                    if index_industry==0:
                        if industry_count[index_industry]>4:
                            output[i]= industry_type[index_industry]
                    else :
                        output[i]= industry_type[index_industry]
                    industry_count[index_industry]=0
        one_output = output[0]
        return one_output

    except:
        return ""