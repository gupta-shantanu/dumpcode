n=int(input())
d=dict()


def create_map(s):
    for p,i in enumerate(s):
        d[ord(i)]=p
for ln in range(0,n):
    create_map(input())
    a=input()
    b=input()
    fl=True
    for i,j in zip(a,b):
        x=ord(i)
        y=ord(j)
        if d[x]<d[y]:
            print("<")
            fl=False
            break
        elif d[x]>d[y]:
            print(">")
            fl=False
            break
    if fl:
        x=len(a)
        y=len(b)
        if x<y:
            print("<")
        elif y>x:
            print(">")
        else:
            print("=")
