s=1366660;p=0;r=range;v=[0 for i in r(0,s)];v[1]=1
for i in r(2,s):
 if v[i]<1:
  p+=1
  if v[p]<1:print(i,end=' ')
  for j in r(i+i,s,i):v[j]=1
print(s+1)
