key=["063", "010", "093", "079", "106", "103", "119", "011", "127", "107"]
mapping={"063":0,"010":1,"093":2, "079":3, "106":4, "103":5, "119":6, "011":7, "127":8, "107":9}

def numerize(n):
    num=0
    for i in range(0,len(n),3):
        num=num*10+mapping[n[i:i+3]]
    return num
while True:
    a=input()
    if a=="BYE":
        break
    l=a.split('+')
    an=numerize(l[0])+numerize(l[1][:-1])
    s=str(an)
    ans=""
    for i in s:
        ans+=key[int(i)]
    print(a+ans)



    
