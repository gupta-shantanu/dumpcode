sieve=[ 0 for i in range(0,100000)]
rank=[]
for i in range(2,100000):
    if sieve[i]>0:
        continue
    for j in range(2*i,100000,i):
        sieve[j]+=1
print("ok")
for i in range(0,100):
    k=int(input())
    print("YES" if(sieve[k]==2) else "NO")
