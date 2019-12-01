# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:18:10 2019

@author: CITY
"""

from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter 
# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import re

from DocAnswer import *
from documentToken import *
from fixed_answer import *
from WhereGoesOrComes import * #1
from RouteHowMany import * #2
from RouteTrainNameNo import * #2
from OnlyNumber import * #3
from OnlyName import * #4
from Offday import * #5&6
from listOfTrainsforAnyPlace import * #7
from train_time import * #8
from seatFair import * #9
from ACavailable import * #10
from trainAvailable import * #11
from nextStation import * #12
from how_long_it_takes import * #13


ENGLISH_STOPS = set(stopwords.words('english'))

lenPattern=[8,7]
whQues=["who","what","where","how","why","when","which"]
pre=["to","from","at","in"] 
yes_no=["is","can","are","does","there"]
extra=["approximate","approriate","there","express","station"]
cut=["why","buy","book","bought","coordinate","ticket"]

tokennns=[]
nouns=[]
place_add=[]
preA=[]
train_name=['701','702','703','704','705','706','707','708','709','710','711','712','713','714','715','716',
            '717','718','719','720','721','722','723','724','725','726','727','728','729','730','731','732','733','734','735',
            '736','737','738','739','740','741','742','743','744','745''746','747','748','749','750','751','752','753','754','755',
            '756','757','758','759','760','761','762','763','764','765','766','767','768','769','770','771','772','773',
            '774','775','776','777','778','779','780','781', '782','783','784','785','786','787', '788','789','790',
            '3107','3108','3109','3110','3129','3130',
            'augnibina',   
            'banalata','bandhan','bijoy','borendra','brahmaputro',
            'chitra', 
            'dhumkatu','doloncapa','drutajan',    
            'egarosindur_godhuli','egarosindur_provati','ekota', 
            'faridpur',
            'haowr',
            'jamuna','joyenteeka',    
            'kalni','kalukhali_vatiap','kishoreganj','korotaya','kopotakha','kurigram', 
            'lalmoni',
            'mahanagar','mahanagar_godhuli','mahanagar_provati','meghna','modhumati','moitree','mohonganj', 
            'padma','paharika','parabat',
            'nelsagore',
            'rangpur','rupsa',
            'seemanta','shagordari','silk_city','sirajganj','sonar_bangla','subarna','sundarban',
            'tista','titumir','turna',
            'udayan','upaban','upakul']



place_names=['abdulpur','accalpur','agimnagar','ahasangang','akhaura','alamdanga','amirgang','aowlia_nagar','arani','arikhola','ashuganj','azampur',
             'b_siajur_islam','badarganj','bajitpur','bamondanga','banani','bangabandhu_htp','barhatta','bbsetu_e','bbsetu_w','benapole','bhairab_bazar','bhairamara','bhanuganj','bhatiary','biman_bandar','birampur','birole','bogura','bojra','bonarpara','boral_bridge','bramanbaria',
             'chapainababganj','chapta','chatmohar','chilahati','chittagong','choumuhani','chuadanga','cirir_bandar','comilla','court_chandpur',
             'darsana','darsana_halt','daulatpur','da_cantonment','dewanganj_bazar','dhaka','dhoala','dinajpur','domar','durmut',
             'fatema_namar','feni',
             'gachihata','gafargaon','gaibandha','gobra','gouripur_myn','gunaboti',
             'hasanpur','horoshpur',
             'ibrahimabad','imam_bari','ishurdi','ishurdi_dhaka','ishurdi_bypass','islampur_bazar',
             'jamalpur','jamtail','jaydebpur','jessore','jhikargacha','joypurhat',
             'kaunia','kawrait','khanabari','khulna','kishoreganj','kismat','krishi_univarsity','kulaura','kuliarchar','kurigram',
             'lahirimohanpur','laksam','lalmonirhat',
             'madhnagar','maijdi_court','maizgaon','manik_khali','melandah_bazar','methikanda','mirpur','mirzapur','mobarakgong','mohera','mohonganj','montala','moshakhali','mouchak','mukundupur','muladuli','mymensingh'
             'nandina','nangalkot','narsingdi','nathar_patua','natore','nayapara','neelfamari','netrokona','noakhali','noapara','nurundi',
             'paghachong','panchabibi','panchagarh','parbatipur','phulbari','pirgacha','pirganj','poradaha','pyerpur',
             'qosba',
             'rajapur','pajendrapur','pajshahi','rangpur','ruhiya',
             'sadanandapur','saidpur','santaher','sararchar','sarishabari','satabgonj','satkhamaer','sh_m_monsur_ali','shahagi_bazar','shaistagonj','shamshernagar','shemganj','shordha_road','shoshidol','sirajganj','sirajganj_bazar','sonaimuri','sonatola','srimangal','sripur','syadabad','sylhet',
             'tangail','tangi','tarakandi','tejgon','thakurakona','thakurgaon','thakurgaon_road','ullapara']

class_names=['tapanukul','first','1st','ac','second','2nd','shulov','shovon','non','s_chair','ac_b','ac_s','f_chair',
             'f_seat','singdha']
            
          
            
def WhereGoesOrComes(): #1...........
    place=0
    flag=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
    k=len(preA)
        
    

    for tt in nouns:
        for t in place_names:
            if t==tt:
                place=1
                place_add.append(t)
                
    
    for tt in nouns:
        for t in train_name:
            if t==tt:
                flag=1
                place_add.append(t)

                #if place==1:
                   # wheregoescomesfromto(t,place_add[0])
                #else:
                    #wheregoescomesfromto(t,'0')
       
    if flag==0:
        print('please mention train name correctly')
        
       
    if k!=0:
        for t in preA:
            place_add.append(t)
    answerDoc(place_add,1)        
        

def RouteHowManyOrRouteTrainNameNo(): #2...........


    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for tt in nouns:
        if tt=="train":
            place_add.append(tt)
            continue
        elif tt=="name" or tt=="number":
            place_add.append(tt)
            continue
        for t in place_names:
            if t==tt:
                plus=plus+1
                place_add.append(t)
        if plus==2:
           # a=place_add[0]
           # b=place_add[1]
            #RouteTrainNameNo(string,a,b)
            if k!=0:
                for t in preA:
                    place_add.append(t)
            answerDoc(place_add,2)   
        elif plus==1:
            print('please mention full route')
        else:
            print('mention place name correctly')
            
            
  
        
    
        
'''
 
    if("how many" in string):
        plus=0
        for word,pos in nltk.pos_tag(tokennns):
            nouns.append(word)
        
        for tt in nouns:
            for t in place_names:
                if t==tt:
                    plus=plus+1
                    place_add.append(t)
        if plus==2:
            a=place_add[0]
            b=place_add[1]
            #RouteHowMany(string,a,b)
        elif plus==1:
            print('please mention full route')
        else:
            print('mention place name correctly')
            
            
    elif("what" in string):
        ff
'''       
        
        
def OnlyNumber(): #3...........
    flags=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
    print(nouns)
    
    for t in train_name:
        for tt in nouns:
            if t==tt and flags==0:
                #giveAnsOfP3(t)
                place_add.append(t)
                place_add.append('train')
                answerDoc(place_add,3) 
                flags=1
        if flags==1:
            break
            
    if flags==0:
        print('please mention train name correctly')
             
                                    
           

def OnlyName():  #4...........
    flag=0
    for word,pos in nltk.pos_tag(tokennns):
        if pos == 'CD':
            cd=word
            flag=1
            break
    
    if flag==1:
        #giveAnsOfP4(cd)
        place_add.append(cd)
        place_add.append('train')
        answerDoc(place_add,4) 
    else:
        print('please mention train name correctly')


            
            
            
def Offday():   #5&6...........
    flags=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
    answerDoc(nouns,6)        
"""      
    for t in train_name:
        for tt in nouns:
            if t==tt:
                offday_with_trainName(t)
                flags=1
                break
        

    for tt in nouns:
        for t in place_names:
            if t==tt and flags==0:
                plus=plus+1
                place_add.append(t)
                
    if flags==0:
        if plus==2:
            a=place_add[0]
            b=place_add[1]
            offday_with_route(a,b)
        elif plus==1:
            print('please mention full route')
        else:
            print('mention place name correctly')

"""        


                
def listOfPlace():   #7...........
    flag=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
        

    for tt in nouns:
        for t in place_names:
            if t==tt:
                plus=plus+1
                flag=1
                place_add.append(t)
                
    if flag==1:
        if plus==1:
            a=place_add[0]
            listOfTrainsforAnyPlace(a)
        else:
            print('mention place name correctly')
            
    else:
        print('mention place name')




def seatFair_func():  #8...........
    flag=0
    plus=0
    one=0
    two=0
    three=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                place_add.append(t)
                flag=1
                plus=plus+1
                one=1
                
    for t in train_name:
        for tt in nouns:
            if t==tt:
                flag=1
                plus=plus+1
                two=1
                
    
    for t in class_names:
        for tt in nouns:
            if t==tt:
                flag=1
                plus=plus+1
                three=1
      
          
                
    if flag!=0:
        if plus==1:
            if one==1:
                print('not specified, missing train name, please provide more information')
            elif two==1:
                print('not specified, missing route, please provide more information')
            elif three==1:
                print('not specified, missing route, please provide more information')
        elif plus==2:
            if one==1 and two==0 and three==0:
                print('not specified, missing train name, please provide more information')
            elif two==1 and three==1:
                print('not specified, missing route, please provide more information')
            else:
                print('not specified, please provide more information')
        elif plus==3:
            if two==1 and three==1:
                print('g')
            if two==1:
                print('not specified, missing class, please provide more information')
            if three==1:
                print('not specified, missing train name, please provide more information')
        elif plus==4:
            a=place_add[0]
            b=place_add[1] 
            seatFair(nouns,a,b)
        else:
            print('not specified, please provide more information')
            
                
                
    if flag==0:
        print('sorry, not specificially asked')      
        


def nextOne():  #9...........
    flag=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                flag=1
                plus=plus+1
                place_add.append(t)
    
    if flag==1:
        if plus==1:
            t=place_add[0]
            nextStation(t,string)
        else:
            print('mention one place only')
    else:
        print('this is not a valid station')  


            

def ACtrain_available():    #10...........
    flag=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                flag=1
                plus=plus+1
                place_add.append(t)
            
    if flag==1:
        if plus==2:
            x=place_add[0]
            y=place_add[1]
            ACavailable(x,y)
        else:
            print('please provide full route information')
            
            
    else:
        print('not specified')      
        
        
        

def trainIfAvailable():   #11...........
    flag=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                flag=1
                plus=plus+1
                place_add.append(t)
            
    if flag==1:
        if plus==2:
            x=place_add[0]
            y=place_add[1]
     
            trainAvailable(x,y)
        else:
            print('please provide full route information')
            
            
    else:
        print('not specified')
        
     
        
def timeFunc():  #12...........
    flag=0
    plus=0
    one=0
    temp=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                flag=1
                plus=plus+1
                place_add.append(t)
                
                
    for t in train_name:
        for tt in nouns:
            if t==tt:
                one=t
                flag=1
                temp=1
                plus=plus+1
                
            
    if flag==1:
        if plus==1:
            print('please provide full route information')
        elif plus==2:
            if temp==1:
                print('please provide full route information')
            else:
                print('please provide train name')
        elif plus==3:
            x=place_add[0]
            y=place_add[1]
            train_time(x,y,one)
        else:
            print('please provide full information')
            
            
    else:
        print('not specified')
   
        
        
    
               
def howLong():  #13...........
    flag=0
    plus=0
    for word,pos in nltk.pos_tag(tokennns):
        nouns.append(word)
        
    for t in nouns:
        for tt in place_names:
            if t==tt:
                place_add.append(t)
                flag=1
                plus=plus+1
                
    
    if flag==1:
        if plus==2:
            a=place_add[0]
            b=place_add[1]
            how_long_it_takes(a,b)
        else:
            print('please provide full route information')
    else:    
        print('not specified')     
        
   
                            
    
def answer(patternNo,tokenn):
    for t in tokenn:
        if t not in ENGLISH_STOPS:
            tokennns.append(t);
            
    if patternNo==1:
        WhereGoesOrComes()
        
    elif patternNo==2:
        RouteHowManyOrRouteTrainNameNo()
            
    elif patternNo==3:
        OnlyNumber()
    
    elif patternNo==4:
        OnlyName()
    
    elif patternNo==5 or patternNo==6:
        Offday()
        
    elif patternNo==7:
        listOfPlace()
            
    elif patternNo==9:
        nextOne()
        
    elif patternNo==8:
        seatFair_func()
        
    elif patternNo==10:
        ACtrain_available()
        
        
    elif patternNo==11:
        trainIfAvailable()
        
        
    elif patternNo==12:
        timeFunc()
        
            
    elif patternNo==13:
        howLong()
        
        
        
        
    
    
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

#1 
p.append(r"(to where |from where |where |give )(does )?(train )?(no |named )?([a-z]*|\d{3,4})( start | come | depart | come | leave | go | travel | pass )(from )?(to |towards )?([a-z]*)")
#2
p.append(r"(per day )?(what |give |tell |how )(many )?(junction )?(route )?(is |me |us |are )?(number |name )?(of )?(train )?(available )?(travel )?(from |to )([a-z]* )(to |from )?([a-z]*)( route)?")
#3
p.append(r"(what |give |tell )(is |me |us )?(number |no )(train |train named |train name )([a-z]*|\D{3,4})")
#4
p.append(r"(what |give |tell )(is |me |us )?(name )?(train |train no |train number )(\d{1,5})")
#5
p.append(r"(on )?(which |give |tell |does )?(day )?(is |me |us )?(day )?(train |train no |train named )?(\d{3,4}|[a-z]*)( does not)?( go)([a-z]*)")
#6
p.append(r"(which |what )(is |are )?(offday )(train )?(number |named )?(\d{3,4}|[a-z]*)")
#7
p.append(r"(give |tell |what )(are |is )?(me |us )?(list )?(train )([a-z]*)")
#8
p.append(r"(what |tell |give )?(is |me |us )?(seat )?(fare |cost |price |pay |fee |charge )(traveling |going )?([a-z]*)?")
#9
p.append(r"(next |previous )(station )?([a-z]*)")
#10
p.append(r"(is )?(there )?(ac | air condition )(system )?(in )?(train )(from |to )([a-z]* )(to |from )?([a-z])*")
#11
p.append(r"(is |are )?(there )?(train )?([a-z]*)?( available )(night )?(to )?(go )?([a-z]*)")
#12
p.append(r"(when |what |give )(does |is )?([a-z]* )?(time |schedule )(of )?(the )?(train |train no |train named )?([a-z]*|\d{3})")
#13
p.append(r"(how |what )(many )?([a-z]* )?(long |time |hour )(train )?([a-z]*)( take )?(travelling )?([a-z]*)")




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
        if t not in extra:
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
string2=""
string=""
for t in lemmatized:
    for k in pre:
        if t==k:
            preA.append(t);
    string=string+t+" "
    string2=string2+"("+t+" )"
print('Pattern is: ' + string2)
cnt=0 



pattern_flag=0
leave=0

if "why" in string or "buy" in string or "book" in string or "give ticket" in string:
    print(t)
    leave=1
    
if leave==1:
    print('...sorry, NOT ANSWERED...')    
  
else:
    for t in p:
        cnt=cnt+1
        if re.search(t,string):
            print("yes matched precision 1")
            print("Pattern ",cnt)
            print(t)
            m=t
            answer(cnt,lemmatized)
            pattern_flag=1
            break

    if pattern_flag==0:
        fixed_answer(inp)
        
        


#if m==0:
    #num=precision_count(string,len(string))
    #print("Pattern ",num+1)
    #print(p[num])


