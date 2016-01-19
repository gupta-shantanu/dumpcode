def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)


while(1):
    l=[int(i) for i in input().split()]
    a,b,c=sorted(l)
    if(a==0):
        print("YES" if(abs(b)==abs(c)) else "NO")
    elif(b==0):
        print("YES" if(abs(a)==abs(c)) else "NO")
    elif(c==0):
        print("YES" if(a==0 and b==0) else "NO")
    elif((a**2+b**2)==(c**2) and gcd(a,gcd(b,c))==1):
        print("YES")
    else:
        print("NO")


