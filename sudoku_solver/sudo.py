ls=[]
unk=[0,0]
def validate(k,x,y):
    if k in ls[x] :
        return False
    if any((k == ls[i][y]) for i in range(0,9)):
        return False
    a=int(x/3)*3
    b=(int(x/3)+1)*3
    c=int(y/3)*3
    d=(int(y/3)+1)*3
    if any((k==ls[i][j]) for i in range(a,b) for j in range(c,d)):
        return False
    return True
def poss(k):
    t={}
    prev=-1
    for i in range(k,al):
        s=a[i][0]
        q=a[i][1]
        t[s*10+q]=[p for p in range(1,10) if validate(p,s,q)]
        
    return t
            
    

for x in range(0,9):
    tmp=list(input())
    tmp=[int(i) for i in tmp]
    ls.append(tmp)
    unk[0]+=tmp.count(0)
        

def recur(x):
    for i in range(x,al):
        x=a[i][0]
        y=a[i][1]
        for p in po[x*10+y]:
            if not validate(p,x,y):
                continue
            ls[x][y]=p
            unk[0]-=1
            recur(i+1)
            if unk[1]==1 :
                return
            if unk[0]==0 and unk[1]==0 :
                 for l in range(0,9):
                    print(ls[l],"\n")
                 unk[1]=1
                 return
            unk[0]+=1
        ls[x][y]=0
        return
a=[]
for i in range(0,9):
    for j in range(0,9):
        if ls[i][j]==0:
            a.append([i,j])
al=len(a)
import time as t
t.clock()
r=t.clock()
po=poss(0)
print(t.clock()-r)
r=t.clock()
recur(0)
print(t.clock()-r)

           
           
