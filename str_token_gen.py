#!//usr/local/bin/python3
import nltk as nl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import argparse

def parse_args():
        parser=argparse.ArgumentParser( description ='supply string to be lemmatized')
        parser.add_argument('--string',required=True)
        return parser.parse_args()

def lemma(string):
 lemmatizer = WordNetLemmatizer()
 words=nl.word_tokenize(string)
 i=0
 tokens=[]
 for j in words:
   tokens.append(lemmatizer.lemmatize(j))
   i=i+1
   if i>4: break
 print(tokens)
 return tokens


def main():
        args = parse_args()
        lemma(args.string)


if __name__ == "__main__":
        main()
