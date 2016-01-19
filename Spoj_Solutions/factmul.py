n=int(input())

ans=1
fact=1
if n>587116:
    print(0)
else:
    for i in range(2,n+1):
        fact=(fact*i)%109546051211
        ans=(ans*fact)%109546051211
    print(ans)
