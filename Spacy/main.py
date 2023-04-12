import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

with open("text.txt") as f:
    text = f.read()

doc = nlp(text)

sentence_list = list(doc.sents)
sentence1 = sentence_list[0]

nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

