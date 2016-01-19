primes=[2]
power=dict()
def recur(n):
    global power
    k=n**0.5
    if power.__contains__(n):
        power[n]+=1
        
    else:
        fl=1
        for i in primes:
            if i>k:
                break
            if not n%i:
                recur(min(n//i,i))
                recur(max(n//i,i))
                fl=0
                break
        if fl:
            if(n>primes[-1]):
                primes.append(n)
            power[n]=1
                

def main(k):
    global power
    power=dict()
    for i in range(2,k+1):
        recur(i)
    print(power)
    ans=1
    ch=0
    for i in power:
        ch+=power[i]
        ans=(ans%1000000007*(power[i]+1)%1000000007)%1000000007
    print(ch,ans)

n=int(input())           
for i in range(0,n):
    k=int(input())
    main(k)
