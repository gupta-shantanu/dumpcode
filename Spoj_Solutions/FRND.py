
n=int(input())

zero=[0 for i in range(0,20)]
one=[0 for i in range(0,20)]
##l=[]
for i in range(0,n):
    k=int(input())
    p=0
##    l.append(k)
    while p<20:
        if k&1:
            one[p]+=1
        else:
            zero[p]+=1
        k>>=1
        p+=1
        

##s=0
##for i in range(0,len(l)):
##        for j in range(i+1,len(l)):
##            s+=l[i]^l[j]

ans=0
bit=1
for i,j in zip(zero,one):
    if i and j:
        ans+=bit*i*j
    bit<<=1

if n>1: 
    print(ans)
else:
    print(n)
#print(s)
