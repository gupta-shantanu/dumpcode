cas=1
while True:
    n=int(input())
    if n==0:
        break
    print("Case",str(cas)+',','N =',str(n)+',',"# of different labelings =",n**(n-2) if n>1 else 1)
    cas+=1
