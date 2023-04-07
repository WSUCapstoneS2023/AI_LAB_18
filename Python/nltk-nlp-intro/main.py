# import matplotlib
# import nltk
#https://realpython.com/nltk-nlp-python/
import nltk 
import tkinter as tk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download("maxent_ne_chunker")
nltk.download("words")

stop_words = set(stopwords.words("english"))

sentences = [    "The quick brown fox jumps over the lazy dog.", "The Porter stemming algorithm (or ‘Porter stemmer’) is a process for removing the commoner James Smith morphological and inflexional endings from words in English. Its main use is as part of a term normalisation process that is usually done when setting up Information Retrieval systems.",    "She sells seashells by the seashore.",    "My favorite color is blue.",    "The cat sat on the mat.",    "The sun rises in the east and sets in the west.",    "The book is on the table.",    "He likes to play soccer and basketball.",    "I have a headache and a fever.",    "The restaurant serves delicious food.",    "Sheila is a talented musician and a great writer."]

example_text = sentences[1]

tokenized_words = word_tokenize(example_text)

filtered_tokenization = [word for word in tokenized_words if word not in stop_words]

pos_tagged_words = nltk.pos_tag(filtered_tokenization)

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()     # reduce words to their base form. remove pre-post suffix

#print(tokenized_words)

# Converts the 
def toWordNetLabel(pos_label):
    if pos_label.startswith('R'):
        return "r"
    if pos_label.startswith('J'):
        return "a"
    if pos_label.startswith('V'):
        return "v"
    if pos_label.startswith('N'):
        return "n"
    # default return noun
    return "n"

tree = nltk.ne_chunk(pos_tagged_words, binary = True)
#tree.draw()
NEs = []
for t in tree:
    if hasattr(t, "label") and t.label() == "NE":
        for name in t:
            NEs.append(name)
#print(NEs)
# adj, adv, noun, verb
pos_tagged_words_converted = [(word, toWordNetLabel(p)) for word,p in pos_tagged_words]
lemmatized_words = [lemmatizer.lemmatize(word, pos=p) for word,p in pos_tagged_words_converted]

print(lemmatized_words)