import re
import os
from ahocorasick import Automaton
import string
from spellchecker import SpellChecker

spell = SpellChecker()

indian_surnames = []

def name_extractor_v3(text, terms, email_id, file_type, filename, phone_no):
    try: 
        terms = terms[:10] # Only first 10 terms are considered for name extraction
        
        name_text = ""
        # Remove the Number and Email ID from the terms
        
        terms = del_num_email(terms, email_id, phone_no)
        terms = clean_text(terms)
        print("terms v3",terms)
        name_text = confirm_format(terms)

        return name_text
    except:
        return ""

def clean_text(terms):
    temp_terms = []
    for i in range(len(terms)):
        temp_text = remove_extra_spaces(terms[i])
        temp_text = remove_punctuation(temp_text)
        if len(temp_text.split()) < 10 and len(temp_text) < 95:
            temp_text =check_if_in_dict(temp_text) 
            if len(temp_text.split()) >1 and len(temp_text) > 8 and len(temp_text) < 40 and len(temp_text.split()) < 7:
                temp_terms.append(temp_text)
    return temp_terms
        
def check_if_in_dict(text):
    text_terms = text.split()
    misspelled = spell.unknown(text_terms)
    text = ""
    for word in text_terms:
        if word.lower() in misspelled:
            text+=word + " "
    return text

def remove_extra_spaces(text):
    text = re.sub(r'\s+', ' ', text)
    return text

def remove_punctuation(text):
    text =  re.sub(r'[^\w\s]', ' ', text)
    return text

def del_num_email(terms, email_id, phone_no):
    for i in range(len(terms)):
        if email_id in terms[i]:
            terms[i] = re.sub(email_id, "", terms[i])
        if len(phone_no)> 4  and  phone_no[-4:] in terms[i]:
            terms[i] = ""
    temp_terms = []
    for i in range(len(terms)):
        if terms[i] != "":
            temp_terms.append(terms[i])

    terms = temp_terms

    return terms

def confirm_format(terms):
    for i in range(len(terms)):
        words = terms[i].split()
        temp = ""
        for w in words :
            if w[0].isupper() and len(w) > 1 :
                temp += w + " "
        if len(temp.split()) > 1 and len(temp.split()) < 6 and len(temp) < 40 and len(temp) >8 :
            return temp.upper()
    return ""
