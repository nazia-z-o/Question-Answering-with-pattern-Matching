# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:24:48 2019

@author: Asus
"""

from nltk.tokenize import sent_tokenize, word_tokenize
#from collections import Counter 
# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
f=open("Document.txt", "r")
pre2=["to","from","at","in"] 
if f.mode == 'r':
    contents =f.read()
    #print(contents)
    f.close()
    sent2= sent_tokenize(contents)
    wordnet_lemmatizer2 = WordNetLemmatizer()
    ENGLISH_STOPS2 = set(stopwords.words('english'))

# Lemmatize all tokens into a new list: lemmatized

    #print(sent2)
    f= open("write11.doc","w+")
    for i in sent2:
        words2 = word_tokenize(i)
        print(words2)
        lower_tokens = [t.lower() for t in words2]
        #f.write("%s" %[wordnet_lemmatizer.lemmatize(t) for t in words])
        
        #no_stops = [t for t in lower_tokens if t not in ENGLISH_STOPS]
        no_stops2= []

# Remove all stop words: no_stops
        for t in lower_tokens:
            if t in pre2 or t not in ENGLISH_STOPS2:
        #if t not in extra:
                no_stops2.append(t)
        lemmatized = [wordnet_lemmatizer2.lemmatize(t) for t in no_stops2]
        st=""
        for t in lemmatized:
            st=st+t+" "
        
        f.write(" %s " %st)
print(lemmatized)
# Create the bag-of-words: bow
#bow = Counter(lemmatized)

# Print the 10 most common tokens
#print(bow.most_common(10))
f.close()


#f= open("guru99.txt","w+")
#f.write(" %s" % words[:])