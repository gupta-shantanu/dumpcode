n=int(input())
#sffx array
for i in range(0,n):
    input()
    k=int(input())
    arr=[0 for kj in range(0,k+1)]

    for j in range(0,k):
        rank=int(input().split()[-1])
        arr[rank]+=1

    actual=0
    ans=0
    for j in range(1,k+1):
        t=arr[j]
        ans+=abs((t*t+2*t*actual+t)//2-j*t)
        actual+=arr[j]
    print(ans)
    
    
