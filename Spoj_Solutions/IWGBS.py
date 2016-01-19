count=0
import sys
sys.setrecursionlimit(10000)
def recur(depth,prev):
    
    if depth==n:
        global count
        count+=1
        return
    recur(depth+1,1)
    if prev!=0:
        recur(depth+1,0)


b=(1-5**0.5)/2
a=(1+5**0.5)/2
root5=5**0.5
def nthfib(n):
    return int((a**n/root5))
dic=dict()
def fib(n):
    if n<=1:
        return 1
    ans=0
    if n in dic:
        return dic[n]
    dic[n]=fib(n-2)+fib(n-1)
    return dic[n]

    
n=int(input())
if n>0:
    #print(nthfib(n+2))
    print(fib(n+1))
else:
    print(0)


