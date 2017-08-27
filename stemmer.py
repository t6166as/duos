#!/usr/local/bin/python3
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
new_text='crazy datasets are dancing on hot tin roof data'
words = word_tokenize(new_text)
#ps=Stemmer()
ps = PorterStemmer()
print(ps.stem("how  are you doing today"))
for w in words:
 print(ps.stem(w))

