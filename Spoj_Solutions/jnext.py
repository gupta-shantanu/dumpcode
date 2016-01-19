n=int(input())

for i in range(0,n):
    k=int(input())
    num=[int(i) for i in input().split()]
    avail=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(num)-1,-1,-1):
        flag=False
        for j in range(num[i]+1,10):
            if avail[j]>0:
                flag=True
                avail[num[i]]+=1
                avail[j]-=1
                num[i]=j
                break
        if flag:
            
            for k in range(i+1,len(num)):
                flag=False
                for j in range(0,10):
                    if avail[j]>0:
                        flag=True
                        num[k]=j
                        avail[j]-=1
                        break
                if not flag:
                    break
            break
        else:
            avail[num[i]]+=1
    
    if flag:
        for i in num:
            print(i,end='')
        print()
    else:
        print(-1)
            
                
