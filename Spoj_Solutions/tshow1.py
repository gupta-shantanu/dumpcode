n=int(input())
for i in range(0,n):
    k=int(input())
    digits=1
    while(2**(digits+1)-2<k):
        digits+=1
    rank=k-2**digits+1
    st=(bin(rank)[2:]).rjust(digits,"0")
    ans=""
    for i in st:
        if i=='0':
            ans+='5'
        else:
            ans+='6'

    print(ans)
    
