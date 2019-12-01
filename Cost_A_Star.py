# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:26:07 2019

@author: Asus
"""

import operator
"""
graph1 = {
        'subarna':['dhaka','biman_bandar','chittagong'],
        'sonar_bangla':['dhaka','biman_bandar','chittagong'],
        'mahanagar_provati':["dhaka","biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        'mahanagar_godhuli':["dhaka","biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        'mahanagar':["dhaka","biman_bandar","narsingdi","bhairab_bazar","ashuganj","brahmanbaria","akhaura","qosba","comilla","laksam","nangalkot","feni","chittagong"],
        'turna':["dhaka","biman_bandar","bhairab_bazar","ashuganj","brahmanbaria","akhaura","comilla","laksam","feni","chittagong"],
        'ekota':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ishurdi_bypass','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur'],
        'drutajan':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','jamtail','chatmohar','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur'],

        'doloncapa':['santahar','talora','bogura','sonatola','mohimaganj','bonar_para','gaibandha','bamondanga','kaunia','rangpur','badar_ganj','kholahati','parbatipur','cirir_bandar','dinajpur'],


        'tista':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar'],
        'brahmaputro':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','nandina','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar'],


        'parabat':['dhaka','biman_bandar','bhairab_bazar','brahmanbaria','azampur','nayapara','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet'],
        'kalni':['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet'],
        'joyenteeka':['dhaka','biman_bandar','ashuganj','bhairab_bazar','azampur','mukundupur','horoshpur','montala','nayapara','shahagi_bazar','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet'],
        'upaban':['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet'],


        'upakul':['dhaka','biman_bandar','narsingdi','bhairab_bazar','ashuganj','brahmanbaria','akhaura','qosba','comilla','laksam','nathar_patua','sonaimuri','bojra','choumuhani','maijdi_court','noakhali'],


        'korotaya':['santaher','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat','aditmari','tushvandar','hatibandha','patgram','burimari'],


        'paharika':['chittagong','feni','nangalkot','laksam','comilla','qosba','akhaura','horoshpur','nayapara','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet'],
        'udayan':['chittagong','feni','laksam','comilla','akhaura','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet'],


        'meghna':['chittagong','feni','nangalkot','laksam','chitosi_road','meher','hajiganj','modhu_road','chandpur_court','chandpur'],


        'augnibina':['dhaka','biman_bandar','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi'],
        'jamuna':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi'],
 

        'egarosindur_provati':['dhaka','biman_bandar','narsingdi','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],
        'kishoreganj':['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],
        'egarosindur_godhuli':['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],



        'lalmoni':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ullapara','boral_bridge','agimnagar','natore','santahar','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat'],


        'rangpur':['dhaka','biman_bandar','bbsetu_e','chatmohar','natore','santahar','bogura','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','kurigram','rangpur'],
        'kurigram':['dhaka','biman_bandar','madhnagar','santahar','joypurhat','parbatipur','badar_ganj','rangpur'],


        'mohonganj':['dhaka','biman_bandar','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj'],
        'haowr':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj'],


        'bijoy':['chittagong','bhatiary','feni','laksam','comilla','akhaura','bhairab_bazar','kishoreganj','gouripur_myn','mymensingh'],

 
        'kopotakha':['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','pakshi','ishurdi','agimnagar','rajshahi'],
        'shagordari':['khulna','noapara','jessore','mobarakgong','court_chandpur','safdarpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','agimnagar','rajshahi'],


        'chitra':['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],
        'sundarban':['khulna','daulatpur','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],


        'rupsa':['khulna','noapara','jessore','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','natore','ahasangang','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','chilahati'],
        'seemanta':['khulna','daulatpur','noapara','jessore','darsana_halt','chuadanga','poradaha','bhairamara','ishurdi','natore','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'borendra':['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],
        'titumir':['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'banalata':['rajshahi','dhaka'],
        'silk_city':['rajshahi','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],
        'padma':['rajshahi','shordha_road','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','jaydebpur','biman_bandar','dhaka'],
        'dhumkatu':['rajshahi','abdulpur','arani','chatmohar','boral_bridge','sm_m_monsur_ali','bbsetu_e','jaydebpur','biman_bandar','dhaka'],


        'modhumati':['rajshahi','ishurdi','pakshi','bhairamara','mirpur','poradaha','kustia','kustia_court','kumarkhali','khoksa','pangsha','kalukhali','rajbari','goalandaghat'],


        'nelsagore':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','muladuli','natore','ahasangang','santahar','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'sirajganj':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','jamtail','sirajganj_bazar','sirajganj'],

 
        'bandhan':['kolkata','khulna'],
        'moitree':['kolkata','dhaka_cantt'],


        'faridpur':['faridpur','rajbari']
         }

graph = {
        'subarna':['dhaka','biman_bandar','chittagong'],'sonar_bangla':['dhaka','biman_bandar','chittagong'],
        'mahanagar_provati':["dhaka","biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        'mahanagar_godhuli':["dhaka","biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        'mahanagar':["dhaka","biman_bandar","narsingdi","bhairab_bazar","ashuganj","brahmanbaria","akhaura","qosba","comilla","laksam","nangalkot","feni","chittagong"],
        'turna':["dhaka","biman_bandar","bhairab_bazar","ashuganj","brahmanbaria","akhaura","comilla","laksam","feni","chittagong"],
        'ekota':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ishurdi_bypass','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur'],
        'drutajan':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','jamtail','chatmohar','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur'],

        'doloncapa':['santahar','talora','bogura','sonatola','mohimaganj','bonar_para','gaibandha','bamondanga','kaunia','rangpur','badar_ganj','kholahati','parbatipur','cirir_bandar','dinajpur'],


        'tista':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar'],
        'brahmaputro':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','nandina','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar'],


        'parabat':['dhaka','biman_bandar','bhairab_bazar','brahmanbaria','azampur','nayapara','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet'],
        'kalni':['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet'],
        'joyenteeka':['dhaka','biman_bandar','ashuganj','bhairab_bazar','azampur','mukundupur','horoshpur','montala','nayapara','shahagi_bazar','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet'],
        'upaban':['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet'],


        'upakul':['dhaka','biman_bandar','narsingdi','bhairab_bazar','ashuganj','brahmanbaria','akhaura','qosba','comilla','laksam','nathar_patua','sonaimuri','bojra','choumuhani','maijdi_court','noakhali'],


        'korotaya':['santaher','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat','aditmari','tushvandar','hatibandha','patgram','burimari'],


        'paharika':['chittagong','feni','nangalkot','laksam','comilla','qosba','akhaura','horoshpur','nayapara','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet'],
        'udayan':['chittagong','feni','laksam','comilla','akhaura','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet'],


        'meghna':['chittagong','feni','nangalkot','laksam','chitosi_road','meher','hajiganj','modhu_road','chandpur_court','chandpur'],


        'augnibina':['dhaka','biman_bandar','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi'],
        'jamuna':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi'],
 

        'egarosindur_provati':['dhaka','biman_bandar','narsingdi','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],
        'kishoreganj':['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],
        'egarosindur_godhuli':['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj'],



        'lalmoni':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ullapara','boral_bridge','agimnagar','natore','santahar','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat'],


        'rangpur':['dhaka','biman_bandar','bbsetu_e','chatmohar','natore','santahar','bogura','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','kurigram','rangpur'],
        'kurigram':['dhaka','biman_bandar','madhnagar','santahar','joypurhat','parbatipur','badar_ganj','rangpur'],


        'mohonganj':['dhaka','biman_bandar','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj'],
        'haowr':['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj'],


        'bijoy':['chittagong','bhatiary','feni','laksam','comilla','akhaura','bhairab_bazar','kishoreganj','gouripur_myn','mymensingh'],

 
        'kopotakha':['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','pakshi','ishurdi','agimnagar','rajshahi'],
        'shagordari':['khulna','noapara','jessore','mobarakgong','court_chandpur','safdarpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','agimnagar','rajshahi'],


        'chitra':['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],
        'sundarban':['khulna','daulatpur','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],


        'rupsa':['khulna','noapara','jessore','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','natore','ahasangang','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','chilahati'],
        'seemanta':['khulna','daulatpur','noapara','jessore','darsana_halt','chuadanga','poradaha','bhairamara','ishurdi','natore','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'borendra':['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],
        'titumir':['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'banalata':['rajshahi','dhaka'],
        'silk_city':['rajshahi','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka'],
        'padma':['rajshahi','shordha_road','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','jaydebpur','biman_bandar','dhaka'],
        'dhumkatu':['rajshahi','abdulpur','arani','chatmohar','boral_bridge','sm_m_monsur_ali','bbsetu_e','jaydebpur','biman_bandar','dhaka'],


        'modhumati':['rajshahi','ishurdi','pakshi','bhairamara','mirpur','poradaha','kustia','kustia_court','kumarkhali','khoksa','pangsha','kalukhali','rajbari','goalandaghat'],


        'nelsagore':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','muladuli','natore','ahasangang','santahar','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati'],


        'sirajganj':['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','jamtail','sirajganj_bazar','sirajganj'],

 
        'bandhan':['kolkata','khulna'],
        'moitree':['kolkata','dhaka_cantt'],


        'faridpur':['faridpur','rajbari']
         }
"""



subarna={'dhaka':['biman_bandar','chittagong'],'biman_bandar':['dhaka','chittagong'],'chittagong':['biman_bandar','dhaka']}
sonar_bangla={'dhaka':['biman_bandar','chittagong'],'biman_bandar':['dhaka','chittagong'],'chittagong':['biman_bandar','dhaka']}
mahanagar_provati={
        "dhaka":["biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        "biman_bandar":["dhaka","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        "bhairab_bazar":["dhaka","biman_bandar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"],
        }
mahanagar_godhuli=["dhaka","biman_bandar","bhairab_bazar","brahmanbaria","akhaura","comilla","laksam","gunaboti","feni","chittagong"]
mahanagar=["dhaka","biman_bandar","narsingdi","bhairab_bazar","ashuganj","brahmanbaria","akhaura","qosba","comilla","laksam","nangalkot","feni","chittagong"]
turna=["dhaka","biman_bandar","bhairab_bazar","ashuganj","brahmanbaria","akhaura","comilla","laksam","feni","chittagong"]


ekota=['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ishurdi_bypass','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur']
drutajan=['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','jamtail','chatmohar','natore','santahar','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','cirir_bandar','dinajpur']

doloncapa=['santahar','talora','bogura','sonatola','mohimaganj','bonar_para','gaibandha','bamondanga','kaunia','rangpur','badar_ganj','kholahati','parbatipur','cirir_bandar','dinajpur']


tista=['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar']
brahmaputro=['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','pyerpur','nandina','jamalpur','jamalpur_town','melandah_bazar','islampur_bazar','dewanganj_bazar']


parabat=['dhaka','biman_bandar','bhairab_bazar','brahmanbaria','azampur','nayapara','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet']
kalni=['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet']
joyenteeka=['dhaka','biman_bandar','ashuganj','bhairab_bazar','azampur','mukundupur','horoshpur','montala','nayapara','shahagi_bazar','shaistagonj','srimangal','bhanugach','kulaura','maizgaon','sylhet']
upaban=['dhaka','biman_bandar','narsingdi','bhairab_bazar','azampur','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet']


upakul=['dhaka','biman_bandar','narsingdi','bhairab_bazar','ashuganj','brahmanbaria','akhaura','qosba','comilla','laksam','nathar_patua','sonaimuri','bojra','choumuhani','maijdi_court','noakhali']


korotaya=['santaher','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat','aditmari','tushvandar','hatibandha','patgram','burimari']


paharika=['chittagong','feni','nangalkot','laksam','comilla','qosba','akhaura','horoshpur','nayapara','shaistagonj','srimangal','bhanugach','shamshernagar','kulaura','maizgaon','sylhet']
udayan=['chittagong','feni','laksam','comilla','akhaura','shaistagonj','srimangal','shamshernagar','kulaura','maizgaon','sylhet']


meghna=['chittagong','feni','nangalkot','laksam','chitosi_road','meher','hajiganj','modhu_road','chandpur_court','chandpur']


augnibina=['dhaka','biman_bandar','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi']
jamuna=['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','jamalpur','jamalpur_town','sarisha_bari','tarakandi']
 

egarosindur_provati=['dhaka','biman_bandar','narsingdi','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj']
kishoreganj=['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj']
egarosindur_godhuli=['dhaka','biman_bandar','narsingdi','methikanda','bhairab_bazar','kuliarchar','bajipur','sararchar','manik_khali','gachihata','kishoreganj']



lalmoni=['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','ullapara','boral_bridge','agimnagar','natore','santahar','bogura','sonatola','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','lalmonirhat']


rangpur=['dhaka','biman_bandar','bbsetu_e','chatmohar','natore','santahar','bogura','bonar_para','gaibandha','bamondanga','pirgacha','kaunia','kurigram','rangpur']
kurigram=['dhaka','biman_bandar','madhnagar','santahar','joypurhat','parbatipur','badar_ganj','rangpur']


mohonganj=['dhaka','biman_bandar','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj']
haowr=['dhaka','biman_bandar','jaydebpur','gafargaon','mymensingh','gouripur_myn','shemganj','netrokona','thakurakona','barhatta','mohonganj']


bijoy=['chittagong','bhatiary','feni','laksam','comilla','akhaura','bhairab_bazar','kishoreganj','gouripur_myn','mymensingh']

 
kopotakha=['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','pakshi','ishurdi','agimnagar','rajshahi']
shagordari=['khulna','noapara','jessore','mobarakgong','court_chandpur','safdarpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','agimnagar','rajshahi']


chitra=['khulna','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','mirpur','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka']
sundarban=['khulna','daulatpur','noapara','jessore','mobarakgong','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','ishurdi','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka']


rupsa=['khulna','noapara','jessore','court_chandpur','darsana_halt','chuadanga','alamdanga','poradaha','bhairamara','pakshi','ishurdi','natore','ahasangang','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','chilahati']
seemanta=['khulna','daulatpur','noapara','jessore','darsana_halt','chuadanga','poradaha','bhairamara','ishurdi','natore','santaher','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati']


borendra=['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati']
titumir=['rajshahi','abdulpur','natore','ahasangang','santaher','accalpur','joypurhat','panchabibi','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati']


banalata=['rajshahi','dhaka']
silk_city=['rajshahi','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','jamtail','sm_m_monsur_ali','bbsetu_e','tangail','mirzapur','jaydebpur','biman_bandar','dhaka']
padma=['rajshahi','shordha_road','abdulpur','ishurdi','ishurdi_bypass','chatmohar','boral_bridge','ullapara','sm_m_monsur_ali','bbsetu_e','tangail','jaydebpur','biman_bandar','dhaka']
dhumkatu=['rajshahi','abdulpur','arani','chatmohar','boral_bridge','sm_m_monsur_ali','bbsetu_e','jaydebpur','biman_bandar','dhaka']


modhumati=['rajshahi','ishurdi','pakshi','bhairamara','mirpur','poradaha','kustia','kustia_court','kumarkhali','khoksa','pangsha','kalukhali','rajbari','goalandaghat']


nelsagore=['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','muladuli','natore','ahasangang','santahar','accalpur','joypurhat','birampur','phulbari','parbatipur','saidpur','neelfamari','domar','chilahati']


sirajganj=['dhaka','biman_bandar','jaydebpur','tangail','bbsetu_e','sm_m_monsur_ali','jamtail','sirajganj_bazar','sirajganj']

 
bandhan=['kolkata','khulna']
moitree=['kolkata','dhaka_cantt']


faridpur=['faridpur','rajbari']
h = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}
dist = {}
f = {}
g = {}

start = 'Arad'
goal = 'Bucharest'

#f[start] = h[start]
#print f

def a_star_search(start,goal):
    
    g[start]=0
    
    if (h[start]==h[goal]):
        print ('Road found')
        return 0
    
    while True:
        if start in graph1:
            #print('\n\n'+start)    
            for n in graph1[start].keys():
                g[n] = g[start] + graph1[start][n]
                f[n] = h[n] + g[n]
                #print (f[n])
            
        fringe = sorted(f.items(), key=operator.itemgetter(1))
        #f = fringe
        #print (fringe)
        print (start,'(',h[start]+g[start],') ->',end="")
        start = fringe[0][0]
        f.__delitem__(start)
        if fringe[0][0] == goal:
            print (start,'(',h[start]+g[start],')',end="")
            break
                  
a_star_search(start,goal)