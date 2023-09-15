NUMS={0:"no",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}

def recite(start, take=1):
    rcte=[]   
    for tk in range(take,0,-1):
        verses=f"""{NUMS[start]} green {"bottle" if start==1 else "bottles"} hanging on the wall,
            {NUMS[start]} green {"bottle" if start==1 else "bottles"} hanging on the wall,
            And if one green bottle should accidentally fall,
            There'll be {NUMS[start-1].lower()} green {"bottle" if start-1==1 else "bottles"} hanging on the wall.
            """
        start-=1
        rcte.extend([verse.strip() for verse in verses.split("\n")])
        rcte.extend("")
        
    return rcte[:len(rcte)-1]