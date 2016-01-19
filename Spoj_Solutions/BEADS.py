n=int(input())
for i in range(0,n):
    k=input()
    ans=0
    lk=len(k)
    k+=k
    for p in range(1,lk):
        for j in range(p,p+lk):
            if k[j]<k[j-p+ans]:
                ans=p
                break
            elif k[j]>k[j-p+ans]:
                break
    print(ans+1)
    
    
