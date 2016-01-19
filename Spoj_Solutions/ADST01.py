##def recur(a,left):
##    global count
##    if left==0:
##        l=len(str(a))
##        for i in str(a):
##            for j in str(a):
##                if abs(int(i)-int(j))>1:
##                    return
##        p=sum([int(i) for i in str(a)])
##        if (p-1)==5*l:
##            count+=1
##            print(a)
##            d.append(a)
##        return
##    
##    recur(a*10+a%10,left-1)
##    if (a%10<9):
##        recur(a*10+(a%10+1),left-1)
##
##for j in range(1,20):
##    for i in range(1,10):
##        recur(i,j-1)
##print(count)
##r=[]
##for i in range(1,100):
##    print(sum(d[:i])%100000007)

t=int(input())
while(t):
    t-=1
    n=int(input())
    print((n+5*prod(n))%100000007)
