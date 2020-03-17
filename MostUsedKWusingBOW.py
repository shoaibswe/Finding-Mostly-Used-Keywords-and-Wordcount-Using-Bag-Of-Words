# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:50:23 2020

@author: NTI/Shoaib
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
import numpy as np

#import pandas as pd
#from nltk.tokenize import word_tokenize as WordTokenizer

#paragraph=pd.read_csv(r'F:\\twdata.txt', encoding='latin1');
#paragraph=pd.read_csv('F:/data10032020.csv', sep=', ', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
#paragraph=pd.read_table('F://tst.txt')


import codecs
# Get the data from the file
with open('F://d4.csv', 'rb') as fp:
  paragraph = fp.read()

# The data is base64 encoded. Let's decode it.
paragraph = codecs.decode(paragraph,'utf-8')
#paragraph.columns=["text"]

#cleaning text
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
        review = re.sub('[^a-zA-Z]', ' ', sentences[i])
        review = review.lower()
        review = review.split()
        review = [wordnet.lemmatize(word) for word in review  if not word in stopwords.words('english')]
        review = " ".join(review)
        corpus.append(review)
#        review = [ps.stem(word) for word in review  if not word in stopwords.words('english')]
        
         
# WCount
MajorIssue = {} 
for data in corpus: 
	words = nltk.word_tokenize(data) 
	for word in words: 
		if word not in MajorIssue.keys(): 
			MajorIssue[word] = 1
		else: 
			MajorIssue[word] += 1

            


