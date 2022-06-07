import json
import spacy
nlp = spacy.load("en_core_web_lg")

def process_text(text):
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    return " ".join(result)

def get_translations_data(soorah): 
    translations = {} 
    f = open('quran_en.json')  
    try:
        data = json.load(f) 
        for verse in data[soorah-1]['verses']: 
              translations[process_text(verse['translation'])] = str(soorah)+":"+str(verse['id']) 
    except:
        pass 
    f.close()
    return translations 

def calculate_similarity(soorah): 
    verse_with_score = {}
    translations = get_translations_data(soorah)
    for base_verse in translations.keys():
        for compare_verse in translations.keys():
            if base_verse != compare_verse:
                score = nlp(base_verse).similarity(nlp(compare_verse))
                verse_with_score[base_verse] = score
    return verse_with_score 
    
def find_max_score_verse_no(soorah): 
    verse_with_score = calculate_similarity(soorah)
    max_score_verse = max(zip(verse_with_score.values(), verse_with_score.keys()))[1] 
    translations = get_translations_data(soorah)
    return translations[max_score_verse]


soorah = int(input("Enter soorah number : "))
print(find_max_score_verse_no(soorah)) 