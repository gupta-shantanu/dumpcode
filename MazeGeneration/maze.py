from random import randint
k=10
a=[[10000 for i in range(0,k**2)] for j in range(0,k**2)]
##0 1 2 3
##4 5 6 7
##8 9 0 1
##2 3 4 5


def prim(a):
    vw={j for j in range(0,len(a))}
    v={0}
    e=[]
    while v!=vw:
        edge=getmin(v,a)
        v.add(edge[1])
        v.add(edge[0])
        e.append(edge)
    print("done")
    return e
def kruskal(a):
    vlist=[]
    edges=[]
    for i in range(0,k**2):
        for j in range(0,k**2):
            if a[i][j]!=10000:
                x=dset(i)
                y=dset(j)
                vlist.append(x)
                vlist.append(y)
    for i in range(0,k**2):
        for j in range(0,k**2):
            if a[i][j]!=10000:
                edges.append([i,j,a[i][j]])
                

    edges.sort(key=lambda x:x[2])
    x=[]      
    for i in edges:
        if getset(i[0],vlist).find()!=getset(i[1],vlist).find():
            x.append((i[0],i[1]))
            getset(i[0],vlist).union(getset(i[1],vlist))
    return x

def getset(a,b):
    for i in b:
        if i.value==a:
            return i
    return 0
        

    
                
                


class dset:
    def __init__(self,a):
        self.value=a
        self.parent=self
        

    def find(self):
        if self==self.parent:
            return self
        return (self.parent).find()
    def union(self,b):
        p1=self.find()
        p2=b.find()
        p1.parent=p2
        
    


def getmin(v,a):
    smallest=1000
    source=0
    destiny=1000
    for ch in range(0,k**2):
        if v.__contains__(ch):
            
            for t in range(0,k**2):
                if a[ch][t]<smallest and not v.__contains__(t):
                    smallest=a[ch][t]
                    source=ch
                    destiny=t
                elif a[t][ch]<smallest and not v.__contains__(t):
                    smallest=a[t][ch]
                    source=t
                    destiny=ch
    return (source,destiny)

for i in range(0,k**2):
    if i+1< k*(i//k+1) and a[i+1][i]==10000:
        a[i][i+1]=randint(1,10)
    if i-1>=k*i and a[i-1][i]==10000:
        a[i][i-1]=randint(1,10)
        
    if i-k>0 and a[i-k][i]==10000:
        a[i][i-k]=randint(1,10)
    if i+k<k**2 and a[i+k][i]==10000:
        a[i][i+k]=randint(1,10)

def calcweight(b,a):
    s=0
    for ch in b:
        s=s+a[ch[0]][ch[1]]
    return s


def resolvePoints(n,k,c):
    return (n%k*50-500+600*(c-1),int(n/k)*50-300)

def drawmaze(a,k,n):
    import turtle
    wn=turtle.Screen()
    wy=turtle.Screen()
    wn.colormode(255)
    wn.screensize(500,500)

    pn = turtle.Turtle()
    pn.speed(0)
    pn.setpos(0,0)
    pn.pensize(10)
    if n==1:
        pn.pen(fillcolor="black", pencolor="red", pensize=30)
    else:
        pn.pen(fillcolor="black", pencolor="blue", pensize=30)
        
    pn.pu()
    for ch in a:
        p=resolvePoints(ch[0],k,n)
        q=resolvePoints(ch[1],k,n)
        pn.setpos(p)
        pn.pd()
        pn.setpos(q)
        pn.pu()


u=prim(a)
x=kruskal(a)
print(u)
print(x)
print("kruskal weight "+str(calcweight(x,a)))
print("prim weight "+str(calcweight(u,a)))
drawmaze(x,k,1)
drawmaze(u,k,2)

