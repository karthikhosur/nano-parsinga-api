import re
import os


city_names_india = [" abohar "," achalpur "," adilabad "," adityapur "," adoni "," adrymbai "," agartala "," agra "," ahmadabad "," ahmadnagar "," ahmed nagar "," ahmedabad "," aizawl "," ajmer "," akbarpur "," akola "," alandur "," alappuzha "," aligarh "," alirajpur "," allahabad "," almora "," alwar "," ambala "," ambala sadar "," ambarnath "," ambattur "," ambedkar nagar "," ambikapur "," ambur "," amravati "," amreli "," amritsar "," amroha "," anand "," anantapur "," ananthapur "," ananthnag "," anantnag "," angul "," anuppur "," araria "," ariyalur "," arlu "," arrah "," arwal "," asansol "," ashok nagar "," ashoknagar kalyangarh "," auraiya "," aurangabad "," aurangabad(bh) "," avadi "," azamgarh "," badlapur "," bagaha "," bagalkot "," bageshwar "," bagpat "," bahadurgarh "," baharampur "," bahraich "," baidyabati "," balaghat "," balangir "," baleshwar town "," baleswar "," ballia "," bally "," bally city "," balrampur "," balurghat "," banaskantha "," banda "," bandipur "," bangalore "," bangalore rural "," banka "," bankura "," bansberia "," banswara "," barabanki "," baramulla "," baran "," baranagar "," barasat "," baraut "," barddhaman "," bardhaman "," bareilly "," bargarh "," baripada town "," barmer "," barnala "," barpeta "," barrackpur "," barshi "," barwani "," basirhat "," bastar "," basti "," batala "," bathinda "," beawar "," beed "," begusarai "," belgaum "," bellary "," bengaluru "," bettiah "," betul "," bhadrak "," bhadravati "," bhadreswar "," bhagalpur "," bhalswa jahangir pur "," bhandara "," bharatpur "," bharuch "," bhatpara "," bhavnagar "," bhilai nagar "," bhilwara "," bhimavaram "," bhind "," bhiwadi "," bhiwandi "," bhiwani "," bhojpur "," bhopal "," bhubaneswar "," bhuj "," bhusawal "," bid "," bidar "," bidhan nagar "," biharsharif "," bijapur "," bijapur(cgh) "," bijapur(kar) "," bijnor "," bikaner "," bilaspur "," bilaspur (hp) "," bilaspur(cgh) "," birbhum "," bishnupur "," bokaro "," bokaro steel city "," bombay "," bongaigaon "," bongaon "," botad "," boudh "," brahmapur town "," budaun "," budgam "," bulandshahr "," buldhana "," bundi "," burari "," burhanpur "," buxar "," cachar "," central delhi "," chamba "," chamoli "," champawat "," champdani "," champhai "," chamrajnagar "," chandannagar "," chandauli "," chandausi "," chandel "," chandigarh "," chandrapur "," changlang "," chapra "," chas "," chatra "," chennai "," chhatarpur "," chhattarpur "," chhindwara "," chickmagalur "," chikkaballapur "," chikmagalur "," chilakaluripet "," chitradurga "," chitrakoot "," chittaurgarh "," chittoor "," chittorgarh "," churachandpur "," churu "," coimbatore "," cooch behar "," cuddalore "," cuddapah "," cuttack "," dabgram "," dadra & nagar haveli "," dahod "," dakshina kannada "," dallo pura "," daman "," damoh "," dantewada "," darbhanga "," darjiling "," darrang "," datia "," dausa "," davanagere "," davangere "," debagarh "," deesa "," dehradun "," dehri "," delhi "," delhi cantonment "," deoghar "," deoli "," deoria "," dewas "," dhalai "," dhamtari "," dhanbad "," dhar "," dharmapuri "," dharmavaram "," dharwad "," dhaulpur "," dhemaji "," dhenkanal "," dholpur "," dhubri "," dhule "," dibang valley "," dibrugarh "," dimapur "," dinapur nizamat "," dindigul "," dindori "," diu "," doda "," dum dum "," dumka "," dungarpur "," durg "," durgapur "," east champaran "," east delhi "," east garo hills "," east godavari "," east kameng "," east khasi hills "," east midnapore "," east nimar "," east siang "," east sikkim "," east singhbhum "," eluru "," english bazar "," ernakulam "," erode "," etah "," etawah "," faizabad "," faridabad "," faridkot "," farrukhabad "," farrukhabad-cum-fatehgarh "," fatehabad "," fatehgarh sahib "," fatehpur "," fazilka "," firozabad "," firozpur "," gadag "," gadag-betigeri "," gadchiroli "," gajapati "," gandhi nagar "," gandhidham "," gandhinagar "," ganganagar "," gangapur city "," gangawati "," ganj "," ganjam "," garhwa "," gariaband "," gautam buddha nagar "," gaya "," ghaziabad "," ghazipur "," giridh "," giridih "," goalpara "," godda "," godhra "," gokal pur "," golaghat "," gonda "," gondal "," goas "," gondia "," gondiya "," gopalganj "," gorakhpur "," greater hyderabad "," greater mumbai "," greater noida "," gudivada "," gulbarga "," gumla "," guna "," guntakal "," guntur "," gurdaspur "," gurgaon "," gurugram "," guwahati "," gwalior "," habra "," hailakandi "," hajipur "," haldia "," haldwani-cum-kathgodam "," halisahar "," hamirpur "," hamirpur(hp) "," hanumangarh "," haora "," hapur "," harda "," hardoi "," hardwar "," haridwar "," hassan "," hastsal "," hathras "," haveri "," hazaribag "," hindaun "," hindupur "," hinganghat "," hingoli "," hisar "," hooghly "," hoshangabad "," hoshiarpur "," hospet "," hosur "," howrah "," hubli-dharwad "," hugli-chinsurah "," hyderabad "," ichalkaranji "," idukki "," imphal "," imphal east "," imphal west "," indore "," jabalpur "," jagadhri "," jagatsinghapur "," jagdalpur "," jaintia hills "," jaipur "," jaisalmer "," jajapur "," jalandhar "," jalaun "," jalgaon "," jalna "," jalor "," jalpaiguri "," jamalpur "," jammu "," jamnagar "," jamshedpur "," jamtara "," jamui "," jamuria "," janjgir-champa "," jashpur "," jaunpur "," jehanabad "," jetpur navagadh "," jhabua "," jhajjar "," jhalawar "," jhansi "," jharsuguda "," jhujhunu "," jhunjhunun "," jind "," jodhpur "," jorhat "," junagadh "," jyotiba phule nagar "," k.v.rangareddy "," kachchh "," kadapa "," kaimur (bhabua) "," kaithal "," kakinada "," kalahandi "," kalol "," kalyani "," kamarhati "," kamrup "," kancheepuram "," kanchipuram "," kanchrapara "," kandhamal "," kangra "," kanker "," kannauj "," kannur "," kanpur "," kanpur city "," kanpur dehat "," kanpur nagar "," kanyakumari "," kapurthala "," karaikal "," karaikkudi "," karauli "," karawal nagar "," karbi anglong "," kargil "," karim nagar "," karimganj "," karimnagar "," karnal "," karur "," kasargod "," kasganj "," kashipur "," kathua "," katihar "," katni "," kaushambi "," kawardha "," kendrapara "," kendujhar "," khagaria "," khammam "," khandwa "," khanna "," kharagpur "," khardaha "," khargone "," kheda "," kheri "," khora "," khorda "," khunti "," khurja "," kinnaur "," kiphire "," kirari suleman nagar "," kishanganj "," kishangarh "," kochi "," kodagu "," koderma "," kohima "," kokrajhar "," kolar "," kolasib "," kolhapur "," kolkata "," kollam "," koppal "," koraput "," korba "," koriya "," kota "," kottayam "," kozhikode "," krishna "," krishnagiri "," krishnanagar "," kulgam "," kullu "," kulti "," kumbakonam "," kupwara "," kurichi "," kurnool "," kurukshetra "," kurung kumey "," kushinagar "," lahul & spiti "," lakhimpur "," lakhisarai "," lakshadweep "," lalitpur "," latehar "," latur "," lawngtlai "," leh "," lohardaga "," lohit "," longleng "," loni "," lower subansiri "," lucknow "," ludhiana "," lunglei "," machilipatnam "," madanapalle "," madavaram "," madhepura "," madhubani "," madhyamgram "," madurai "," mahabub nagar "," maharajganj "," mahasamund "," mahbubnagar "," mahe "," mahendragarh "," mahesana "," maheshtala "," mahoba "," mainpuri "," malappuram "," malda "," malegaon "," malerkotla "," malkangiri "," mammit "," mandi "," mandla "," mandoli "," mandsaur "," mandya "," mangalore "," mango "," mansa "," marigaon "," mathura "," maunath bhanjan "," mayurbhanj "," medak "," medinipur "," meerut "," mira bhayander "," miryalaguda "," mirzapur "," mirzapur-cum-vindhyachal "," modinagar "," moga "," mohali "," mokokchung "," mon "," moradabad "," morena "," morvi "," motihari "," mughalsarai "," muktsar "," mumbai "," munger "," murshidabad "," murwara "," mustafabad "," muzaffarnagar "," muzaffarpur "," mysore "," nabadwip "," nabarangapur "," nadia "," nadiad "," nagaon "," nagapattinam "," nagaur "," nagda "," nagercoil "," nagpur "," naihati "," nainital "," nalanda "," nalbari "," nalgonda "," namakkal "," nanded "," nanded waghala "," nandurbar "," nandyal "," nangloi jat "," narasaraopet "," narayanpur "," narmada "," narsinghpur "," nashik "," navi mumbai "," navsari "," nawada "," nawanshahr "," nayagarh "," neemuch "," nellore "," new delhi "," neyveli "," nicobar "," nilgiris "," nizamabad "," noida "," north 24 parganas "," north and middle andaman "," north barrackpur "," north cachar hills "," north delhi "," north dinajpur "," north dum dum "," north goa "," north sikkim "," north tripura "," north west delhi "," nuapada "," ongole "," orai "," osmanabad "," ozhukarai "," pakur "," palakkad "," palamau "," palanpur "," pali "," pallavaram "," palwal "," panch mahals "," panchkula "," panihati "," panipat "," panna "," panvel "," papum pare "," parbhani "," patan "," pathanamthitta "," pathankot "," patiala "," patna "," pauri garhwal "," perambalur "," peren "," phek "," pilibhit "," pimpri chinchwad "," pithampur "," pithoragarh "," pondicherry "," poonch "," porbandar "," port blair "," prakasam "," pratapgarh "," proddatur "," puducherry "," pudukkottai "," pulwama "," pune "," puri "," purnia "," puruliya "," rae bareli "," raebareli "," raichur "," raiganj "," raigarh "," raigarh(mh) "," raipur "," raisen "," rajahmundry "," rajapalayam "," rajarhat gopalpur "," rajauri "," rajgarh "," rajkot "," rajnandgaon "," rajpur sonarpur "," rajsamand "," ramagundam "," ramanagar "," ramanathapuram "," ramgarh "," rampur "," ranchi "," ranibennur "," raniganj "," ratlam "," ratnagiri "," raurkela industrial township "," raurkela town "," rayagada "," reasi "," rewa "," rewari "," ri bhoi "," rishra "," robertson pet "," rohtak "," rohtas "," roorkee "," ropar "," rudraprayag "," rudrapur "," rupnagar "," s.a.s. nagar "," sabarkantha "," sagar "," saharanpur "," saharsa "," sahibganj "," saiha "," salem "," samastipur "," sambalpur "," sambhal "," sangli "," sangli miraj kupwad "," sangrur "," sant kabir nagar "," sant ravidas nagar "," santipur "," saran "," sasaram "," satara "," satna "," sawai madhopur "," secunderabad "," sehore "," senapati "," seoni "," seraikela-kharsawan "," serampore "," serchhip "," shahdol "," shahjahanpur "," shajapur "," shamli "," sheikhpura "," sheohar "," sheopur "," shikohabad "," shillong "," shimla "," shimoga "," shivpuri "," shrawasti "," sibsagar "," siddharthnagar "," sidhi "," sikar "," silchar "," siliguri "," simdega "," sindhudurg "," singrauli "," sirmaur "," sirohi "," sirsa "," sitamarhi "," sitapur "," sivaganga "," siwan "," solan "," solapur "," sonapur "," sonbhadra "," sonipat "," sonitpur "," south 24 parganas "," south andaman "," south delhi "," south dinajpur "," south dum dum "," south garo hills "," south goa "," south sikkim "," south tripura "," south west delhi "," srikakulam "," srinagar "," sujangarh "," sultan pur majra "," sultanpur "," sundergarh "," supaul "," surat "," surendra nagar "," surendranagar dudhrej "," surguja "," suryapet "," tadepalligudem "," tadpatri "," tambaram "," tamenglong "," tapi "," tarn taran "," tawang "," tehri garhwal "," tenali "," thane "," thanesar "," thanjavur "," the dangs "," theni "," thiruvananthapuram "," thoothukkudi "," thoubal "," thrissur "," tikamgarh "," tinsukia "," tirap "," tiruchirappalli "," tirunelveli "," tirupati "," tiruppur "," tiruvallur "," tiruvannamalai "," tiruvarur "," tiruvottiyur "," titagarh "," tonk "," tuensang "," tumkur "," tuticorin "," udaipur "," udgir "," udham singh nagar "," udhampur "," udupi "," ujjain "," ukhrul "," ulhasnagar "," uluberia "," umaria "," una "," unnao "," upper siang "," upper subansiri "," urwati "," uttara kannada "," uttarkashi "," uttarpara kotrung "," vadodara "," vaishali "," valsad "," varanasi "," vasai virar city "," vellore "," veraval "," vidisha "," vijayawada "," villupuram "," virudhunagar "," visakhapatnam "," vizianagaram "," warangal "," wardha "," washim "," wayanad "," west champaran "," west delhi "," west garo hills "," west godavari "," west kameng "," west khasi hills "," west midnapore "," west nimar "," west siang "," west sikkim "," west singhbhum "," west tripura "," wokha "," yadgir "," yamuna nagar "," yamunanagar "," yavatmal "," zunhebotto "]


us_states_short = [ " AK "," AL "," AR "," AZ "," CA "," CO "," CT "," DC "," DE "," FL "," GA "," GU "," HI "," IA "," ID "," IL "," IN "," KS "," KY "," LA "," MA "," MD "," ME "," MI "," MN "," MO "," MS "," MT "," NC "," ND "," NE "," NH "," NJ "," NM "," NV "," NY "," OH "," OK "," OR "," PA "," PR "," RI "," SC "," SD "," TN "," TX "," UT "," VA "," VI "," VT "," WA "," WI "," WV "," WY "]


us_states_full = ["alaska","alabama","arkansas","arizona","california","colorado","connecticut","washington dc","delaware","florida","georgia","guam","hawaii","iowa","idaho","illinois","indiana","kansas","kentucky","louisiana","massachusetts","maryland","maine","michigan","minnesota","missouri","mississippi","montana","north carolina","north dakota","nebraska","new hampshire","new jersey","new mexico","nevada","new york","ohio","oklahoma","oregon","pennsylvania","puerto rico","rhode island","south carolina","south dakota","tennessee","texas","utah","virginia","virgin islands","vermont","washington","wisconsin","west virginia","wyoming"]

us_states_full_text ="Alaska|Alabama|Arkansas|Arizona|California|Colorado|Connecticut|Washington DC|Delaware|Florida|Georgia|Guam|Hawaii|Iowa|Idaho|Illinois|Indiana|Kansas|Kentucky|Louisiana|Massachusetts|Maryland|Maine|Michigan|Minnesota|Missouri|Mississippi|Montana|North Carolina|North Dakota|Nebraska|New Hampshire|New Jersey|New Mexico|Nevada|New York|Ohio|Oklahoma|Oregon|Pennsylvania|Puerto Rico|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Virginia|Virgin Islands|Vermont|Washington|Wisconsin|West Virginia|Wyoming|ALASKA|ALABAMA|ARKANSAS|ARIZONA|CALIFORNIA|COLORADO|CONNECTICUT|WASHINGTON DC|DELAWARE|FLORIDA|GEORGIA|GUAM|HAWAII|IOWA|IDAHO|ILLINOIS|INDIANA|KANSAS|KENTUCKY|LOUISIANA|MASSACHUSETTS|MARYLAND|MAINE|MICHIGAN|MINNESOTA|MISSOURI|MISSISSIPPI|MONTANA|NORTH CAROLINA|NORTH DAKOTA|NEBRASKA|NEW HAMPSHIRE|NEW JERSEY|NEW MEXICO|NEVADA|NEW YORK|OHIO|OKLAHOMA|OREGON|PENNSYLVANIA|PUERTO RICO|RHODE ISLAND|SOUTH CAROLINA|SOUTH DAKOTA|TENNESSEE|TEXAS|UTAH|VIRGINIA|VIRGIN ISLANDS|VERMONT|WASHINGTON|WISCONSIN|WEST VIRGINIA|WYOMING"

personal_info_headings= ["personal"]


def extract_address(text,phone_number):
    try:
        # india code =0 and us code =1 
        country_code = 1 
        address={"postal_code":" ","place_name":" ","state_name":" ","city_name":" ","area_name":" ","longitude":" ","latitude":" "}
        pincode = ""
        ind_pincode = ""
        indian_city= ""
        us_pincode =""
        us_city= ""
        state_name =""


        text = re.sub("\.|\-|,|\n"," ",text)



        # Indian Address

        #Search for Indian Pincode
        if re.search(r"\b\d{3}\s{0,1}\d{3}\b",text) :
            try:
                ind_pincode =str(re.search(r"\b\d{3}\s{0,1}\d{3}\b",text)[0])
                ind_pincode = re.sub("\s","",ind_pincode)
                if  re.search(ind_pincode,phone_number):
                    ind_pincode = ""
            except:
                ind_pincode = ""
            

        
        for i in range(len(city_names_india)):
            if re.search(city_names_india[i],text.lower()) :
                if len(re.search(city_names_india[i],text.lower())[0])>4:
                    indian_city = re.search(city_names_india[i],text.lower())[0]
                    break
        
        if indian_city == "" or  ind_pincode == "":
            try:
                if re.search(r"\b\d{5}([-+]?\d{4})?\b",text):
                    us_pincode=str(re.search(r"\b\d{5}([-+]?\d{4})?\b",text)[0])
                    us_pincode =re.sub("\s","",us_pincode)
                if re.search(us_pincode,phone_number):
                    us_pincode =""
            except:
                us_pincode =""

            if re.search(r"\b\d{5}\b",text):
                try:
                    us_pincode = re.search(r"\b\d{5}\b",text)[0]
                    us_pincode =re.sub("\s","",us_pincode)
                    if  re.search(us_pincode,phone_number):
                        us_pincode= ""
                except:
                    us_pincode= ""

            text = re.sub("[^A-Z\s]+"," ", text)
            for i in range(len(us_states_short)):
                if re.search(us_states_short[i],text):
                    state_name = us_states_full[i]

            if state_name == "":

                if re.search(us_states_full_text,text):
                    state_name = re.search(us_states_full_text,text)[0]

        

        if ind_pincode != "":
            country_code = 0
            address["postal_code"] = ind_pincode
        if us_pincode != "":
            country_code=1
            address["postal_code"] = us_pincode
        if indian_city != "":
            country_code =0
            address["place_name"] = indian_city
            address["city_name"] = indian_city
        if state_name != "":
            country_code=1
            address["place_name"] = state_name
            address["city_name"] = state_name
        return address,country_code
    except:

        return address,country_code

def extract_dob(text):
    try:
        birth_date = ""
        match_dob=""
        dob_words = "Born on|Date of birth|Birth|DOB :|DOB|DOB:|DATE OF BIRTH|Birth Date|Birth :|D.O.B|d. o. b|d o b|d  o  b|date and place of birth:|date and place of birth|date and country of birth|dateofbirth|data of birth|date of  birth|birthdate|date of birth/age:|date of birth/age|date of birthage|b\\'date|b’date|date  of  birth|date of birth|date ofbirth|dob|date & place of birth|d.o.b|date of birth|date-of-birth|date   of   birth|BORN:"
        date_text = ""
        if re.search(dob_words,text):
            date_end = re.search(dob_words,text).end() 
            date_text = text[date_end:date_end+20]
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

def passport_no(text):
    try:
        pno=""
        passport_regex = "[A-PR-WY][1-9]\\d" +\
                "\\s?\\d{4}[1-9]"
        if re.search(passport_regex,text):
            pno =  re.search(passport_regex,text)[0]

        return pno 
    except:
        return ""