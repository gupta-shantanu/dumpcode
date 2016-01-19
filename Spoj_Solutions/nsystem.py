n=int(input())
const=['i','x','c','m']
arr={'m':0,'c':0,'x':0,'i':0}
for i in range(0,n):
    a=input()
    prev=1
    for i in a:
        if i==' ':
            prev=1
            continue
        if ord(i)<58:
            prev=int(i)
        else:
            arr[i]+=prev
            prev=1
    ans=""
    carry=0
    for i in const:
        s=arr[i]+carry
        arr[i]=0
        k=s%10
        carry=s//10
        if k==0:
            continue
        if k==1:
            ans=i+ans
        else:
            
            ans=str(k)+i+ans
            
    print(ans)
