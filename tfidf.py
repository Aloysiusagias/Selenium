import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import ast
import numpy as np


df = pd.read_csv('data.csv')

# numOfWords = set(df['isi'][0])
# for i in df['isi']:
#     # numOfWords.union(set(i))
#     print(i)

# listOfStudents=df['isi'][0]
# print("List of Students:",listOfStudents) 
# uniqueNames=set(listOfStudents) 
# print("Set of uniqueNames:",uniqueNames)

def convert_text_list(texts):
    texts = ast.literal_eval(texts)
    return [text for text in texts]

df['isi_list'] = df['isi'].apply(convert_text_list)

def calc_TF(document):
    # Counts the number of times the word appears in review
    TF_dict = {}
    for term in document:
        if term in TF_dict:
            TF_dict[term] += 1
        else:
            TF_dict[term] = 1
    # Computes tf for each word
    for term in TF_dict:
        TF_dict[term] = TF_dict[term] / len(document)
    return TF_dict

df["TF_dict"] = df['isi_list'].apply(calc_TF)

# print(df['TF_dict'][0])

# Check TF result

# print('%20s' % "term", "\t", "TF\n")
# for key in df["TF_dict"][0]:
#     print('%20s' % key, "\t", df["TF_dict"][0][key])

def calc_DF(tfDict):
    count_DF = {}
    # Run through each document's tf dictionary and increment countDict's (term, doc) pair
    for document in tfDict:
        for term in document:
            if term in count_DF:
                count_DF[term] += 1
            else:
                count_DF[term] = 1
    return count_DF

DF = calc_DF(df["TF_dict"])
# print(DF)

n_document = len(df)

def calc_IDF(__n_document, __DF):
    IDF_Dict = {}
    for term in __DF:
        IDF_Dict[term] = np.log(__n_document / (__DF[term] + 1))
    return IDF_Dict
  
#Stores the idf dictionary
IDF = calc_IDF(n_document, DF)

# print(IDF)

#calc TF-IDF
def calc_TF_IDF(TF):
    TF_IDF_Dict = {}
    #For each word in the review, we multiply its tf and its idf.
    for key in TF:
        TF_IDF_Dict[key] = TF[key] * IDF[key]
    return TF_IDF_Dict

#Stores the TF-IDF Series
df["TF-IDF_dict"] = df["TF_dict"].apply(calc_TF_IDF)

print(df["TF-IDF_dict"][0])