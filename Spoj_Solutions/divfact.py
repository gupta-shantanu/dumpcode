primes=[2]
power=dict()
def recur(n):
    global power
    for i in primes:
        if i>n**0.5:
            break
        while not n%i:
            power[i]+=1
            n/=i
    if n>1:
        if(n>primes[-1]):
            primes.append(n)
        if n in power:
            power[n]+=1
        else:
            power[n]=1

def main(k):
    global power
    power=dict()
    for i in range(2,k+1):
        recur(i)
    ans=1
    for i in power:
        ans=(ans%1000000007*(power[i]+1)%1000000007)%1000000007
    print(ans)

n=int(input())           
for i in range(0,n):
    k=int(input())
    main(k)
