# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:26:24 2019

@author: Asus
"""

from nltk.tokenize import sent_tokenize, word_tokenize
#from collections import Counter 
# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

f=open("Text.txt", "r")
pre2=["to","from","at","in"] 
whQues=["who","what","where","how","why","when","which"]
if f.mode == 'r':
    contents =f.read()
    #print(contents)
    f.close()
    sent22= sent_tokenize(contents)
    wordnet_lemmatizer22 = WordNetLemmatizer()
    ENGLISH_STOPS22 = set(stopwords.words('english'))

# Lemmatize all tokens into a new list: lemmatized

    #print(sent2)
    f= open("write112.doc","w+")
    for i in sent22:
        words2 = word_tokenize(i)
        print(words2)
        lower_tokens = [t.lower() for t in words2]
        #f.write("%s" %[wordnet_lemmatizer.lemmatize(t) for t in words])
        
        #no_stops = [t for t in lower_tokens if t not in ENGLISH_STOPS]
        no_stops22= []

# Remove all stop words: no_stops
        for t in lower_tokens:
            if t in pre2 or t not in ENGLISH_STOPS22:
        #if t not in extra:
                no_stops22.append(t)
        lemmatized = [wordnet_lemmatizer22.lemmatize(t) for t in no_stops22]
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

def answerDoc(Qus,no):
    print("comee")
    f= open("write112.doc","r")
    if f.mode == 'r':
        contents =f.read()
    f.close()
    sent2= sent_tokenize(contents)
   # wordnet_lemmatizer23 = WordNetLemmatizer()
    Array=[]
    name=0
    num=0
    for t in Qus:
        if t=="to":
            t="in"
        if t=="name":
            name=1
            continue
        elif t=="number":
            num=1
            continue
        Array.append(t)
        print(t)
    cc=len(Array)
    snt=[]
    for i in sent2:
        words2 = word_tokenize(i)
        cnt=0
        
        for t in Array:
            for j in words2:
                if t==j:
                    cnt+=1
                    break
                
        if cnt>=cc:
            
            print("Matched:")
            print(i)
            kk=len(words2)
            kkk=len(Array)
           
            if no==1:
                ff=0
                jf=0
                jt=0
                for j in range(0,kk-1):
                    if words2[j]=="from":
                        jf=j
                    elif words2[j]=="in":
                        jt=j
                for j in range(0,kkk):
                    if Array[j]=="in":
                        ff=1
                    elif Array[j]=="from":
                        ff=2
                if ff==1:
                    for jj in Array:
                        if jj==words2[jt+1]:
                            print("Ans: "+words2[jf+1])
                            
                            break
                    
                elif ff==2:
                    for jj in Array:
                        if jj==words2[jf+1]:
                            print("Ans: "+words2[jt+1])
                            
                            break
            
                    #print("Ans: "+words2[jt+1])
                    #break;
                elif ff==0 and jf!=0 and jt!=0:
                    print("Ans: "+words2[jf+1]+"-"+words2[jt+1]+" Route")
                    
            
            elif no==2:
                
                jf=0
                jt=0
                ff=0
                m=0
                n=0
                nt=0
                
                for j in range(0,kk-1):
                    if words2[j]=="from":
                        jf=j
                    elif words2[j]=="in":
                        jt=j
                    elif words2[j]=="train":
                        nt=j
                        ff=1
                        
                for j in range(0,kkk):
                    if Array[j]==words2[jf+1]:
                        m=1
                        
                    elif Array[j]==words2[jt+1]:
                        n=1
                        
                        
                print(m)
                print(n)
                print(ff)
                if m==1 and n==1 and ff==1:
                    if name==1:
                        print("Ans: "+words2[nt+3])
                        #if i not in snt:
                        snt.append(words2[nt+3])
                        
                            
                    elif num==1:
                        print("Ans: "+words2[nt+1])
                        
                        #snt.append(i)
                    else:
                        print("Ans: no "+words2[nt+1]+" "+words2[nt+3])
                        #if i not in snt:
                        snt.append(words2[nt+3])
                    
                    
               
                    
                    
                    
            elif no==3:
                ff=0
                for jj in range(0,kk):
                    #re_matchData = re.compile(r"(\d{3,4})")
                    if words2[jj]==Array[0] and words2[jj-3]=="train":
                        print("Ans: "+words2[jj-2])
                        ff=1
                        break
                if ff==0:
                    print("No such train found")
                    
                        
                        
                        
            elif no==4:
                ff=0
                for jj in range(0,kk):
                    #re_matchData = re.compile(r"(\d{3,4})")
                    if words2[jj]==Array[0] and words2[jj-1]=="train":
                        print("Ans: "+words2[jj+2])
                        ff=1
                        break
                if ff==0:
                    print("No such train found")
            elif no==6:
                for j in range(0,kk-1):
                    
                    if words2[j]=="offday":
                        if words2[j+1]==",":
                            print("Ans: No offday")
                            break
                        else:
                            print("Ans : "+words2[j+2])
                            break
                
    list_set = set(snt) 
    # convert the set to the list 
    unique_list = (list(list_set))
    for x in unique_list: 
        print(x)
    lent=len(unique_list)
    if no==2:
        print("Total trains: ")
        print(lent)
                                
                    
                     
                
        
                
           
            
#What is offday of turna       
            
            
            