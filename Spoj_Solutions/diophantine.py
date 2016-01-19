w=int(input())
n=[]
for i in range(0,w):
    n.append(int(input()))

pro={0:0}

for i in range(0,w):
    for j in range(0,w):
        for k in range(0,w):
            d=n[i]*n[j]+n[k]
            if pro.__contains__(d):
                pro[d]=pro[d]+1
            else:
                pro[d]=1

ans=0
for i in range(0,w):
    for j in range(0,w):
        for k in range(0,w):
            d=n[i]*(n[j]+n[k])
            if pro.__contains__(d):
                    if n[i]!=0:
                        ans=ans+pro[d]
print(ans)
