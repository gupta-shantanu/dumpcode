
sieve=[ False for i in range(0,50000)]
primes=[]
for i in range(2,50000):
    if sieve[i]:
        continue
    primes.append(i)
    for j in range(i,50000,i):
        sieve[j]=True
n=int(input())
for i in range(0,n):
    k=int(input())
    for j in primes:
        divisors=0
        if j>k:
            break
        while not k%j:
            k/=j
            divisors+=1
        ans*=divisors+1
            
