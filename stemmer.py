#!/usr/local/bin/python3
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

new_text="…earnings and employment data from the March Current Population Surveys covering years 1967-1997"
sentences=sent_tokenize(new_text)
words = word_tokenize(new_text)
print(nltk.pos_tag(words))
for s in sentences:
	words = word_tokenize(s)
	for w in words:
		print(w)

