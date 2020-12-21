import nltk 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer() 
import numpy 
import tflearn 
import tensorflow 
import random 
import json 

with open('intents.json') as file:
    data = json.load(file) 

words = []
labels = [] 
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['patterns']: 
        wrds = nltk.word_tokenize(pattern) 
        words.extend(wrds)
        docs_x.append(wrds), 
        docs_y.append(intent["tag"])
    
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w != "?"] 
words = sorted(list(set(words))) 
labels = sorted(labels)
