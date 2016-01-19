n=int(input())
for i in range(0,n):
    k=int(input())
    ans=0
    if(k&1):
        print(k)
    else:
        while(k):
            ans<<=1
            ans+=k&1
            k>>=1

        print(ans)
