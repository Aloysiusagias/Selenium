import pandas as pd;
import string 
import re #regex library
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

df = pd.read_csv('datasetberita.csv')
#Case Folding

def case_folding(text):
  text = text.lower()
  return text
df['isi'] = df['isi'].apply(case_folding)

#Tokenizing
def tokenizing(text):
  #remove angka
  text = re.sub(r"\d+","",text)
  #remove puntuation
  text = text.translate(str.maketrans("","",string.punctuation))
  #remove white space leading & trailing
  text = text.strip()
  #remove multiple whitespace into single whitespace
  text = re.sub('\s+',' ',text) 
  text = nltk.tokenize.word_tokenize(text)
  text = nltk.FreqDist(text)
  return text

df['isi'] = df['isi'].apply(tokenizing)

#get indonesia stop word
list_stopwords = set(stopwords.words('indonesian'))
#remove stopwords pada list token
def stopword(text):
  tokens_without_stopword = [word for word in text if not word in list_stopwords]
  return tokens_without_stopword

df['isi'] = df['isi'].apply(stopword)

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
def stem(text):
  output   = [stemmer.stem(token) for token in text]
  return output

df['isi'] = df['isi'].apply(stem)
df.to_csv('data.csv', index=False)