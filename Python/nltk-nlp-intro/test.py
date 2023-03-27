import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = """At eight o'clock on Thursday morning
    Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print(tokens)