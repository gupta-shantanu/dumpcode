n=int(input())

def gcd(a,b):
    if b==0:
        return a
    if a==0:
        return b

    return gcd(b,a%b)

for l in range(1,n+1):
    a,b,c=[int(i) for i in input().split()]
    if a==0 and b==0:
        if c==0:
                print("Case %d: Yes"%(l))
        else:
                print("Case %d: No"%(l))
            
        
    elif not c%gcd(a,b):
        print("Case %d: Yes"%(l))
    else:
        print("Case %d: No"%(l))
