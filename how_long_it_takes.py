khulna_chilahati=["khulna", "jessore", "court chandpur","darsana","chuadanga","alamdanga","poradaha",
                  "bhairamara","pakshi","ishurdi","natore","ahasangang","santahar","accalpur","joypurhat",
                  "birampur","phulbari","parbatipur","saidpur","neelfamari","domar","chilahati"]



dhaka_chittagong=["dhaka","bimanbondor","narsingdi","bhairavbazar","ashuganj","brahmanbaria","akhaura","qosba",
                  "comilla","laksam","nangalkot","gunaboti","feni","chittagong"]

def how_long_it_takes(x,y):
    flag=0
    if x in khulna_chilahati:
        if y in khulna_chilahati:
            flag=1
            if x=='khulna' and y=='jessore':
                print('1hour')
            if x=='khulna' and y=='chilahati':
                print('6hour')
            else:
                print('4 hour+-')
        else:
            print('does not go there')
            
    elif x in dhaka_chittagong:
        if y in dhaka_chittagong:
            flag=1
            print('a* prg')
        else:
            print('does not go there')
            
        
        

            
    