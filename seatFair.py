subarna_list=['dhaka','khulna']


def seatFair(s,a,b):
    if "subarna" in s:
        if a in subarna_list:
            if b in subarna_list:
                if "ac" in s:
                    print('900')
                elif "s_chair" in s:
                    print('700')
            else:
                print('does not go there')
        else:
            print('does not go there')
            
      
        
        
        
    if "ekota" in s:
        print('then')
        