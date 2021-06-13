import re
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
import os 



# load pre-trained model
base_path = os.path.dirname(__file__)

nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

file = os.path.join(base_path,"skills_words.txt")
file = open(file, "r", encoding='utf-8')
skill = [line.strip().lower() for line in file]
skillsmatcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(text) for text in skill if len(nlp.make_doc(text)) < 10]
skillsmatcher.add("Job title", None, *patterns)


def skills_extract(text):
    try:
        skills = []
        converted_list=[]
        converted_text=""
        
        __nlp = nlp(text)
            # Only run nlp.make_doc to speed things up

        for token in __nlp:
                if not token.is_stop and not token.is_punct:
                    if token.pos_ == "NOUN" or token.pos_ == "PROPN" :
                        if token.text  not in converted_list:

                            converted_list.append(token.text)
                            converted_text += " "+token.text
        extra_skills =[]
        nlp_new = nlp(converted_text.lower())
        matches = skillsmatcher(nlp_new)
        for match_id, start, end in matches:
            span = nlp_new[start:end]
            skills.append( span.text)
        
        return skills
    except:
        return []

