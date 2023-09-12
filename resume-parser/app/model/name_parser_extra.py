
def name_extractor_extra(text, terms, email_id, file_type, filename, phone):
    name_text = ""
    name_text = name_in_beginning(text, terms, email_id, phone)
    return name_text     
def is_initial_uppercase(s):
    return all(word[0].isupper() for word in s.split() if word)
 
def name_in_beginning(text, terms, email_id, phone ):
    for i in range(0,6):
        if email_id not in terms[i].lower() and phone not in terms[i].lower():
            if is_initial_uppercase(terms[i]) and len(terms[i].split(" ")) < 4 and len(terms[i].split(" ")) > 0:
                return terms[i]
            
    return ""