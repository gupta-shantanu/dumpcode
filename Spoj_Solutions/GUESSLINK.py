while True:
    try:
        n=input().split('/')[-2]
    except:
        break
    b=n[6:]
    a="%06d"%(((int(n[3:6])+991)*1000+(int(n[:3])+36))%1000000)

    A=0
    B=0

    for i in range(0,6):
        for j in range(0,6):
            if a[i]==b[j]:
                if i==j:
                    A+=1
                else:
                    B+=1
                
                
    print(A,"A",B,"B",sep='')

            
