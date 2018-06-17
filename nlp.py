# Natural Language Processing 

#import Libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 



#cleaning the texts

import re 
import nltk
# nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 

inp = 'The problem I have is that they charge $11.99 for a sandwich that is no bigger than a Subway sub (which offers better and more amount of vegetables).'
sent = re.sub('[^a-zA-Z]', ' ' ,inp)
#converting to lowercase
sent = sent.lower()

# removing not significant words(stopwords)   # stemming : taking the root of the word(PorterStemmer)

sent = sent.split()
#ps = PorterStemmer()  # stemming is not working properly 

sent = [word for word in sent if not word in set(stopwords.words('english'))]
 
print(sent)