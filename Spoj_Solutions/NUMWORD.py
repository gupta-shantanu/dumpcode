y=10
h=100
m=y*h
k=' '
x='teen'
d=['zero','one','two','three','four','five','six','seven','eight','nine']
s=['ten','eleven','twelve','thir'+x,d[4]+x,'fif'+x,d[6]+x,d[7]+x,d[8]+'een',d[9]+x]
t=['','','twen','thir','for','fif',d[6],d[7],'eigh',d[9]]
w={h:'hundred',m:'thousand'}
def r(a):
 e=a%y
 if a<20:return (s[e],d[e])[a<y]
 if a<100:return t[a//y]+"ty"+(k+d[e],"")[e<1]
 l=h if a<m else m
 return r(a//l)+k+w[l]+(k+r(a%l),"")[e<1]
print(r(int(input())))
