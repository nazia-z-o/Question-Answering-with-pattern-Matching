# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:10:37 2019

@author: Asus
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter 
# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import re
ENGLISH_STOPS = set(stopwords.words('english'))
patCol=[]
patRow=[]
patRow.append(r"(from where |where )")
patRow.append(r"(does )?")
patRow.append(r"(the )*?")
patRow.append(r"(train )?")
patRow.append(r"(no |named )?")
patRow.append(r"([a-z]*|\d{3})")
patRow.append(r"( start | depart | leave | travel | pass )")
patRow.append(r"(from)?")
patCol.append(patRow)
patRow.clear()
patRow.append(r"(to where |where )")
patRow.append(r"(does )?")
patRow.append(r"(the )*?")
patRow.append(r"(train )?")
patRow.append(r"(no |named )?")
patRow.append(r"([a-z]*|\d{3})")
patRow.append(r"( go| reach| travel)")
patCol.append(patRow)
patRow.clear()
lenPattern=[8,7]
pre=[]
tokennns=[]
nouns=[]

train_name=['sundarban','rupsha']
def giveAnswer(train):
    if train=='707' or train=='sundarban':
        for t in nouns:
            if t=='dhaka':
                print('Answer: Khulna')
                break
            if t=='khulna':
                print('Answer: Dhaka')
                break
def pattern1match():
    flag=0
    for word,pos in nltk.pos_tag(tokennns):
        
        if pos =='CD':
            flag=1
            cd=word
        else:
            nouns.append(word)
        
        
    if flag==1:
        giveAnswer(cd)
    else:
        flagg=0
        for tt in train_name:
            for t in nouns:
                if t==tt and flagg==0:
                    giveAnswer(t)
                    flagg=1
                    break
            if flagg==1:
                break
         
            
        
        
        
    
def answer(patternNo,tokenn):
    for t in tokenn:
        if t not in ENGLISH_STOPS:
            tokennns.append(t);
            
    if patternNo==1:
        pattern1match()
def precision_count(strr,l):
    for i in 2:
        t=0
        for j in lenPattern[i]:
            for k in l:
                if re.search(patCol[i][j],strr[k]):
                    t=t+1
                    
        t=t/lenPattern[i]
        pre.append(t)
    maxx=-100
    num=0
    for i in 2:
        if pre[i]>maxx:
            maxx=pre[i]
            num=i
    print(num+1," precision:",maxx)
    return num
p=[]
p.append( r"(from where |where )(does )?(the )*?(train )?(no |named )?([a-z]*|\d{3})( start | depart | leave | travel | pass )(from )?(to )([a-z]*)")
p.append( r"(to where |where )(does )?(the )*?(train |train no |train named )? ([a-z]*|\d{3})( go | reach | travel )(to )?(from )([a-z]*)")
p.append( r"(what |give |tell )?(is |me |us )?(the )?(name |number |no )?(of )?(train |train no |train named |train number )([a-z]*|\d{3})")
p.append(r"(when |what )(does |is )?(the )?(time |starting time |departing time |traveling time )?(of )?(the )?(train |train no |train named )?([a-z]*|\d{3})( start | travel | depart )?(from )?[a-z]*")
p.append(r"(when |what )(does |is )?(the )?(time |arrival time )?(of )?(the )?(train |train no |train named )?([a-z]*|\d{3})( go | reach )?(in |to |at )? [a-z]*")
p.append(r"(which |what )(is )?(the )?(name |no )(of )?(train )(that )?(come |go |start |depart |leave |reach )?(from |to )?[a-z]*( from | to )?[a-z]*( at )?\d{2}\D{1}\d{2}?")
p.append(r"(on )?(which |give |tell )(day )?(is |me |us )?(the )?(offday )?(of )?(train |train no |train named )(\d{3}|[a-z]*)( does not )?(go)?")
p.append( r"(what |tell |give )?(is |me |us )?(the )?(fair |cost |price |fee |charge )(of )?(traveling |going )(from )?[a-z]*(to )[a-z]*(in )?(non-ac apartment|ac apartment)")
  
whQues=["who","what","where","how","when","why","which"]
pre=["to","from","in","at","on"]
inp=input("Enter Question:")
sent= sent_tokenize(inp)
print(sent)
for i in sent:
    words = word_tokenize(i)
print(words)
lower_tokens = [t.lower() for t in words]


# Retain alphabetic words: alpha_only
#alpha_only = [t for t in lower_tokens if t.isalpha()]


no_stops= []

# Remove all stop words: no_stops
for t in lower_tokens:
    if t in whQues or t in pre or t not in ENGLISH_STOPS:
        no_stops.append(t)

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
print(lemmatized)
# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))

string=""
for t in lemmatized:
    string=string+t+" "
print(string)
cnt=0 
m=0

for t in p:
    cnt=cnt+1
    if re.search(t,string):
        print("yes matched precision 1")
        print("Pattern ",cnt)
        print(t)
        m=1
        answer(cnt,lemmatized)
        break
if m==0:
    num=precision_count(string,len(string))
    print("Pattern ",num+1)
    print(p[num])
#  Where does the train Sudarban start from?