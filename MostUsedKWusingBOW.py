# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:50:23 2020
author: Shoaib
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#import numpy as np
#import pandas as pd
#from nltk.tokenize import word_tokenize as WordTokenizer
import nltk
import codecs

with open('F://d4.csv', 'rb') as fp:
  paragraph = fp.read()

#Dcoding base64 data
paragraph = codecs.decode(paragraph,'utf-8')

#Data preprocessed with Trifacta
#Now cleaning Data
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
nltk.download('PorterStemmer')
from nltk.stem import WordNetLemmatizer

ps= PorterStemmer()
wordnet = WordNetLemmatizer()


sentences = nltk.sent_tokenize(str(paragraph))

corpus=[]
for i in range(len(sentences)):
        data = re.sub('[^a-zA-Z]', ' ', sentences[i])
        data = data.lower()
        data = data.split()
        data = [wordnet.lemmatize(word) for word in data  if not word in stopwords.words('english')]
        data = " ".join(data)
        corpus.append(data)
#       data = [ps.stem(word) for word in data  if not word in stopwords.words('english')]
        
         
# WordCount
MajorIssue = {} 
for data in corpus: 
	words = nltk.word_tokenize(data) 
	for word in words: 
		if word not in MajorIssue.keys(): 
			MajorIssue[word] = 1
		else: 
			MajorIssue[word] += 1

            


