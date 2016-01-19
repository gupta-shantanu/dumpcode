n=int(input())
sieve=[ 0 for i in range(0,2000000)]
rank=[]
for i in range(2,200000):
    if sieve[i]>0:
        if sieve[i]==2:
            rank.append(i)
        continue
    for j in range(i,2000000,i):
        sieve[j]+=1
print("ok")
for i in range(0,n):
    k=int(input())
    print(rank[k-1])
