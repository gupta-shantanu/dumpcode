t=int(input())
while(t):
 m=int(raw_input().split()[1])
 print -1*sum(sorted([((0,int(i))[int(i)<0]) for i in raw_input().split()])[:m])
 t-=1
